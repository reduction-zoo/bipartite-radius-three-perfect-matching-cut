from pathlib import Path
import sys,json
import networkx as nx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,target_valid,solve

def residual(g,u,h):
    distance=nx.single_source_shortest_path_length(g,u)
    assert max(distance.values())<=3 and g.degree(h)==1
    k=[v for v in g if distance[v]==1 and v!=h]
    a=[v for v in g if distance[v]==2];b=[v for v in g if distance[v]==3]
    c=[0]*len(g);c[h]=1
    for v in b:c[v]=1
    demands={v:1 for v in k+b};free=[]
    for v in a:
        nk=[w for w in g[v] if w in k];nb=[w for w in g[v] if w in b]
        can_one=len(nk)==1;can_zero=len(nb)==1
        if not can_one and not can_zero:return None
        if can_one and can_zero:free.append((v,nk[0],nb[0]));continue
        c[v]=int(can_one)
        demands[nk[0] if can_one else nb[0]]-=1
    if min(demands.values(),default=0)<0 or sum(demands.values())!=len(free):return None
    flow=nx.DiGraph();flow.add_nodes_from(['s','t'])
    for v,x,y in free:
        flow.add_edge('s',('v',v),capacity=1)
        for w in [x,y]:flow.add_edge(('v',v),('d',w),capacity=1)
    for w,d in demands.items():flow.add_edge(('d',w),'t',capacity=d)
    value,assignment=nx.maximum_flow(flow,'s','t')
    if value!=len(free):return None
    for v,x,y in free:c[v]=int(assignment[('v',v)][('d',x)]==1)
    return c

if __name__=='__main__':
    records=[]
    for g in nx.graph_atlas_g():
        if len(g)<2 or not nx.is_connected(g) or not nx.is_bipartite(g):continue
        for u in g:
            if nx.eccentricity(g,u)>3:continue
            for h in g[u]:
                if g.degree(h)!=1:continue
                got=residual(g,u,h);s,c=target_solver(g);s.add(c[u]==False,c[h]==True);expected=solve(s,c)
                assert (got is not None)==(expected is not None)
                if got is not None:assert target_valid(g,got)
                records.append(dict(n=len(g),edges=sorted(g.edges()),u=u,h=h,witness=got))
    (HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(dict(center_cases=len(records),solver_queries=len(records),yes=sum(r['witness'] is not None for r in records))))
    print('PASS: restricted residual flow and witness recovery')
