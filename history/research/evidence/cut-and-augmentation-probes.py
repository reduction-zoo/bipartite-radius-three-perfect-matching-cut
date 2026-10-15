"""Bounded relation checks for Karp-reduction topic screening, not hardness proofs."""
from itertools import combinations, product
import networkx as nx


def colorings(g, perfect):
    nodes = list(g)
    for bits in product((0, 1), repeat=len(nodes)):
        if len(set(bits)) != 2:
            continue
        colors = dict(zip(nodes, bits))
        counts = [sum(colors[v] != colors[u] for u in g[v]) for v in nodes]
        if all(c == 1 if perfect else c <= 1 for c in counts):
            yield colors


def disconnected_perfect_matching(g):
    for colors in colorings(g, False):
        boundary = {v for u, v in g.edges() if colors[u] != colors[v]}
        boundary |= {u for u, v in g.edges() if colors[u] != colors[v]}
        residual = g.subgraph(set(g) - boundary)
        # Cross edges have already been chosen. The remaining matching is internal.
        internal = nx.Graph()
        internal.add_nodes_from(residual)
        internal.add_edges_from((u, v) for u, v in residual.edges() if colors[u] == colors[v])
        if 2 * len(nx.max_weight_matching(internal, maxcardinality=True)) == len(internal):
            return True
    return False


def cube_relation():
    cube = nx.Graph((u, v) for u in range(8) for v in range(u + 1, 8)
                    if (u ^ v).bit_count() == 1)
    assignments = list(colorings(cube, True))
    relation = {tuple(c[p] for p in (1, 2, 4)) for c in assignments}
    assert len(assignments) == 6
    assert relation == set(product((0, 1), repeat=3)) - {(0, 0, 0), (1, 1, 1)}
    assert all(c[0] != c[7] for c in assignments)
    # Retain the existing internal perfect-cut coloring; add hub--helper--0.
    # Hub color is pinned to auxiliary 7 by the proposed original connector.
    survivors = 0
    for colors in assignments:
        for helper in (0, 1):
            hub = colors[7]
            if helper == hub and helper == colors[0]:
                survivors += 1
    assert survivors == 0
    print('CUBE: all 256 colorings; 6 perfect cuts; terminal relation exactly NAE3')
    print('CUBE: 12 pinned helper extensions; none preserves a saturated hub and cube')


def cut_semantics():
    cycle = nx.cycle_graph(6)
    tree = nx.path_graph(7)
    tree.add_edge(1, 7)
    for name, g in [('C6', cycle), ('P7 plus leaf at 1', tree)]:
        mc = bool(list(colorings(g, False)))
        pmc = bool(list(colorings(g, True)))
        dpm = disconnected_perfect_matching(g)
        assert nx.is_bipartite(g) and nx.radius(g) == 3
        assert (mc, pmc, dpm) == ((True, False, True) if name == 'C6' else (True, False, False))
        print(f'SEMANTICS: {name}: MC={mc}, PMC={pmc}, DPM={dpm}')


def two_hubs():
    checked, first = 0, None
    for g in nx.graph_atlas_g():
        if not 2 <= len(g) <= 6 or not nx.is_connected(g) or not nx.is_bipartite(g):
            continue
        h = g.copy()
        partition = nx.bipartite.color(g)
        a, b = len(g), len(g) + 1
        h.add_edge(a, b)
        h.add_edges_from((a if partition[v] else b, v) for v in g)
        assert nx.is_bipartite(h) and nx.diameter(h) <= 3
        before, after = bool(list(colorings(g, False))), bool(list(colorings(h, False)))
        checked += 1
        if before != after and first is None:
            first = (list(g.edges()), before, after)
    assert first is not None
    print(f'HUBS: {checked} connected bipartite atlas inputs through n=6; first failure={first}')


def contains(g, pattern):
    return any(nx.is_isomorphic(g.subgraph(vertices), pattern)
               for vertices in combinations(g, len(pattern)))


def induced_restrictions():
    path = nx.path_graph(6)
    two_paths = nx.disjoint_union(nx.path_graph(4), nx.path_graph(4))
    cone = two_paths.copy()
    cone.add_edges_from((8, v) for v in range(8))
    three_edges = nx.Graph([(0, 1), (2, 3), (4, 5)])
    assert not contains(path, three_edges) and not contains(cone, three_edges)
    assert contains(path, path) and not contains(path, two_paths)
    assert contains(cone, two_paths) and not contains(cone, path)
    print('CLASSES: P6 and cone(2P4) are connected 3P2-free counterexamples to the two identity maps')
    # A plane P3 can be extended to K4 by adding one vertex, but not to any
    # cubic graph on the original three vertices (the degree sum would be odd).
    k4 = nx.complete_graph(4)
    assert nx.check_planarity(k4)[0] and nx.node_connectivity(k4) == 3
    assert all(k4.has_edge(u, v) for u, v in nx.path_graph(3).edges())
    assert 3 * 3 % 2 == 1
    print('AUGMENTATION: P3 is NO for edges-only cubic completion and YES when vertices are allowed')


if __name__ == '__main__':
    cube_relation()
    cut_semantics()
    two_hubs()
    induced_restrictions()
