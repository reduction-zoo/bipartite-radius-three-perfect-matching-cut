import itertools
import json
import subprocess
import sys
from pathlib import Path
import networkx as nx
import z3

HERE=Path(__file__).resolve().parent
CANDIDATE=HERE.parents[1]/'work/algorithm.py'

def call(data, extract=False):
    result=subprocess.run([sys.executable,str(CANDIDATE)]+(['--extract'] if extract else []),input=json.dumps(data),text=True,capture_output=True,check=True)
    return json.loads(result.stdout)

def valid(g, bits):
    return len(bits)==len(g) and all(type(b)is int and b in (0,1) for b in bits) and len(set(bits))==2 and all(sum(bits[u]!=bits[v] for v in g[u])<=1 for u in g)

def local():
    results=[]
    # The local graph contains all private edges, with anchor colors fixed.
    blocks=[('binary',[(0,1),(0,2),(3,1),(3,2),(4,5),(4,6),(7,5),(7,6),(1,5),(2,6)],{0:1,3:0,4:0,7:1}),
            ('selector',[(1,j) for j in (2,3,4)]+[(0,j) for j in (5,6,7)]+[(j+2,k+5) for j in range(3) for k in range(3) if j!=k],{0:1,1:0})]
    for name,edges,anchors in blocks:
        g=nx.Graph();g.add_nodes_from(range(8));g.add_edges_from(edges)
        for opposite in (False,True):
            allowed=[]
            for bits in itertools.product((0,1),repeat=8):
                if any(bits[k]!=(v if opposite else 0) for k,v in anchors.items()):continue
                if any(sum(bits[k]!=bits[j] for j in g[k])>1 for k in g):continue
                allowed.append(bits)
                if not opposite:assert not any(bits)
                elif name=='binary':
                    assert bits[1]==bits[5] and bits[2]==bits[6] and bits[1]!=bits[2]
                    assert all(sum(bits[k]!=bits[j] for j in g[k])==1 for k in (1,2,5,6))
                else:
                    assert sum(bits[2:5])==1 and all(bits[k+5]==1-bits[k+2] for k in range(3))
                    assert all(sum(bits[k]!=bits[j] for j in g[k])==1 for k in (5,6,7))
            assert len(allowed)==(1 if not opposite else 2 if name=='binary' else 3)
            results.append({'block':name,'opposite_anchors':opposite,'assignments_examined':256,'legal_assignments':allowed})
    return results

def formula(g):
    x=[z3.Bool(f'x{i}') for i in g]
    s=z3.Solver()
    for u in g:
        if len(g[u])>1:s.add(z3.PbLe([(x[u]!=x[v],1) for v in g[u]],1))
    s.add(z3.Or(x),z3.Or([z3.Not(v) for v in x]))
    return s,x

def main():
    result={'local':local(),'full_outputs':[],'invalid_inputs':[]}
    for name,g in [('edge',nx.path_graph(2)),('three_vertex_path',nx.path_graph(3)),('biclique_two_three',nx.complete_bipartite_graph(2,3))]:
        source={'n':len(g),'edges':[sorted(e) for e in g.edges()]}
        output=call(source);h=nx.Graph();h.add_nodes_from(range(output['n']));h.add_edges_from(output['edges'])
        assert len(output['edges'])==h.number_of_edges() and not list(nx.selfloop_edges(h))
        assert nx.is_connected(h) and nx.is_bipartite(h)
        distances=nx.single_source_shortest_path_length(h,0);assert max(distances.values())<=3
        n=len(g);T=sum(len(g[v])*(len(g[v])-1)//2 for v in g);C=2*T+2*max(n-2,1);N=n+2*max(n-3,0)+6*C;K=4*C
        assert len(h)==12+8*N+8*K and h.number_of_edges()==19+18*N+19*K
        s,x=formula(h)
        truth=any(valid(g,b) for b in itertools.product((0,1),repeat=len(g)))
        decision=s.check();assert decision in (z3.sat,z3.unsat) and (decision==z3.sat)==truth
        recovered=0
        if decision==z3.sat:
            model=s.model();bits=[int(z3.is_true(model.eval(v))) for v in x]
            assert valid(h,bits)
            for witness in (bits,[1-b for b in bits]):
                assert valid(g,call({'source':source,'target_solution':witness},True));recovered+=1
        s.push();s.add(x[0]==x[6]);same=s.check();assert same==z3.unsat;s.pop()
        projection=[x[13+8*i] for i in g]
        bad=[z3.And(projection),z3.And([z3.Not(v) for v in projection])]
        for b in g:
            bad.extend(z3.And(projection[a]!=projection[b],projection[c]!=projection[b]) for a,c in itertools.combinations(g[b],2))
        s.push();s.add(z3.Or(bad));invalid=s.check();assert invalid==z3.unsat;s.pop()
        result['full_outputs'].append({'name':name,'vertices':len(h),'edges':h.number_of_edges(),'eccentricity_zero':max(distances.values()),'decision':str(decision),'recoveries':recovered,'nonconstant_same_reservoir_query':str(same),'invalid_projection_query':str(invalid)})
        print(name,decision,flush=True)
    for name,data in [('radius_five_path',{'n':11,'edges':[[i,i+1] for i in range(10)]}),('boolean_size',{'n':True,'edges':[]}),('duplicate_edge',{'n':2,'edges':[[0,1],[0,1]]}),('odd_cycle',{'n':3,'edges':[[0,1],[1,2],[0,2]]}),('disconnected',{'n':3,'edges':[[0,1]]}),('huge_size',{'n':10**100,'edges':[]})]:
        assert call(data)=={};result['invalid_inputs'].append(name)
    singleton=call({'n':1,'edges':[]});s,x=formula(nx.Graph(singleton['edges']));assert s.check()==z3.unsat
    result['singleton_no']=True
    (HERE/'checks.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
