from pathlib import Path
import json
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
records=[]
for k in [5,6,7,8]:
    s=z3.Solver(); e={(a,b):z3.Bool(f'e{a}_{b}') for a in range(k) for b in range(k,2*k)}
    s.add(e[0,k])
    for a in range(1,k):s.add(z3.Or([z3.And(e[0,b],e[a,b]) for b in range(k,2*k)]))
    for b in range(k,2*k):s.add(z3.Or([e[a,b] for a in range(k)]))
    cs=[]
    for i in range(3):
        c=[z3.Bool(f'c{i}_{v}') for v in range(2*k)];cs.append(c)
        s.add(z3.Not(c[0]),c[k],e[1,k+1+i],c[1]!=c[k+1+i])
        for v in range(2*k):
            s.add(z3.PbEq([(z3.And(edge,c[a]!=c[b]),1) for (a,b),edge in e.items() if v in (a,b)],1))
    result=s.check();assert result!=z3.unknown
    record=dict(k=k,result=str(result));records.append(record)
    if result==z3.sat:
        m=s.model();edges=[edge for edge,x in e.items() if z3.is_true(m.eval(x))]
        cuts=[[int(z3.is_true(m.eval(x))) for x in c] for c in cs]
        g=nx.Graph();g.add_nodes_from(range(2*k));g.add_edges_from(edges)
        assert nx.is_bipartite(g) and nx.is_connected(g) and nx.eccentricity(g,0)<=3
        assert all(all(sum(c[v]!=c[w] for w in g[v])==1 for v in g) for c in cuts)
        record.update(edges=edges,cuts=cuts,radius=nx.radius(g));break
    print(json.dumps(record),flush=True)
(HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records),flush=True)
