"""Additional fresh-process checks using independently written predicates."""
import argparse
from itertools import combinations, product
import json
from pathlib import Path
import random
import subprocess
import sys
import networkx as nx
import z3


def call(candidate, value, extract=False):
    run = subprocess.run([sys.executable, str(candidate)] + (['--extract'] if extract else []),
                         input=json.dumps(value), text=True, capture_output=True, check=True)
    return json.loads(run.stdout)


def source_ok(x, bits):
    return (len(bits) == x['n'] and all(type(v) is int and v in (0, 1) for v in bits)
            and all(0 < sum(bits[v] for v in c) < 3 for c in x['clauses']))


def graph_and_solver(target):
    assert set(target) == {'n', 'edges'} and type(target['n']) is int
    n = target['n']; assert n >= 2
    g = nx.Graph(); g.add_nodes_from(range(n)); seen = set()
    for edge in target['edges']:
        assert len(edge) == 2 and all(type(v) is int and 0 <= v < n for v in edge)
        a, b = edge; assert a != b and tuple(sorted(edge)) not in seen
        seen.add(tuple(sorted(edge))); g.add_edge(a, b)
    distances = nx.single_source_shortest_path_length(g, 0)
    assert len(distances) == n and max(distances.values()) <= 3 and nx.is_bipartite(g)
    c = [z3.Bool(f'color{v}') for v in range(n)]; s = z3.Solver()
    for v in g:s.add(z3.PbEq([(z3.Xor(c[v], c[w]), 1) for w in g[v]], 1))
    return g, s, c


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--candidate', type=Path, required=True)
    args = parser.parse_args(); candidate = args.candidate.resolve()
    out = Path(__file__).resolve().parent/'evidence'/'full-rule'; out.mkdir(parents=True, exist_ok=True)
    triples = list(combinations(range(4), 3))
    formulas = [(4, [list(c) for j, c in enumerate(triples) if mask >> j & 1]) for mask in range(16)]
    fano = [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]]
    formulas += [(0, []), (8, []), (7, fano), (8, fano+fano), (7, [c[::-1] for c in fano[::-1]]), (3, [[0,1,2]]*5)]
    rng = random.Random(4801)
    for n in [5,6,7,8]:
        for m in [1,4,8,16]:
            formulas.append((n, [rng.sample(range(n),3) for _ in range(m)]))
    totals = dict(instances=len(formulas),yes=0,no=0,solver_queries=0,recoveries=0,maximum_vertices=0)
    for i,(n,clauses) in enumerate(formulas):
        x = dict(n=n,variables=list(range(n)),clauses=clauses)
        expected = any(source_ok(x,list(bits)) for bits in product((0,1),repeat=n))
        target = call(candidate,x); g,s,c = graph_and_solver(target)
        totals['maximum_vertices']=max(totals['maximum_vertices'],len(g))
        if clauses:
            assert len(g)==4+8*n+160*len(clauses)
            assert len(g.edges())==3+14*n+304*len(clauses)
        record=dict(source=x,target=target,expected=expected,recoveries=[])
        try:
            for j in range(4):
                answer=s.check();totals['solver_queries']+=1;assert answer!=z3.unknown
                if j==0:assert (answer==z3.sat)==expected
                if answer==z3.unsat:break
                model=s.model();y=[int(z3.is_true(model.eval(v,model_completion=True))) for v in c]
                assert all(sum(y[v]!=y[w] for w in g[v])==1 for v in g)
                recovered=call(candidate,dict(source=x,target_solution=y),True)
                record['recoveries'].append(dict(target_witness=y,source_witness=recovered));totals['recoveries']+=1
                assert source_ok(x,recovered)
                s.add(z3.Or([v!=bool(bit) for v,bit in zip(c,y)]))
            totals['yes' if expected else 'no']+=1
        finally:
            (out/f'case-{i:02}.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(totals));print('PASS: independent predicates, source enumeration and actual-output witness recovery')
