from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,target_valid,solve
r=next(r for r in json.loads((HERE.parent/'028/result.json').read_text()) if r['variables']==3 and r['occurrences']==1)
g=nx.Graph();g.add_nodes_from(range(r['vertices']));g.add_edges_from(r['edges']);s,c=target_solver(g);s.add(c[0]==False)
witnesses=[];queries=0
while True:
    y=solve(s,c);queries+=1
    if y is None:break
    witnesses.append(y);s.add(z3.Or([v!=bool(b) for v,b in zip(c,y)]))
assert len(witnesses)==8
ports=[p for p,q in r['ports']];good=[w for w in witnesses if len({w[p] for p in ports})==2]
side=nx.bipartite.color(g);added=[(u,v) for u in g for v in g if u<v and side[u]!=side[v] and not g.has_edge(u,v) and all(w[u]==w[v] for w in good)]
h=g.copy();h.add_edges_from(added)
assert all(target_valid(h,w) for w in witnesses)
(HERE/'result.json').write_text(json.dumps(dict(base=r,added_edges=added,witnesses=witnesses),indent=2)+'\n')
print(json.dumps(dict(queries=queries,witnesses=len(witnesses),added_edges=len(added),all_equal_survivors=2,radius=nx.radius(h))))
