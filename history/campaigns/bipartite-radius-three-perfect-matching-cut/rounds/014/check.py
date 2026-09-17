from itertools import product
from pathlib import Path
import json
import networkx as nx
cube=nx.Graph([(v,v^(1<<j)) for v in range(8) for j in range(3)])
odd=[1,2,4,7]; even=[0,3,5,6]
allowed={c for c in product((0,1),repeat=3) if len(set(c))==2}
records=[]; successes=[]
for a in range(1,16):
    for b in range(16):
        g=cube.copy();g.add_edge(8,9)
        g.add_edges_from((8,v) for i,v in enumerate(odd) if a>>i&1)
        g.add_edges_from((9,v) for i,v in enumerate(even) if b>>i&1)
        witnesses=[c for c in product((0,1),repeat=10) if all(sum(c[v]!=c[w] for w in g[v])==1 for v in g)]
        relation={tuple(c[v] for v in [1,2,4]) for c in witnesses}
        eccentricity=nx.eccentricity(g,8)
        record=dict(a=a,b=b,eccentricity=eccentricity,relation=sorted(relation))
        records.append(record)
        if eccentricity<=3 and relation==allowed:
            successes.append(dict(**record,edges=sorted(g.edges()),witnesses=witnesses))
Path(__file__).with_name('result.json').write_text(json.dumps(dict(graphs=len(records),colorings=len(records)*1024,records=records,successes=successes),indent=2)+'\n')
print(json.dumps(dict(graphs=len(records),colorings=len(records)*1024,successes=len(successes),successful_masks=[(s['a'],s['b']) for s in successes])))
