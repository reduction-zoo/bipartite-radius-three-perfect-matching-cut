from pathlib import Path
import json,sys
import networkx as nx
import z3
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent.parent/'work'))
from check import solve
records=[]
for r in json.loads((H.parent/'028/result.json').read_text()):
    g=nx.Graph(r['edges']);c=[z3.Bool(f'c{v}') for v in range(len(g))];s=z3.Solver()
    ports={v for local in r['copies'] for pair in local for v in pair};relaxed={0,1,*ports}
    counts={v:z3.Sum([z3.If(c[v]!=c[w],1,0) for w in g[v]]) for v in g}
    s.add([counts[v]<=1 if v in relaxed else counts[v]==1 for v in g]);s.add(z3.Not(c[0]))
    s.add(z3.Or(z3.Not(c[1]),*[counts[v]!=1 for v in ports],*[c[a]==c[b] for a,b in r['ports']],*[z3.Or(c[v]!=c[a],c[w]!=c[b]) for (a,b),local in zip(r['ports'],r['copies']) for v,w in local]))
    bad=solve(s,c);records.append(dict(n=r['variables'],occ=r['occurrences'],bad=bad));assert bad is None
(H/'result.json').write_text(json.dumps(records,indent=2)+'\n');print('PASS: nine shared-center wire queries UNSAT')
