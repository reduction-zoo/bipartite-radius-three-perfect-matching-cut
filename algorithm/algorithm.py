"""Positive NAE-3-SAT to bipartite radius-three Perfect Matching Cut."""
import argparse
import json
import sys


def valid_source(x):
    if not isinstance(x, dict) or set(x) != {'n', 'variables', 'clauses'}:
        return False
    n = x['n']
    return (type(n) is int and n >= 0
            and isinstance(x['variables'], list) and len(x['variables']) == n
            and all(type(v) is int and v == i for i, v in enumerate(x['variables']))
            and isinstance(x['clauses'], list)
            and all(isinstance(c, list) and len(c) == 3
                    and all(type(v) is int and 0 <= v < n for v in c)
                    and len(set(c)) == 3 for c in x['clauses']))


def forward(x):
    if not valid_source(x):
        return {'n': 6, 'edges': [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]]}
    if not x['clauses']:
        return {'n': 2, 'edges': [[0, 1]]}
    variables = x['n']
    clauses = []
    for clause in x['clauses']:
        for positive in (True, False):
            selected = list(range(variables, variables + 3))
            slack = list(range(variables + 3, variables + 6))
            variables += 6
            clauses.append([(v, True) for v in selected])
            clauses.extend([[(s, True), (v, not positive), (t, True)]
                            for s, v, t in zip(selected, clause, slack)])
    edges = [(0, 1), (0, 2), (2, 3)]
    for i in range(variables):
        f, p, r, z, a, v, w, q = range(4 + 8*i, 12 + 8*i)
        edges.extend([(1, f), (f, p), (f, r), (z, 2), (z, p), (z, r),
                      (0, a), (a, v), (a, w), (q, v), (q, w), (p, v), (r, w), (z, a)])
    for i, clause in enumerate(clauses):
        f, d0, d1, d2, t0, t1, t2, a = range(4 + 8*variables + 8*i, 12 + 8*variables + 8*i)
        low, high = [d0, d1, d2], [t0, t1, t2]
        edges.extend([(1, f), (0, a)])
        edges.extend((f, t) for t in high)
        edges.extend((a, d) for d in low)
        edges.extend((d, t) for j, d in enumerate(low) for k, t in enumerate(high) if j != k)
        edges.extend((t, 4 + 8*v + (6 if positive else 5))
                     for t, (v, positive) in zip(high, clause))
    return {'n': 4 + 8*variables + 8*len(clauses),
            'edges': [[min(a, b), max(a, b)] for a, b in edges]}


def recover(x, y):
    if not valid_source(x):
        raise ValueError('recovery requires a valid source')
    target = forward(x)
    if not isinstance(y, list) or len(y) != target['n'] or any(type(v) is not int or v not in (0, 1) for v in y):
        raise ValueError('target witness bits')
    counts = [0] * target['n']
    for a, b in target['edges']:
        if y[a] != y[b]:
            counts[a] += 1
            counts[b] += 1
    if any(count != 1 for count in counts):
        raise ValueError('not a perfect-cut witness')
    return [y[5 + 8*i] ^ y[0] for i in range(x['n'])] if x['clauses'] else [0] * x['n']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--extract', action='store_true')
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)
    try:
        value = json.load(sys.stdin)
    except (json.JSONDecodeError, RecursionError):
        if args.extract:
            raise
        value = None
    if args.extract:
        if not isinstance(value, dict) or set(value) != {'source', 'target_solution'}:
            raise ValueError('recovery input keys')
        result = recover(value['source'], value['target_solution'])
    else:
        result = forward(value)
    print(json.dumps(result))
