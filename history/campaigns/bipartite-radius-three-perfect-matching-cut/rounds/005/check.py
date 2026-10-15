from itertools import product
import json
from pathlib import Path
import networkx as nx

count=0; deficits=0
for g in nx.graph_atlas_g():
    if len(g)<2 or not nx.is_connected(g) or not nx.is_bipartite(g):continue
    for u in g:
        dist=nx.single_source_shortest_path_length(g,u)
        if max(dist.values())>3:continue
        third={v for v in g if dist[v]==3}
        for c in product((0,1),repeat=len(g)):
            if c[u]!=0:continue
            crossing={v:sum(c[v]!=c[w] for w in g[v]) for v in g}
            if any(crossing[v]!=1 for v in g if v not in third):continue
            if any(crossing[v]>1 for v in third):continue
            h=next(v for v in g[u] if c[v]==1)
            near=set(g[u])-{h}
            f={v for v in g if dist[v]==2 and h in g[v] and not (set(g[v])&near)}
            assert sum(c[v]==0 and crossing[v]==1 for v in third)==len(f)
            count+=1;deficits+=any(crossing[v]==0 for v in third)
result={'partial_colorings':count,'with_zero_budget_terminal':deficits,'max_order':7}
print(json.dumps(result));Path(__file__).with_name('result.json').write_text(json.dumps(result,indent=2)+'\n')
