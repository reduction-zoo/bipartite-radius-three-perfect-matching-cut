from itertools import product
from pathlib import Path
import json
import networkx as nx
left=[0,2];right=[1,3,4]
g=nx.Graph([(u,v) for u in left for v in right]+[(2,5),(3,6),(4,7)])
valid=[];loose=[]
for c in product((0,1),repeat=8):
    counts=[sum(c[v]!=c[w] for w in g[v]) for v in range(8)]
    if all(counts[v]==1 for v in range(2,8)) and counts[0]<=1 and counts[1]<=1:
        loose.append(c)
        assert len({c[v] for v in range(5)})==1
    if counts[:2]==[0,0] and counts[2:]==[1]*6: valid.append(c)
assert {c[:2] for c in valid}=={(0,0),(1,1)}
Path(__file__).with_name('result.json').write_text(json.dumps(dict(edges=sorted(g.edges()),terminals=[0,1],witnesses=valid,loose_witnesses=loose),indent=2)+'\n')
print(json.dumps(dict(colorings=256,exact_witnesses=len(valid),at_most_one_terminal_witnesses=len(loose),relation=sorted({c[:2] for c in valid}))))
print('PASS: equality with zero terminal crossing budgets')
