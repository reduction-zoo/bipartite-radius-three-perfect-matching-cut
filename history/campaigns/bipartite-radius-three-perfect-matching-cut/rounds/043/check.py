from pathlib import Path
from itertools import product
import json,sys
import networkx as nx
import z3
H=Path(__file__).resolve().parent
sys.path.insert(0,str(H.parent.parent/'work'))
from check import target_solver,target_valid,solve
EDGES=json.loads((H.parent/'041/result.json').read_text())[0]['edges']
def construct(n):
    g=nx.Graph([(0,1)]);blocks=[]
    for i in range(n):
        mapping={0:0,5:1};mapping.update({v:2+8*i+j for j,v in enumerate([1,2,3,4,6,7,8,9])})
        g.add_edges_from((mapping[a],mapping[b]) for a,b in EDGES)
        blocks.append(dict(low=[mapping[v] for v in [2,3,4]],high=[mapping[v] for v in [6,7,8]]))
    return g,blocks
if __name__=='__main__':
    records=[];queries=0
    for n in [1,2,3]:
        g,blocks=construct(n);assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
        s,c=target_solver(g);s.add(z3.Not(c[0]))
        for choices in product(range(3),repeat=n):
            s.push();s.add([c[b['low'][i]] for b,i in zip(blocks,choices)])
            y=solve(s,c);queries+=1;assert y is not None and target_valid(g,y);s.pop()
        s.add(z3.Or(z3.Not(c[1]),*[z3.Sum([z3.If(c[v],1,0) for v in b['low']])!=1 for b in blocks],*[c[a]==c[b] for block in blocks for a,b in zip(block['low'],block['high'])]))
        assert solve(s,c) is None;queries+=1
        records.append(dict(n=n,vertices=len(g),edges=sorted(g.edges()),blocks=blocks))
    (H/'result.json').write_text(json.dumps(records,indent=2)+'\n');print(dict(graphs=3,queries=queries))
