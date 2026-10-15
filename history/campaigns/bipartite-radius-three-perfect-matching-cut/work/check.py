"""Exact definition-based oracles and fresh-process complete-rule checks."""
import argparse
from itertools import combinations, product
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import networkx as nx
import z3

HERE = Path(__file__).resolve().parent


def source_domain(x):
    if not isinstance(x, dict) or set(x) != {'n', 'variables', 'clauses'}:
        raise ValueError('source keys')
    n, variables, clauses = x['n'], x['variables'], x['clauses']
    if type(n) is not int or n < 0 or not isinstance(variables, list) or len(variables) != n:
        raise ValueError('explicit variable list')
    if any(type(v) is not int or v != i for i, v in enumerate(variables)):
        raise ValueError('variable labels')
    if not isinstance(clauses, list):
        raise ValueError('clause list')
    for c in clauses:
        if not isinstance(c, list) or len(c) != 3 or any(type(v) is not int or not 0 <= v < n for v in c) or len(set(c)) != 3:
            raise ValueError('positive three-distinct-variable clause')


def bits(y, n):
    return isinstance(y, list) and len(y) == n and all(type(v) is int and v in (0, 1) for v in y)


def source_valid(x, y):
    return bits(y, x['n']) and all(len({y[v] for v in c}) == 2 for c in x['clauses'])


def target_domain(x):
    if not isinstance(x, dict) or set(x) != {'n', 'edges'}:
        raise ValueError('target keys')
    n, edges = x['n'], x['edges']
    if type(n) is not int or n < 2 or not isinstance(edges, list) or n > len(edges) + 1:
        raise ValueError('connected target order')
    seen = set()
    for e in edges:
        if not isinstance(e, list) or len(e) != 2 or any(type(v) is not int or not 0 <= v < n for v in e) or e[0] == e[1]:
            raise ValueError('target edge')
        edge = tuple(sorted(e))
        if edge in seen:
            raise ValueError('duplicate edge')
        seen.add(edge)
    g = nx.Graph(); g.add_nodes_from(range(n)); g.add_edges_from(seen)
    if not nx.is_connected(g) or not nx.is_bipartite(g) or nx.radius(g) > 3:
        raise ValueError('target must be connected, bipartite and radius <= 3')
    return g


def target_valid(g, y):
    return bits(y, len(g)) and len(set(y)) == 2 and all(sum(y[v] != y[w] for w in g[v]) == 1 for v in g)


def source_solver(x):
    source_domain(x)
    c = [z3.Bool(f's{i}') for i in range(x['n'])]
    solver = z3.Solver()
    for a, b, d in x['clauses']:
        solver.add(z3.Or(c[a] != c[b], c[a] != c[d]))
    return solver, c


def target_solver(g):
    c = [z3.Bool(f't{i}') for i in range(len(g))]
    solver = z3.Solver()
    for v in g:
        solver.add(z3.Sum([z3.If(c[v] != c[w], 1, 0) for w in g[v]]) == 1)
    return solver, c


def solve(solver, colors):
    result = solver.check()
    if result == z3.unsat:
        return None
    if result != z3.sat:
        raise RuntimeError(f'inconclusive solver result: {result}: {solver.reason_unknown()}')
    model = solver.model()
    return [int(z3.is_true(model.eval(c, model_completion=True))) for c in colors]


def encode(g):
    return {'n': len(g), 'edges': [list(e) for e in sorted(g.edges())]}


def invoke(path, value, extract=False):
    result = subprocess.run([sys.executable, str(path)] + (['--extract'] if extract else []), input=json.dumps(value), text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f'candidate failed: {result.stderr}')
    return json.loads(result.stdout)


def check_case(path, case, record):
    source = case['source']; source_domain(source)
    sy = solve(*source_solver(source)); answer = sy is not None
    if sy is not None:
        assert source_valid(source, sy)
    assert answer == case['yes'], 'stored source answer'
    target = invoke(path, source); record.update(source=source, target=target, source_yes=answer)
    g = target_domain(target); solver, colors = target_solver(g)
    y = solve(solver, colors); record['target_yes'] = y is not None
    assert answer == (y is not None), 'decision mismatch'
    record['recoveries'] = []
    for _ in range(8):
        if y is None:
            break
        assert target_valid(g, y)
        recovered = invoke(path, {'source': source, 'target_solution': y}, True)
        record['recoveries'].append({'target_solution': y, 'source_solution': recovered})
        assert source_valid(source, recovered), 'invalid recovered source witness'
        solver.add(z3.Or([c != bool(v) for c, v in zip(colors, y)]))
        y = solve(solver, colors)


def self_test(cases):
    for case in cases:
        x = case['source']; y = solve(*source_solver(x))
        brute = any(source_valid(x, list(b)) for b in product((0, 1), repeat=x['n']))
        assert (y is not None) == brute == case['yes']
        if y is not None:
            assert source_valid(x, y)
    graphs = 0
    for g in nx.graph_atlas_g():
        if len(g) < 2 or not nx.is_connected(g) or not nx.is_bipartite(g) or nx.radius(g) > 3:
            continue
        target_domain(encode(g))
        y = solve(*target_solver(g))
        brute = any(target_valid(g, list(b)) for b in product((0, 1), repeat=len(g)))
        assert (y is not None) == brute
        if y is not None:
            assert target_valid(g, y)
        graphs += 1
    assert not target_valid(nx.cycle_graph(6), [0, 0, 0, 1, 1, 1])
    assert not target_valid(nx.path_graph(2), [False, True])
    assert not source_valid(cases[2]['source'], [0, 0, 0])
    invalid = [encode(nx.cycle_graph(3)), encode(nx.path_graph(8)), {'n':2,'edges':[[0,1],[1,0]]}]
    for x in invalid:
        try:
            target_domain(x)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid target accepted')
    fixtures = [
        ('invalid-graph', "print('{\"n\":2,\"edges\":[]}')", cases[2]),
        ('wrong-yes', "print('{\"n\":2,\"edges\":[[0,1]]}')", cases[4]),
        ('wrong-no', 'print('+repr(json.dumps(encode(nx.cycle_graph(6))))+')', cases[2]),
        ('bad-recovery', "import sys\nprint('[0,0,0]' if '--extract' in sys.argv else '{\"n\":2,\"edges\":[[0,1]]}')", cases[2]),
    ]
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory)/'valid_fixture.py'
        path.write_text("import sys\nprint('[0,0,1]' if '--extract' in sys.argv else '{\"n\":2,\"edges\":[[0,1]]}')")
        record = {}
        check_case(path, cases[2], record)
        assert len(record['recoveries']) == 2
        for name, code, case in fixtures:
            path = Path(directory)/'fixture.py'; path.write_text(code)
            record = {'fixture': name}
            try:
                check_case(path, case, record)
            except (ValueError, AssertionError) as error:
                record['detected'] = str(error)
            else:
                raise AssertionError(f'fixture accepted: {name}')
            (HERE/'self-test-evidence').mkdir(exist_ok=True)
            (HERE/'self-test-evidence'/f'{name}.json').write_text(json.dumps(record, indent=2)+'\n')
    print(f'PASS: {len(cases)} source cases, {graphs} bipartite radius<=3 atlas graphs through order seven, four faulty executable fixtures and one valid control')
    print(f'Z3 {z3.get_version_string()}, NetworkX {nx.__version__}; no timeouts')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--self-test', action='store_true'); mode.add_argument('--candidate', type=Path)
    args = parser.parse_args(); cases = json.loads((HERE/'cases.json').read_text())
    if args.self_test:
        self_test(cases)
    else:
        out = HERE/'candidate-evidence'; out.mkdir(exist_ok=True)
        for case in cases:
            record = {}
            try:
                check_case(args.candidate.resolve(), case, record)
            finally:
                (out/f"{case['name']}.json").write_text(json.dumps(record, indent=2)+'\n')
        print(f'PASS: {len(cases)} injected cases')
