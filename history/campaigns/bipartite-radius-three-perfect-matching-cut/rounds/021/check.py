from itertools import product
from pathlib import Path
import json
import networkx as nx
edges=[(u,v) for u in range(3) for v in range(3,6)]
records=[];connected=0
for mask in range(512):
    g=nx.Graph();g.add_nodes_from(range(6));g.add_edges_from(e for i,e in enumerate(edges) if mask>>i&1)
    if not nx.is_connected(g):continue
    connected+=1;states=set();witnesses=[]
    for c in product((0,1),repeat=6):
        d=[sum(c[v]!=c[w] for w in g[v]) for v in range(6)]
        if all(d[v]==1 for v in [1,2,4,5]) and d[0]<=1 and d[3]<=1:
            states.add((c[0],c[3],d[0],d[3]));witnesses.append(c)
    if states=={(0,0,0,0),(1,1,0,0)}:
        records.append(dict(edges=sorted(g.edges()),radius=nx.radius(g),terminal_distance=nx.shortest_path_length(g,0,3),witnesses=witnesses))
Path(__file__).with_name('result.json').write_text(json.dumps(dict(connected=connected,colorings=connected*64,successes=records),indent=2)+'\n')
print(json.dumps(dict(connected=connected,colorings=connected*64,successes=len(records))))
