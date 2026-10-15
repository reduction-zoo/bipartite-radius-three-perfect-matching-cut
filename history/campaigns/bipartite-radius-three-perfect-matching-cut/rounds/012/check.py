from itertools import product
import json
from pathlib import Path
import networkx as nx

cube = nx.Graph([(v, v ^ (1 << j)) for v in range(8) for j in range(3)])
side = [v for v in cube if v.bit_count() % 2]
records = []
for mask in range(16):
    g = cube.copy(); g.add_edge(8, 9)
    g.add_edges_from((8, v) for i, v in enumerate(side) if mask >> i & 1)
    if not nx.is_connected(g):
        continue
    witnesses = [c for c in product((0, 1), repeat=10)
                 if all(sum(c[v] != c[w] for w in g[v]) == 1 for v in g)]
    intact = [c for c in witnesses if all(sum(c[v] != c[w] for w in cube[v]) == 1 for v in cube)]
    if nx.eccentricity(g, 8) <= 3 and intact:
        print('COUNTEREXAMPLE', mask, list(g.edges()), intact[0])
    records.append(dict(mask=mask, center_eccentricity=nx.eccentricity(g, 8),
                        radius=nx.radius(g), witnesses=len(witnesses), intact_witnesses=len(intact)))
Path(__file__).with_name('result.json').write_text(json.dumps(records, indent=2)+'\n')
print(json.dumps(dict(graphs=len(records), colorings=len(records)*1024,
                     short_center_graphs=sum(r['center_eccentricity'] <= 3 for r in records),
                     intact_witnesses=sum(r['intact_witnesses'] for r in records))))
print('Completed enumeration; inspect records before drawing a conclusion')
