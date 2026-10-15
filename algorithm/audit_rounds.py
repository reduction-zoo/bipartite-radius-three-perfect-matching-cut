"""Check saved rounds without rerunning synthesis or importing search code."""
from itertools import product
import json
from pathlib import Path

import networkx as nx
import z3
from check import target_domain, target_solver, target_valid, solve

ROOT = Path(__file__).resolve().parent.parent
allowed = {p for p in product((0, 1), repeat=3) if len(set(p)) == 2}
counts = dict(graphs=0, positive_queries=0, bad_witnesses=0)
for number in range(4, 11):
    for path in sorted((ROOT/'rounds'/f'{number:03}').glob('result-*.json')):
        result = json.loads(path.read_text())
        for index, graph in enumerate(result['candidates']):
            g = target_domain(graph)
            assert nx.eccentricity(g, 0) <= 3
            b = result['ordinary_first_layer']
            patterns = allowed
            if number == 4:
                ports = list(range(8+b, 14+b))
                patterns = {tuple(v for bit in p for v in (bit, 1-bit)) for p in allowed}
            elif number == 7:
                ports = [2, 3, 4]
            elif number == 9:
                k = b + result['far_count'] - 1
                left = result['left_ports']
                ports = list(range(1, 1+left)) + list(range(1+k+b, 1+k+b+3-left))
            elif number == 10:
                ports = result['ports']
            else:
                raise AssertionError('Unexpected candidate-bearing round')
            for pattern in patterns:
                solver, colors = target_solver(g)
                if number != 10:
                    solver.add(colors[0] == False)
                if number in (4, 7):
                    solver.add(colors[1] == True)
                solver.add([colors[v] == bool(bit) for v, bit in zip(ports, pattern)])
                witness = solve(solver, colors)
                assert witness is not None and target_valid(g, witness)
                counts['positive_queries'] += 1
            if index < len(result['counterexamples']):
                bad = result['counterexamples'][index]
                assert target_valid(g, bad)
                assert tuple(bad[v] for v in ports) not in patterns
                assert bad[0] == 0
                if number in (4, 7):
                    assert bad[1] == 1
                counts['bad_witnesses'] += 1
            counts['graphs'] += 1
            if number == 10:
                adjacency = {v: list(g.neighbors(v)) for v in g}
                witnesses = [bits for bits in product((0, 1), repeat=g.number_of_nodes())
                             if all(sum(bits[v] != bits[u] for u in adjacency[v]) == 1 for v in g)]
                assert set(witnesses) == {tuple(w) for w in result['witnesses']}
                assert {tuple(w[v] for v in ports) for w in witnesses} == allowed
                assert nx.is_isomorphic(g, nx.cubical_graph())
                assert all(w[0] == int(sum(w[v] for v in ports) < 2) for w in witnesses)
                conditional = sorted({tuple(w[v] for v in ports) for w in witnesses if w[0] == 0})
                print(json.dumps(dict(cube_isomorphic=True, exhaustive_colorings=2**len(g),
                                     valid_colorings=len(witnesses), center_zero_patterns=conditional)))
print(json.dumps(counts))
print('PASS; author-side audit, not independent review or an UNSAT certificate')
