from pathlib import Path
from itertools import product
import importlib.util,json,sys
import networkx as nx
import z3
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent.parent/'work'))
from check import target_solver,target_valid,solve
spec=importlib.util.spec_from_file_location('wire',H.parent/'028/check.py');wire=importlib.util.module_from_spec(spec);spec.loader.exec_module(wire)
spec=importlib.util.spec_from_file_location('selector',H.parent/'043/check.py');selector=importlib.util.module_from_spec(spec);spec.loader.exec_module(selector)
def construct(n,clauses):
    g,ports,copies=wire.construct(n,1)
    for clause in clauses:
        sub,blocks=selector.construct(1);mapping={0:0,1:1};mapping.update({v:len(g)+j for j,v in enumerate(range(2,len(sub)))})
        g.add_edges_from((mapping[a],mapping[b]) for a,b in sub.edges())
        for high,(v,positive) in zip(blocks[0]['high'],clause):g.add_edge(mapping[high],copies[v][0][1 if positive else 0])
    return g,ports
if __name__=='__main__':
    records=[]
    for signs in [(True,True,True),(True,False,True)]:
        clause=list(zip(range(3),signs));g,ports=construct(3,[clause]);assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
        for bits in product((0,1),repeat=3):
            s,c=target_solver(g);s.add(z3.Not(c[0]),*[c[p]==bool(b) for (p,r),b in zip(ports,bits)])
            y=solve(s,c);expected=sum(b if positive else 1-b for b,positive in zip(bits,signs))==1
            records.append(dict(signs=signs,bits=bits,expected=expected,witness=y));assert (y is not None)==expected
            if y is not None:assert target_valid(g,y)
    (H/'result.json').write_text(json.dumps(records,indent=2)+'\n');print('PASS: 16 truth-table queries; signed exact-one relation and radius three')
