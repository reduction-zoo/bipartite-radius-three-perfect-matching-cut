from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,target_valid,solve

def construct(g):
    n=len(g);h=nx.Graph();h.add_nodes_from(range(8*n))
    h.add_edges_from((2*u+s,2*v+1-s) for u,v in g.edges() for s in (0,1))
    for v in g:
        a,b,c,p,q,r=range(2*n+6*v,2*n+6*v+6)
        h.add_edges_from((x,y) for x in [2*v,a] for y in [2*v+1,b,c])
        h.add_edges_from([(a,p),(b,q),(c,r)])
    return h

if __name__=='__main__':
    records=[]
    for g in nx.graph_atlas_g():
        if not 2<=len(g)<=6 or not nx.is_connected(g):continue
        h=construct(g);assert nx.is_bipartite(h) and nx.is_connected(h)
        assert len(h)==8*len(g) and h.number_of_edges()==2*g.number_of_edges()+9*len(g)
        a=solve(*target_solver(g));solver,colors=target_solver(h);b=solve(solver,colors)
        assert (a is not None)==(b is not None)
        if b is not None: assert target_valid(g,[b[2*v] for v in g])
        solver.add(z3.Or([z3.Sum([z3.If(colors[2*v]!=colors[2*w],1,0) for w in g[v]]) != 1 for v in g]))
        assert solve(solver,colors) is None
        records.append(dict(n=len(g),edges=sorted(g.edges()),source_radius=nx.radius(g),target_radius=nx.radius(h),yes=a is not None))
    (HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(dict(graphs=len(records),solver_queries=3*len(records),radius_failures=sum(r['target_radius']>3 for r in records),maximum_target_radius=max(r['target_radius'] for r in records),first_radius_failure=next((r for r in records if r['target_radius']>3),None))))
    print('PASS: decisions and universal finite-instance recovery; radius contract fails')
