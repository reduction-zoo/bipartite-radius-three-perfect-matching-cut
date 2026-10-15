from pathlib import Path
from itertools import product,combinations_with_replacement
import importlib.util,json,sys
import networkx as nx
import z3
H=Path(__file__).resolve().parent;sys.path.insert(0,str(H.parent.parent/'work'))
from check import target_solver,target_valid,solve
spec=importlib.util.spec_from_file_location('clause',H.parent/'046/check.py');clause=importlib.util.module_from_spec(spec);spec.loader.exec_module(clause)
choices=[list(zip(range(3),signs)) for signs in product((False,True),repeat=3)];records=[];queries=0;yes=0
for clauses in combinations_with_replacement(choices,2):
    g,ports=clause.construct(3,clauses);assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
    s,c=target_solver(g);s.add(z3.Not(c[0]));local=[]
    for bits in product((0,1),repeat=3):
        s.push();s.add([c[p]==bool(b) for (p,r),b in zip(ports,bits)]);y=solve(s,c);s.pop();queries+=1
        expected=all(sum(bits[v] if sign else 1-bits[v] for v,sign in terms)==1 for terms in clauses)
        assert (y is not None)==expected
        if y is not None:assert target_valid(g,y);yes+=1
        local.append(dict(bits=bits,yes=expected,witness=y))
    records.append(dict(clauses=clauses,assignments=local))
(H/'result.json').write_text(json.dumps(records,indent=2)+'\n');print(dict(graphs=len(records),queries=queries,yes_assignments=yes));print('PASS: interacting and repeated signed clauses')
