import argparse
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import networkx as nx
import z3


def graph(data, target=False):
    assert type(data) is dict and set(data)=={'n','edges'}
    n,edges=data['n'],data['edges']
    assert type(n) is int and n>=1 and type(edges) is list
    assert all(type(e) is list and len(e)==2 and all(type(v) is int for v in e) and 0<=e[0]<e[1]<n for e in edges)
    assert len(set(map(tuple,edges)))==len(edges)
    g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from(edges)
    assert nx.is_connected(g) and nx.is_bipartite(g)
    assert any(len(nx.single_source_shortest_path_length(g,v,cutoff=3 if target else 4))==n for v in g)
    return g


def valid(g, matching):
    if type(matching) is not list or any(type(e) is not list or len(e)!=2 or any(type(v) is not int for v in e) for e in matching):return False
    if any(not (u<v and g.has_edge(u,v)) for u,v in matching):return False
    vertices=[v for e in matching for v in e]
    if len(vertices)!=len(g) or set(vertices)!=set(g):return False
    h=g.copy();h.remove_edges_from(matching)
    return not nx.is_connected(h)


def solve(data,target=False,limit=1):
    g=graph(data,target);edges=data['edges']
    x=[z3.Bool(f'x{i}') for i in g];chosen=[z3.Bool(f'm{i}') for i in range(len(edges))]
    s=z3.Solver();s.add(z3.Not(x[0]),z3.Or(x))
    incident=[[] for _ in g]
    for bit,(u,v) in zip(chosen,edges):
        incident[u].append((bit,1));incident[v].append((bit,1));s.add(z3.Implies(x[u]!=x[v],bit))
    for row in incident:s.add(z3.PbEq(row,1) if row else z3.BoolVal(False))
    result=[]
    for _ in range(limit):
        status=s.check()
        if status==z3.unsat:break
        assert status==z3.sat,status
        m=s.model();values=[z3.is_true(m.eval(b,model_completion=True)) for b in chosen]
        matching=[e for e,b in zip(edges,values) if b];assert valid(g,matching)
        result.append(matching);s.add(z3.Or([bit!=value for bit,value in zip(chosen,values)]))
    return result


def call(path,payload,extract=False):
    p=subprocess.run([sys.executable,str(path)]+(['--extract'] if extract else []),input=json.dumps(payload),text=True,capture_output=True,check=True)
    return json.loads(p.stdout)


def check(path,cases):
    recoveries=0;largest=0
    for case in cases:
        source=case['source'];target=call(path,source);witnesses=solve(target,True,2)
        assert bool(witnesses)==case['yes'],case
        largest=max(largest,target['n'])
        for witness in witnesses:
            for supplied in (witness,list(reversed(witness))):
                recovered=call(path,{'source':source,'target_solution':supplied},True)
                assert valid(graph(source),recovered),(source,supplied,recovered)
                recoveries+=1
    return {'cases':len(cases),'recoveries':recoveries,'largest_output_order':largest}


def self_test(cases):
    counts=[0,0];witnesses=0
    for g in nx.graph_atlas_g():
        if not 1<=len(g)<=6 or not nx.is_connected(g) or not nx.is_bipartite(g):continue
        data={'n':len(g),'edges':[sorted(e) for e in g.edges()]}
        expected={tuple(sorted(es)) for es in itertools.combinations(map(tuple,data['edges']),len(g)//2) if valid(g,list(map(list,es)))}
        for target in (False,True):
            actual={tuple(sorted(map(tuple,y))) for y in solve(data,target,len(expected)+1)}
            assert actual==expected,(data,expected,actual)
            counts[target]+=1
        witnesses+=len(expected)
        assert not valid(g,[]) and not valid(g,[[0,0]])
    for c in cases:assert bool(solve(c['source']))==c['yes'],c
    yes={'n':2,'edges':[[0,1]]}
    with tempfile.TemporaryDirectory() as directory:
        p=Path(directory)/'bad.py'
        fixtures=[('print("{}")',cases[:1]),('print('+repr(json.dumps(yes))+')',[c for c in cases if not c['yes']][:1]),('import sys; print("[]" if "--extract" in sys.argv else '+repr(json.dumps(yes))+')',[c for c in cases if c['yes']][:1])]
        for script,subset in fixtures:
            p.write_text(script)
            try:check(p,subset)
            except AssertionError:pass
            else:raise AssertionError('Accepted incorrect fixture')
    print(json.dumps({'solver':z3.get_version_string(),'source_graphs':counts[0],'target_graphs':counts[1],'exhaustive_witnesses':witnesses,'stored_cases':len(cases),'rejected_fixtures':len(fixtures)}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--self-test',action='store_true');p.add_argument('--candidate',type=Path);a=p.parse_args()
    cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    if a.self_test:self_test(cases)
    elif a.candidate:print(json.dumps(check(a.candidate.resolve(),cases)))
    else:p.error('Select --self-test or --candidate')
