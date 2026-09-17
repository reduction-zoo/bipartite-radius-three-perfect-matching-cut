from itertools import combinations,product
from pathlib import Path
import random,json
import networkx as nx
rng=random.Random(3401);records=[];eligible=0;checks=0
for k in [5,6]:
    edges=[(u,v) for u in range(k) for v in range(k,2*k)];patterns=[]
    for zeros in combinations([v for v in range(1,2*k) if v!=k],k-1):
        c=[1]*(2*k);c[0]=0
        for v in zeros:c[v]=0
        cross=[sum(1<<i for i,(a,b) in enumerate(edges) if v in (a,b) and c[a]!=c[b]) for v in range(2*k)]
        patterns.append((c,cross))
    for density in [.2,.3,.4,.5,.6]:
        for sample in range(500):
            mask=1|sum((1<<i) for i in range(1,len(edges)) if rng.random()<density)
            g=nx.Graph();g.add_nodes_from(range(2*k));g.add_edges_from(e for i,e in enumerate(edges) if mask>>i&1)
            if not nx.is_connected(g) or nx.eccentricity(g,0)>3:continue
            eligible+=1;checks+=len(patterns)
            witnesses=[c for c,cross in patterns if all((mask&cross[v]).bit_count()==1 for v in range(2*k))]
            if witnesses:
                diversity=max(len({w for c in witnesses for w in g[v] if c[v]!=c[w]}) for v in g)
                records.append(dict(n=2*k,density=density,sample=sample,edges=sorted(g.edges()),witnesses=witnesses,diversity=diversity))
g=nx.Graph([(v,v^(1<<j)) for v in range(8) for j in range(3)]+[(8,1),(8,9)])
control=[c for c in product((0,1),repeat=10) if c[8]==0 and c[9]==1 and all(sum(c[v]!=c[w] for w in g[v])==1 for v in g)]
assert len(control)==3 and nx.eccentricity(g,8)==4
result=dict(generated=5000,eligible=eligible,coloring_checks=checks,records=records,control=dict(edges=sorted(g.edges()),witnesses=control))
Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(generated=5000,eligible=eligible,coloring_checks=checks,feasible=len(records),max_mates=max((r['diversity'] for r in records),default=0),coloring_counts=sorted({len(r['witnesses']) for r in records}),control_witnesses=len(control))))
