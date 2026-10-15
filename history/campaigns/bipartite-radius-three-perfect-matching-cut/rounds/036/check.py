from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,solve
edges=[(u,v) for u in range(3) for v in range(3,6)];records=[]
for mask in range(512):
    g=nx.Graph();g.add_nodes_from(range(6));g.add_edges_from(e for i,e in enumerate(edges) if mask>>i&1)
    if not nx.is_connected(g):continue
    x=[z3.Real(f'x{v}') for v in g];s=z3.Solver()
    s.add([g.degree(v)*x[v]-z3.Sum([x[w] for w in g[v]])==2*x[v] for v in g]);s.add(z3.Or([v!=0 for v in x]))
    status=s.check()
    if status not in (z3.sat,z3.unsat):raise RuntimeError(s.reason_unknown())
    relaxed=status==z3.sat;pmc=solve(*target_solver(g)) is not None
    assert not pmc or relaxed
    witness=[str(s.model().eval(v,model_completion=True)) for v in x] if relaxed else None
    records.append(dict(edges=sorted(g.edges()),relaxed=relaxed,pmc=pmc,real_witness=witness,radius=nx.radius(g)))
(HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
bad=[r for r in records if r['relaxed'] and not r['pmc']]
print(json.dumps(dict(graphs=len(records),queries=2*len(records),false_positives=len(bad),first=bad[0] if bad else None)))
