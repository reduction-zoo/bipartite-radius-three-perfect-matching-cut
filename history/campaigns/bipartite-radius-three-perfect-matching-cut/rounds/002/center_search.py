"""Finite exact synthesis of radius-three NAE clauses with a shared matched center edge."""
from itertools import product
import json
from pathlib import Path
import networkx as nx
import z3

HERE = Path(__file__).resolve().parent


def synthesize(auxiliary_count, far_count):
    # Vertices 0 and 1 are a shared opposite-color matched pair.
    k = auxiliary_count + far_count + 3
    a = list(range(2, 2+k))
    ports = list(range(2+k, 5+k))
    b = list(range(5+k, 5+k+auxiliary_count))
    far = list(range(5+k+auxiliary_count, 5+k+auxiliary_count+far_count))
    n = 2*k+2
    fixed = [(0, 1)] + [(0, v) for v in b]
    possible = [(u, v) for u in a for v in [1]+b+ports+far]
    edge = {e: z3.Bool(f'e{e[0]}_{e[1]}') for e in possible}
    solver = z3.Solver()
    for u in a:
        solver.add(z3.Or([edge[u, v] for v in [1]+b]))
    for v in ports+far:
        solver.add(z3.Or([edge[u, v] for u in a]))

    def constraints(values):
        c = {0: z3.BoolVal(False), 1: z3.BoolVal(True)}
        c.update({v:z3.BoolVal(False) for v in b}); c.update(values)
        conditions = []
        for u in range(n):
            terms = [z3.If(c[x] != c[y], 1, 0) for x, y in fixed if u in (x, y)]
            terms += [z3.If(z3.And(present, c[x] != c[y]), 1, 0) for (x, y), present in edge.items() if u in (x, y)]
            conditions.append(z3.Sum(terms) == 1)
        return z3.And(conditions)

    for number, bits in enumerate(product((0, 1), repeat=3)):
        pin = {p:z3.BoolVal(bool(v)) for p, v in zip(ports, bits)}
        if len(set(bits)) == 2:
            values = pin | {u:z3.Bool(f'c{number}_{u}') for u in a+far}
            solver.add(constraints(values))
        else:
            for colors in product((0, 1), repeat=k+far_count):
                values = pin | {u:z3.BoolVal(bool(v)) for u, v in zip(a+far, colors)}
                solver.add(z3.Not(constraints(values)))
    result = solver.check()
    record = {'auxiliary_count':auxiliary_count, 'far_count':far_count, 'vertices':n,
              'optional_edges':len(possible), 'result':str(result)}
    if result == z3.sat:
        model = solver.model()
        edges = fixed + [list(e) for e in possible if z3.is_true(model.eval(edge[e]))]
        g = nx.Graph(); g.add_nodes_from(range(n)); g.add_edges_from(edges)
        assert nx.is_bipartite(g) and nx.is_connected(g)
        assert max(nx.single_source_shortest_path_length(g, 0).values()) <= 3
        relation = set(); witnesses = []
        for colors in product((0, 1), repeat=n-2):
            c = (0, 1)+colors
            if all(sum(c[v] != c[w] for w in g[v]) == 1 for v in g):
                relation.add(tuple(c[p] for p in ports)); witnesses.append(list(c))
        assert relation == set(product((0,1),repeat=3))-{(0,0,0),(1,1,1)}
        record.update(edges=edges, ports=ports, witnesses=witnesses)
    elif result != z3.unsat:
        raise RuntimeError(f'{result}: {solver.reason_unknown()}')
    return record


if __name__ == '__main__':
    records = []
    for count, far_count in [(0,1),(1,1),(2,1),(0,2),(1,2)]:
        record = synthesize(count, far_count); records.append(record)
        print(json.dumps(record), flush=True)
        (HERE/'center-search.json').write_text(json.dumps(records, indent=2)+'\n')
        if record['result'] == 'sat':
            break
    print('Completed finite family; no reduction or general impossibility claim.', flush=True)
