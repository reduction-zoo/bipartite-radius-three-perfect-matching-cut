"""Bounded counterexample-guided synthesis of complementary-pair NAE interfaces."""
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic

import networkx as nx
import z3

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent/'work'))
from check import target_domain, target_solver, target_valid, solve

ALLOWED = {bits for bits in product((0,1),repeat=3) if len(set(bits))==2}


def search(b_count, far_count, left_ports):
    start = monotonic()
    k = b_count+far_count-1
    a = list(range(1,1+k))
    b = list(range(1+k,1+k+b_count))
    far = list(range(1+k+b_count,1+2*k+1))
    n = 2+2*k
    ports = a[:left_ports]+far[:3-left_ports]
    free = [v for v in range(1,n) if v not in ports]
    fixed = [(0,v) for v in b]
    possible = [(u,v) for u in a for v in b+far]
    edge = {e:z3.Bool(f'e{e[0]}_{e[1]}') for e in possible}
    solver = z3.Solver()
    for u in a:
        solver.add(z3.Or([edge[u,v] for v in b]))
    for v in far:
        solver.add(z3.Or([edge[u,v] for u in a]))

    def legal(c):
        return z3.And([z3.Sum(
            [z3.If(c[u] != c[v],1,0) for u,v in fixed if node in (u,v)] +
            [z3.If(z3.And(present,c[u] != c[v]),1,0) for (u,v),present in edge.items() if node in (u,v)]
        ) == 1 for node in range(n)])

    for i, bits in enumerate(sorted(ALLOWED)):
        c = {0:z3.BoolVal(False)}
        c.update({v:z3.BoolVal(bool(bit)) for v,bit in zip(ports,bits)})
        c.update({v:z3.Bool(f'c{i}_{v}') for v in free})
        solver.add(legal(c))
    result = {'ordinary_first_layer':b_count,'vertices':n,'candidate_limit':8, 'far_count':far_count, 'left_ports':left_ports,
              'synthesis_queries':0,'oracle_queries':0,'candidates':[], 'counterexamples':[]}
    for attempt in range(8):
        status = solver.check(); result['synthesis_queries'] += 1
        if status == z3.unsat:
            result['status'] = 'unsat'; break
        if status != z3.sat:
            raise RuntimeError(solver.reason_unknown())
        model = solver.model()
        edges = fixed+[e for e in possible if z3.is_true(model.eval(edge[e]))]
        graph = {'n':n,'edges':[list(e) for e in edges]}
        g = target_domain(graph)
        assert max(nx.single_source_shortest_path_length(g,0).values()) <= 3
        result['candidates'].append(graph)
        oracle,c = target_solver(g)
        oracle.add(c[0] == False)
        for good in ALLOWED:
            oracle.add(z3.Or([c[v] != bool(bit) for v,bit in zip(ports,good)]))
        bad = solve(oracle,c); result['oracle_queries'] += 1
        if bad is None:
            witnesses=[]; relation=set()
            for tail in product((0,1),repeat=n-1):
                coloring=[0]+list(tail)
                if target_valid(g,coloring):
                    witnesses.append(coloring); relation.add(tuple(coloring[v] for v in ports))
            assert relation == ALLOWED
            result.update(status='exact-local-relation',ports=ports,witnesses=witnesses,
                          exhaustive_colorings=2**(n-1))
            break
        assert target_valid(g,bad) and tuple(bad[v] for v in ports) not in ALLOWED
        result['counterexamples'].append(bad)
        for interior in product((0,1),repeat=len(free)):
            assignment = dict(enumerate(bad))
            assignment.update(zip(free,interior))
            solver.add(z3.Not(legal({v:z3.BoolVal(bool(bit)) for v,bit in assignment.items()})))
    else:
        result['status']='candidate-limit'
    result['elapsed_seconds']=monotonic()-start
    return result


if __name__ == '__main__':
    for size,far_count,left_ports in [(2,3,2),(3,3,2),(2,3,1),(3,3,1)]:
        result=search(size,far_count,left_ports)
        (HERE/f'result-{size}-{far_count}-{left_ports}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k not in ('candidates','counterexamples','witnesses')}),flush=True)
        print(f"candidate graphs: {len(result['candidates'])}; counterexamples: {len(result['counterexamples'])}",flush=True)
        if result['status']=='exact-local-relation':
            break
