from itertools import combinations
from pathlib import Path
import json
import networkx as nx
edges=[(u,v) for u in range(4) for v in range(4,8)]
colorings=[]
for zero in combinations([1,2,3,5,6,7],3):
    c=[1]*8;c[0]=0
    for v in zero:c[v]=0
    cross=[sum(1<<i for i,(a,b) in enumerate(edges) if v in (a,b) and c[a]!=c[b]) for v in range(8)]
    colorings.append((c,cross))
records=[];checked=0
for mask in range(1,65536,2):
    witnesses=[c for c,cross in colorings if all((mask&cross[v]).bit_count()==1 for v in range(8))]
    if not witnesses:continue
    g=nx.Graph();g.add_nodes_from(range(8));g.add_edges_from(e for i,e in enumerate(edges) if mask>>i&1)
    if not nx.is_connected(g) or nx.eccentricity(g,0)>3:continue
    checked+=1;mates=[sorted({w for c in witnesses for w in g[v] if c[v]!=c[w]}) for v in g]
    records.append(dict(mask=mask,edges=sorted(g.edges()),witnesses=witnesses,maximum_mates=max(map(len,mates)),mates=mates))
Path(__file__).with_name('result.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(dict(edge_masks=32768,coloring_checks=32768*len(colorings),feasible_center_graphs=checked,max_mates=max(r['maximum_mates'] for r in records),coloring_counts=sorted({len(r['witnesses']) for r in records}))))
