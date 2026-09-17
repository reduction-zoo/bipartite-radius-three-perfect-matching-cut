from itertools import product
from pathlib import Path
import json,sys
import networkx as nx
import z3
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'work'))
from check import target_domain,target_solver,target_valid,solve
queries=0;graphs=0;bad_checks=0
for number in [30,31]:
    for path in sorted((ROOT/'rounds'/f'{number:03}').glob('result-*.json')):
        result=json.loads(path.read_text());b,f=result['b'],result['f'];k=b+f;h=3+k
        anchors=list(range(h+1,h+1+b));ports=[0,1,2]
        for edges,bad in zip(result['candidates'],result['bad']):
            g=nx.Graph();g.add_nodes_from(range(result['vertices']));g.add_edges_from(edges)
            def oracle():
                c=[z3.Bool(f'c{v}') for v in g];s=z3.Solver()
                s.add(c[h]==True,*[c[v]==False for v in anchors])
                for v in g:s.add(z3.Sum([z3.If(c[v]!=c[w],1,0) for w in g[v]])==int(v not in ports+[h]))
                return s,c
            allowed=[bits for bits in product((0,1),repeat=3) if (len(set(bits))==2 if number==30 else sum(bits)==1)]
            assert tuple(bad) not in allowed
            for bits in allowed+[tuple(bad)]:
                s,c=oracle();s.add([c[p]==bool(bit) for p,bit in zip(ports,bits)]);y=solve(s,c);queries+=1
                assert y is not None
                assert all(sum(y[v]!=y[w] for w in g[v])==int(v not in ports+[h]) for v in g)
            graphs+=1;bad_checks+=1
result=json.loads((ROOT/'rounds/038/result.json').read_text())
for edges,bad in zip(result['candidates'],result['counterexamples']):
    g=target_domain(dict(n=result['base']['vertices'],edges=edges))
    assert target_valid(g,bad) and len({bad[p] for p in result['ports']})==1
    for bits in product((0,1),repeat=3):
        if len(set(bits))!=2:continue
        s,c=target_solver(g);s.add(c[0]==False,*[c[p]==bool(bit) for p,bit in zip(result['ports'],bits)])
        y=solve(s,c);queries+=1;assert y is not None and target_valid(g,y)
    graphs+=1;bad_checks+=1
print(json.dumps(dict(graphs=graphs,solver_queries=queries,bad_checks=bad_checks)))
print('PASS: saved positive extensions and forbidden witnesses; no independent review or UNSAT certification')
