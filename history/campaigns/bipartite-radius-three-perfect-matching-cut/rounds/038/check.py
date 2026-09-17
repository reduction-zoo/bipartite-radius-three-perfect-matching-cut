from itertools import product
from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,target_valid,solve
base=next(r for r in json.loads((HERE.parent/'028/result.json').read_text()) if r['variables']==3 and r['occurrences']==1)
g=nx.Graph();g.add_nodes_from(range(base['vertices']));g.add_edges_from(base['edges']);side=nx.bipartite.color(g)
ports=[p for p,q in base['ports']];n=len(g)
e={}
for u in g:
    for v in g:
        if u<v and side[u]!=side[v]:e[u,v]=z3.BoolVal(True) if g.has_edge(u,v) else z3.Bool(f'e{u}_{v}')
def legal(c):
    return z3.And([z3.Sum([z3.If(z3.And(on,c[a]!=c[b]),1,0) for (a,b),on in e.items() if v in (a,b)])==1 for v in g])
s=z3.Solver();allowed={b for b in product((0,1),repeat=3) if len(set(b))==2}
for i,bits in enumerate(sorted(allowed)):
    c=[z3.Bool(f'c{i}_{v}') for v in g];s.add(c[0]==False,*[c[p]==bool(bit) for p,bit in zip(ports,bits)],legal(c))
result=dict(queries=0,candidates=[],counterexamples=[],ports=ports,base=base)
for attempt in range(8):
    status=s.check();result['queries']+=1
    if status==z3.unsat:result['status']='unsat';break
    if status!=z3.sat:raise RuntimeError(s.reason_unknown())
    model=s.model();h=nx.Graph();h.add_nodes_from(g);h.add_edges_from(p for p,on in e.items() if z3.is_true(model.eval(on)))
    assert nx.is_connected(h) and nx.is_bipartite(h) and nx.eccentricity(h,0)<=3
    result['candidates'].append(sorted(h.edges()))
    oracle,c=target_solver(h);oracle.add(c[0]==False,c[ports[0]]==c[ports[1]],c[ports[1]]==c[ports[2]])
    bad=solve(oracle,c);result['queries']+=1
    if bad is None:result['status']='exact-interface';break
    assert target_valid(h,bad);result['counterexamples'].append(bad)
    s.add(z3.Not(legal([z3.BoolVal(bool(v)) for v in bad])))
else:result['status']='candidate-limit'
(HERE/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],queries=result['queries'],candidates=len(result['candidates']))))
