from pathlib import Path
from itertools import product
import json
import networkx as nx
H=Path(__file__).resolve().parent
r=json.loads((H.parent/'041/result.json').read_text())[0]
g=nx.Graph(r['edges']);cuts=[list(c) for c in product((0,1),repeat=10) if all(sum(c[v]!=c[w] for w in g[v])==1 for v in g)]
normalized=[c for c in cuts if c[0]==0];fixed=[c for c in normalized if c[5]==1]
assert len(fixed)==3
assert {tuple(c[v] for v in [2,3,4]) for c in fixed}=={(1,0,0),(0,1,0),(0,0,1)}
assert all(all(c[a]!=c[b] for a,b in [(2,6),(3,7),(4,8)]) for c in fixed)
result=dict(coloring_checks=1024,cuts=cuts,fixed=fixed,other_center=[c for c in normalized if c[5]==0])
(H/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
