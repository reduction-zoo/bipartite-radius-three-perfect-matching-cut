from itertools import product
from pathlib import Path
import json
import networkx as nx
edges=[(0,1),(0,2),(0,4),(2,3),(1,5),(5,10),(5,11),(6,2),(6,4),(6,10),(6,11),(4,7),(4,8),(9,7),(9,8),(10,7),(11,8)]
g=nx.Graph(edges);assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
witnesses=[c for c in product((0,1),repeat=12) if all(sum(c[v]!=c[w] for w in g[v])==1 for v in g)]
normalized=[c for c in witnesses if c[0]==0]
assert {(c[10],c[11]) for c in normalized}=={(0,1),(1,0)}
assert all(c[1]==1 and c[9]==1 and c[6]==0 and c[7]==c[10] and c[8]==c[11] for c in normalized)
Path(__file__).with_name('result.json').write_text(json.dumps(dict(edges=edges,witnesses=witnesses,radius=nx.radius(g)),indent=2)+'\n')
print(json.dumps(dict(colorings=4096,witnesses=len(witnesses),normalized=len(normalized),radius=nx.radius(g))))
