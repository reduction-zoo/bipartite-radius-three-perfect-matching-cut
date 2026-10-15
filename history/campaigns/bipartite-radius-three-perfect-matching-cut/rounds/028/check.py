from itertools import product
from pathlib import Path
import json,sys
import networkx as nx
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_solver,target_valid,solve

def construct(n,occ):
    g=nx.Graph([(0,1),(0,2),(2,3)]);ports=[];copies=[];next_id=4
    for i in range(n):
        f,p,r,z=range(next_id,next_id+4);next_id+=4;ports.append((p,r));local=[]
        g.add_edges_from([(1,f),(f,p),(f,r),(z,2),(z,p),(z,r)])
        for j in range(occ):
            a,v,w,q=range(next_id,next_id+4);next_id+=4;local.append((v,w))
            g.add_edges_from([(0,a),(a,v),(a,w),(q,v),(q,w),(p,v),(r,w)])
            if j==0:g.add_edge(z,a)
        copies.append(local)
    return g,ports,copies

if __name__=='__main__':
    records=[];queries=0
    for n,occ in product([1,2,3],[1,2,4]):
        g,ports,copies=construct(n,occ)
        assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
        solver,c=target_solver(g);solver.add(c[0]==False)
        for assignment in product((0,1),repeat=n):
            solver.push();solver.add([c[p]==bool(v) for (p,r),v in zip(ports,assignment)])
            y=solve(solver,c);queries+=1;assert y is not None and target_valid(g,y);solver.pop()
        solver.add(z3.Or(c[1]==False,*[c[p]==c[r] for p,r in ports],*[z3.Or(c[v]!=c[p],c[w]!=c[r]) for (p,r),local in zip(ports,copies) for v,w in local]))
        assert solve(solver,c) is None;queries+=1
        records.append(dict(variables=n,occurrences=occ,vertices=len(g),edges=sorted(g.edges()),ports=ports,copies=copies,radius=nx.radius(g)))
    (HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(dict(constructions=len(records),queries=queries,maximum_vertices=max(r['vertices'] for r in records))))
    print('PASS: all intended wire assignments and finite-instance universal consistency')
