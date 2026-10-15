"""Recheck saved graphs and counterexamples without importing the synthesis script."""
from collections import Counter
import json
from pathlib import Path
import sys
from itertools import product
import z3

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'work'))
from check import target_domain, target_valid, target_solver, solve

summary=Counter()
for count in (1,2):
    data=json.loads((HERE/f'result-{count}.json').read_text())
    ports=list(range(8+count,14+count))
    previous=[]
    for graph,bad in zip(data['candidates'],data['counterexamples'],strict=True):
        g=target_domain(graph)
        assert bad[:2]==[0,1] and target_valid(g,bad)
        pattern=[bad[v] for v in ports]
        assert pattern.count(0)==3
        pairs_valid=all(pattern[i]!=pattern[i+1] for i in (0,2,4))
        if pairs_valid:
            assert len(set(pattern[::2]))==1
            summary['complementary_but_all_equal']+=1
        else:
            summary['invalid_complementary_pair']+=1
        for earlier in previous:
            assert not target_valid(g,earlier)
            summary['previous_counterexamples_rejected']+=1
        previous.append(bad)
        for assignment in product((0,1),repeat=3):
            if len(set(assignment))!=2:
                continue
            wanted=[v for bit in assignment for v in (bit,1-bit)]
            oracle,c=target_solver(g)
            oracle.add(c[0]==False,c[1]==True)
            oracle.add(*[c[v]==bool(bit) for v,bit in zip(ports,wanted)])
            witness=solve(oracle,c)
            assert witness is not None and target_valid(g,witness)
            summary['allowed_extensions_verified']+=1
        summary['graphs_checked']+=1
    assert len(data['candidates'])==32 and data['status']=='candidate-limit'
print(json.dumps(dict(summary),indent=2))
(HERE/'evidence-check.json').write_text(json.dumps(dict(summary),indent=2)+'\n')
