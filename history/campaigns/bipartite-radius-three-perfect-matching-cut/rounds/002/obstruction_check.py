"""Exhaustive checks of center-layer obstructions, independent of synthesis code."""
from itertools import product
import networkx as nx

centers = colorings = leaf_centers = 0
for g in nx.graph_atlas_g():
    if len(g) < 2 or not nx.is_connected(g) or not nx.is_bipartite(g):
        continue
    valid = [c for c in product((0, 1), repeat=len(g))
             if all(sum(c[v] != c[w] for w in g[v]) == 1 for v in g)]
    for u in g:
        dist = nx.single_source_shortest_path_length(g, u)
        if max(dist.values()) > 3:
            continue
        for h in g[u]:
            group = [c for c in valid if c[u] == 0 and c[h] == 1]
            if not group:
                continue
            centers += 1
            near = set(g[u]) - {h}
            second = {v for v in g if dist[v] == 2}
            third = {v for v in g if dist[v] == 3}
            fixed = {v for v in second if h in g[v] and not (set(g[v]) & near)}
            for c in group:
                assert sum(c[v] == 0 for v in third) == len(fixed)
                colorings += 1
                if g.degree(h) == 1:
                    assert all(c[v] == 1 for v in third)
                    leaf_centers += 1
print(f'PASS: {centers} feasible ordered center/mate choices; {colorings} colorings; {leaf_centers} leaf-mate colorings; atlas orders <=7')
