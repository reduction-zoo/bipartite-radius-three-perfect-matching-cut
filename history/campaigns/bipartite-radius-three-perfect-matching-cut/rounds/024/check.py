from itertools import product
from pathlib import Path
import json
import networkx as nx
import z3
n=8;term=[0,4,1,5];internal=[2,3,6,7]
edges=[(u,v) for u in range(4) for v in range(4,8)]
e={p:z3.Bool(f'e{p[0]}_{p[1]}') for p in edges};s=z3.Solver()
d=[z3.Int(f'd{v}') for v in range(n)];s.add(d[0]==0)
for v in range(1,n):
    s.add(d[v]>=1,d[v]<n,z3.Or([z3.And(present,d[w]<d[v]) for (a,b),present in e.items() for w in ([b] if v==a else [a] if v==b else [])]))
def counts(c):
    return [z3.Sum([z3.If(z3.And(present,c[a]!=c[b]),1,0) for (a,b),present in e.items() if v in (a,b)]) for v in range(n)]
for i,(x,y) in enumerate(product((0,1),repeat=2)):
    c={v:z3.Bool(f'c{i}_{v}') for v in internal};c.update({0:z3.BoolVal(bool(x)),4:z3.BoolVal(bool(x)),1:z3.BoolVal(bool(y)),5:z3.BoolVal(bool(y))})
    k=counts(c);s.add([k[v]==int(v in internal) for v in range(n)])
for bits in product((0,1),repeat=n):
    c={v:z3.BoolVal(bool(bits[v])) for v in range(n)};k=counts(c)
    valid=z3.And(*[k[v]==1 for v in internal],*[k[v]<=1 for v in term])
    desired=z3.And(bits[0]==bits[4],bits[1]==bits[5],*[k[v]==0 for v in term])
    s.add(z3.Implies(valid,desired))
status=s.check();result=dict(status=str(status),synthesis_queries=1)
if status==z3.sat:
    m=s.model();g=nx.Graph();g.add_nodes_from(range(n));g.add_edges_from(p for p in edges if z3.is_true(m.eval(e[p])))
    assert nx.is_connected(g)
    states=set()
    for bits in product((0,1),repeat=n):
        k=[sum(bits[v]!=bits[w] for w in g[v]) for v in g]
        if all(k[v]==1 for v in internal) and all(k[v]<=1 for v in term):states.add(tuple(bits[v] for v in term)+tuple(k[v] for v in term))
    assert states=={(x,x,y,y,0,0,0,0) for x,y in product((0,1),repeat=2)}
    result.update(edges=sorted(g.edges()),states=sorted(states),radius=nx.radius(g))
elif status!=z3.unsat:raise RuntimeError(s.reason_unknown())
Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
