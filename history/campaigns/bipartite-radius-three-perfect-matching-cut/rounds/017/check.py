from pathlib import Path
import json,sys
import networkx as nx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,target_valid,solve
records=[]
for g in nx.graph_atlas_g():
    if not 2<=len(g)<=5 or not nx.is_connected(g):continue
    h=nx.Graph();h.add_nodes_from(range(2*len(g)))
    h.add_edges_from((2*u+s,2*v+1-s) for u,v in g.edges() for s in (0,1))
    a=solve(*target_solver(g));b=solve(*target_solver(h))
    if a is not None: assert b is not None
    if b is not None: assert target_valid(h,b)
    records.append(dict(n=len(g),edges=sorted(g.edges()),source_yes=a is not None,target_yes=b is not None,
                        target_witness=b,connected=nx.is_connected(h),radius=nx.radius(h) if nx.is_connected(h) else None))
(HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
bad=[r for r in records if r['source_yes']!=r['target_yes']]
print(json.dumps(dict(graphs=len(records),queries=2*len(records),decision_mismatches=len(bad),first_counterexample=bad[0] if bad else None)))
