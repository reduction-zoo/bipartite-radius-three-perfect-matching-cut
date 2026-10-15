from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,solve

def construct(g,edges):
    n=len(g);h=nx.Graph();h.add_nodes_from(range(6*n))
    h.add_edges_from((2*u+s,2*v+1-s) for u,v in g.edges() for s in (0,1))
    for v in g:
        mapping={0:2*v,3:2*v+1}
        mapping.update(zip([1,2,4,5],range(2*n+4*v,2*n+4*v+4)))
        h.add_edges_from((mapping[a],mapping[b]) for a,b in edges)
    return h

if __name__=='__main__':
    interfaces=json.loads((HERE.parent/'021/result.json').read_text())['successes'];records=[]
    for i,interface in enumerate(interfaces):
        for g in nx.graph_atlas_g():
            if not 2<=len(g)<=5 or not nx.is_connected(g):continue
            h=construct(g,interface['edges']);a=solve(*target_solver(g));solver,c=target_solver(h);b=solve(solver,c)
            assert (a is not None)==(b is not None)
            solver.add(z3.Or([z3.Sum([z3.If(c[2*v]!=c[2*w],1,0) for w in g[v]])!=1 for v in g]))
            assert solve(solver,c) is None
            assert nx.is_connected(h) and nx.is_bipartite(h)
            records.append(dict(interface=i,n=len(g),edges=sorted(g.edges()),radius=nx.radius(h)))
    (HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(dict(transformations=len(records),queries=3*len(records),radius_three=sum(r['radius']<=3 for r in records),radius_range=[min(r['radius'] for r in records),max(r['radius'] for r in records)])))
