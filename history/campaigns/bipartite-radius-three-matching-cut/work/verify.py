import argparse
import itertools
import json
from pathlib import Path
import subprocess
import sys
import networkx as nx
import z3


def call(path,data,extract=False):
    return json.loads(subprocess.run([sys.executable,str(path)]+(['--extract'] if extract else []),input=json.dumps(data),text=True,capture_output=True,check=True).stdout)


def valid(source,x):
    if type(x)is not list or len(x)!=source['n'] or any(type(b)is not int or b not in (0,1) for b in x) or len(set(x))!=2:return False
    cross=[0]*source['n']
    for u,v in source['edges']:
        if x[u]!=x[v]:cross[u]+=1;cross[v]+=1
    return max(cross)<=1


def models(target):
    assert type(target)is dict and set(target)=={'n','edges'}
    n,edges=target['n'],target['edges'];assert type(n)is int and n>=1
    assert all(type(e)is list and len(e)==2 and all(type(v)is int for v in e) and 0<=e[0]<e[1]<n for e in edges)
    assert len(set(map(tuple,edges)))==len(edges)
    g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from(edges)
    assert nx.is_connected(g) and nx.is_bipartite(g)
    assert any(len(nx.single_source_shortest_path_length(g,v,cutoff=3))==n for v in g)
    x=[z3.Bool(f'v{i}') for i in range(n)];s=z3.Solver();s.add(z3.Or(x),z3.Or([z3.Not(v) for v in x]))
    for i in g:s.add(z3.PbLe([(x[i]!=x[j],1) for j in g[i]],1))
    out=[]
    for _ in range(2):
        status=s.check()
        if status==z3.unsat:break
        assert status==z3.sat,status
        y=[int(z3.is_true(s.model().eval(v))) for v in x]
        assert valid(target,y)
        out.append(y);s.add(z3.Or([v!=bool(b) for v,b in zip(x,y)]))
    return out


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--candidate',required=True,type=Path);args=p.parse_args()
    graphs=[g for g in nx.graph_atlas_g() if 1<=len(g)<=5 and nx.is_connected(g) and nx.is_bipartite(g)]
    graphs += [nx.cycle_graph(6),nx.complete_bipartite_graph(3,3),nx.complete_bipartite_graph(2,4),nx.convert_node_labels_to_integers(nx.grid_2d_graph(2,3))]
    graphs.append(nx.path_graph(9))
    g=nx.path_graph(8);g.add_edge(1,8);graphs.append(g)
    g=nx.path_graph(9);g.add_edge(1,9);graphs.append(g)
    records=[]
    for g in graphs:
        assert nx.radius(g)<=4
        source={'n':len(g),'edges':[sorted(e) for e in g.edges()]}
        yes=any(valid(source,list(x)) for x in itertools.product((0,1),repeat=len(g)))
        target=call(args.candidate,source);ys=models(target)
        if bool(ys)!=yes:
            Path(__file__).with_name('failure.json').write_text(json.dumps({'source':source,'target':target,'yes':yes,'witnesses':ys}));raise AssertionError('decision mismatch')
        recoveries=0
        for y in ys:
            for coloring in (y,[1-b for b in y]):
                recovered=call(args.candidate,{'source':source,'target_solution':coloring},True)
                if not valid(source,recovered):
                    Path(__file__).with_name('failure.json').write_text(json.dumps({'source':source,'target':target,'witness':coloring,'recovered':recovered}));raise AssertionError('recovery mismatch')
                recoveries+=1
        records.append({'source':source,'yes':yes,'target_vertices':target['n'],'target_edges':len(target['edges']),'solver_witnesses':len(ys),'recoveries':recoveries})
    print(json.dumps({'instances':len(records),'yes':sum(r['yes'] for r in records),'recoveries':sum(r['recoveries'] for r in records),'records':records},indent=2))
