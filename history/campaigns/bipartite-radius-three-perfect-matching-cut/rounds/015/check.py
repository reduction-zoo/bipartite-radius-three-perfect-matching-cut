from itertools import combinations
from pathlib import Path
import json, sys
import networkx as nx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import source_solver,source_valid,target_solver,target_valid,solve
previous=json.loads((HERE.parent/'014/result.json').read_text())['successes']
formulas=[(3,[(0,1,2)]),(5,[(0,1,2),(1,2,3),(2,3,4)]),(4,list(combinations(range(4),3)))]
records=[]
for interface in previous:
    for n,clauses in formulas:
        source=dict(n=n,variables=list(range(n)),clauses=[list(c) for c in clauses])
        g=nx.Graph();g.add_edge(0,1)
        for j,clause in enumerate(clauses):
            mapping={v:2+8*j+v for v in range(8)};mapping.update({8:0,9:1})
            g.add_edges_from((mapping[u],mapping[v]) for u,v in interface['edges'])
            for port,variable in zip([1,2,4],clause):
                g.add_edge(mapping[port],2+8*len(clauses)+2*variable)
        variables=[2+8*len(clauses)+2*i for i in range(n)]
        g.add_edges_from((v,v+1) for v in variables)
        x=solve(*source_solver(source));y=solve(*target_solver(g))
        assert x is not None and source_valid(source,x)
        recovered=None if y is None else [y[v] for v in variables]
        if y is not None:
            assert target_valid(g,y) and source_valid(source,recovered)
        records.append(dict(interface=[interface['a'],interface['b']],source=source,source_witness=x,
                            n=len(g),edges=sorted(g.edges()),radius=nx.radius(g),bipartite=nx.is_bipartite(g),
                            target_yes=y is not None,target_witness=y,recovered=recovered))
(HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps([dict(interface=r['interface'],clauses=len(r['source']['clauses']),radius=r['radius'],target_yes=r['target_yes']) for r in records]))
print('Source/target queries: 12 each; complete reduction not obtained')
