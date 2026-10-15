from itertools import combinations
from pathlib import Path
import json,sys
import z3
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import source_solver,source_valid,solve

def forward(source):
    n=source['n'];clauses=[]
    for clause in source['clauses']:
        for positive in [True,False]:
            selectors=list(range(n,n+3));slack=list(range(n+3,n+6));n+=6
            clauses.append([(v,True) for v in selectors])
            clauses.extend([[(s,True),(v,not positive),(t,True)] for s,v,t in zip(selectors,clause,slack)])
    return dict(n=n,clauses=clauses)

def recover(source,witness):return witness[:source['n']]

triples=list(combinations(range(4),3));sources=[dict(n=4,variables=list(range(4)),clauses=[list(c) for i,c in enumerate(triples) if mask>>i&1]) for mask in range(16)]
sources+=[dict(n=0,variables=[],clauses=[]),dict(n=7,variables=list(range(7)),clauses=[[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]])]
records=[]
for source in sources:
    target=forward(source);x=solve(*source_solver(source));s=z3.Solver();c=[z3.Bool(f'e{i}') for i in range(target['n'])]
    for clause in target['clauses']:
        s.add(z3.Sum([z3.If(c[v] if positive else z3.Not(c[v]),1,0) for v,positive in clause])==1)
    y=solve(s,c);assert (x is not None)==(y is not None)
    if y is not None:assert source_valid(source,recover(source,y))
    s.add(z3.Or([z3.And(c[a]==c[b],c[b]==c[d]) for a,b,d in source['clauses']]))
    assert solve(s,c) is None
    records.append(dict(source=source,target=target,source_yes=x is not None,target_witness=y))
(HERE/'result.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(dict(pairs=len(records),queries=3*len(records),yes=sum(r['source_yes'] for r in records))))
print('PASS: intermediate exact-one encoding and finite-instance universal recovery')
