from pathlib import Path
import json,sys
import z3
import networkx as nx
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent.parent/'work'))
from check import solve
records=[]
for r in json.loads((H.parent/'043/result.json').read_text()):
    g=nx.Graph(r['edges']);c=[z3.Bool(f'c{v}') for v in range(len(g))];s=z3.Solver()
    high=[v for b in r['blocks'] for v in b['high']];relaxed={0,1,*high};counts={v:z3.Sum([z3.If(c[v]!=c[w],1,0) for w in g[v]]) for v in g}
    s.add([counts[v]<=1 if v in relaxed else counts[v]==1 for v in g]);s.add(z3.Not(c[0]))
    s.add(z3.Or(z3.Not(c[1]),*[counts[v]!=1 for v in high],*[z3.Sum([z3.If(c[v],1,0) for v in b['low']])!=1 for b in r['blocks']],*[c[a]==c[b] for block in r['blocks'] for a,b in zip(block['low'],block['high'])]))
    bad=solve(s,c);records.append(dict(n=r['n'],bad=bad));assert bad is None
(H/'result.json').write_text(json.dumps(records,indent=2)+'\n');print('PASS: three relaxed selector queries UNSAT')
