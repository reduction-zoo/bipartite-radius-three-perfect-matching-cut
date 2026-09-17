from itertools import product
from pathlib import Path
import json
import networkx as nx
cube=nx.Graph([(v,v^(1<<j)) for v in range(8) for j in range(3)])
side=[1,2,4,7]; allowed={c for c in product((0,1),repeat=3) if len(set(c))==2}
records=[]
for mask in range(1,16):
    g=cube.copy();g.add_edge(8,9);g.add_edges_from((8,v) for i,v in enumerate(side) if mask>>i&1)
    witnesses=[c for c in product((0,1),repeat=10) if all(sum(c[v]!=c[w] for w in g[v])==1 for v in g)]
    relation={tuple(c[v] for v in [1,2,4]) for c in witnesses}
    records.append(dict(mask=mask, attachments=[v for i,v in enumerate(side) if mask>>i&1],eccentricity=nx.eccentricity(g,8),relation=sorted(relation),full_nae=relation==allowed))
    assert nx.eccentricity(g,8)>3 or relation != allowed
Path(__file__).with_name('result.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records))
print('PASS: no fixed attachment in the declared family is a full NAE interface at eccentricity <= 3')
