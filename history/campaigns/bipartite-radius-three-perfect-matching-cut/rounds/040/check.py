from itertools import combinations
from pathlib import Path
import json,random
import networkx as nx
rng=random.Random(4001);records=[];checks=0;generated=0;connected=0
for k in [6,7,8]:
    edges=[(u,v) for u in range(k) for v in range(k,2*k)];patterns=[]
    for zeros in combinations([v for v in range(1,2*k) if v!=k],k-1):
        c=[1]*(2*k);c[0]=0
        for v in zeros:c[v]=0
        cross=[sum(1<<i for i,(a,b) in enumerate(edges) if v in (a,b) and c[a]!=c[b]) for v in range(2*k)]
        patterns.append((c,cross))
    for density in [.25,.5,.75,1.]:
        for sample in range(50):
            planted=list(rng.choice(patterns)[0]);matching=[(0,k)]
            for bit in [0,1]:
                left=[v for v in range(k) if planted[v]==bit and v!=0]
                right=[v for v in range(k,2*k) if planted[v]!=bit and v!=k]
                rng.shuffle(right);assert len(left)==len(right);matching+=list(zip(left,right))
            g=nx.Graph();g.add_nodes_from(range(2*k));g.add_edges_from(matching)
            g.add_edges_from((u,v) for u,v in edges if planted[u]==planted[v] and rng.random()<density)
            assert all(sum(planted[v]!=planted[w] for w in g[v])==1 for v in g);generated+=1
            if not nx.is_connected(g):continue
            connected+=1
            if nx.eccentricity(g,0)>3:continue
            mask=sum(1<<i for i,e in enumerate(edges) if g.has_edge(*e));checks+=len(patterns)
            witnesses=[c for c,cross in patterns if all((mask&cross[v]).bit_count()==1 for v in range(2*k))]
            diversity=max(len({w for c in witnesses for w in g[v] if c[v]!=c[w]}) for v in g)
            records.append(dict(n=2*k,density=density,sample=sample,edges=sorted(g.edges()),planted=planted,witnesses=witnesses,diversity=diversity))
result=dict(generated=generated,connected=connected,coloring_checks=checks,records=records)
Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(generated=generated,connected=connected,eligible=len(records),coloring_checks=checks,max_mates=max((r['diversity'] for r in records),default=0),coloring_counts=sorted({len(r['witnesses']) for r in records}))))
