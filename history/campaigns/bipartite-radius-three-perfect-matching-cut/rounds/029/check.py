from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import solve
records=json.loads((HERE.parent/'028/result.json').read_text());results=[]
for r in records:
    g=nx.Graph();g.add_nodes_from(range(r['vertices']));g.add_edges_from(r['edges'])
    terminals={v for local in r['copies'] for pair in local for v in pair}
    c=[z3.Bool(f'c{v}') for v in g];s=z3.Solver();counts=[]
    for v in g:
        k=z3.Sum([z3.If(c[v]!=c[w],1,0) for w in g[v]]);counts.append(k);s.add(k<=1 if v in terminals else k==1)
    s.add(c[0]==False,z3.Or(c[1]==False,*[counts[v]==0 for v in terminals],*[c[p]==c[q] for p,q in r['ports']],*[z3.Or(c[v]!=c[p],c[w]!=c[q]) for (p,q),local in zip(r['ports'],r['copies']) for v,w in local]))
    bad=solve(s,c);results.append(dict(variables=r['variables'],occurrences=r['occurrences'],bad=bad))
    assert bad is None
(HERE/'result.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS: nine relaxed-boundary queries UNSAT; all occurrence ports remain saturated and consistent')
