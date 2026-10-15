"""Independent finite audit; run from any directory. Never imports the candidate."""
import itertools
import json
from pathlib import Path
import subprocess
import sys
import networkx as nx
import z3

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE.parents[1] / 'work' / 'algorithm.py'


def call(data, extract=False):
    result = subprocess.run([sys.executable, str(CANDIDATE)] + (['--extract'] if extract else []), input=json.dumps(data), text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def valid(g, matching):
    pairs = [tuple(e) for e in matching]
    assert len(set(pairs)) == len(pairs)
    assert sorted(v for e in pairs for v in e) == list(range(len(g)))
    assert all(u < v and g.has_edge(u, v) for u, v in pairs)
    residual = g.copy()
    residual.remove_edges_from(pairs)
    assert not nx.is_connected(residual)
    return nx.number_connected_components(residual)


def source_yes(g):
    for edges in itertools.combinations(sorted(g.edges()), len(g)//2):
        if sorted(v for e in edges for v in e) != list(range(len(g))):
            continue
        residual = g.copy()
        residual.remove_edges_from(edges)
        if not nx.is_connected(residual):
            return True
    return False


def audit(g, name):
    source = {'n': len(g), 'edges': [list(sorted(e)) for e in reversed(list(g.edges()))]}
    output = call(source)
    h = nx.Graph()
    h.add_nodes_from(range(output['n']))
    h.add_edges_from(output['edges'])
    assert h.number_of_edges() == len(output['edges'])
    assert all(0 <= u < v < len(h) for u,v in output['edges'])
    assert nx.is_connected(h) and nx.is_bipartite(h)
    assert nx.eccentricity(h, 0) <= 3
    n,m = len(g),g.number_of_edges()
    b = sum(d*(d-1)//2 for _,d in g.degree())
    zz = sum(max(d-3,0) for _,d in g.degree())+2*max(n-3,0)
    c = sum(max(d-2,1) for _,d in g.degree())+b+2*m+2*max(n-2,1)
    nv = n+m+zz+6*c
    assert len(h) == 14+8*nv+32*c
    assert h.number_of_edges() == 25+18*nv+76*c
    edges = sorted(h.edges())
    bits = [z3.Bool(f'e{i}') for i in range(len(edges))]
    colors = [z3.Bool(f'c{i}') for i in range(len(h))]
    solver = z3.Solver()
    incidence = [[] for _ in h]
    for (u,v),bit in zip(edges,bits):
        incidence[u].append((bit,1));incidence[v].append((bit,1))
        solver.add(z3.Implies(colors[u] != colors[v], bit))
    solver.add([z3.PbEq(row,1) for row in incidence])
    solver.add(z3.Not(colors[0]), z3.Or(colors))
    expected = source_yes(g)
    components = []
    for _ in range(3 if expected else 1):
        result = solver.check()
        assert result in (z3.sat,z3.unsat)
        assert (result == z3.sat) == expected
        if not expected:break
        model = solver.model()
        selected = [z3.is_true(model.eval(bit)) for bit in bits]
        witness = [list(e) for e,b in zip(edges,selected) if b]
        components.append(valid(h,witness))
        recovered = call({'source':source,'target_solution':witness},True)
        valid(g,recovered)
        solver.add(z3.Or([bit != value for bit,value in zip(bits,selected)]))
    return {'name':name,'source_yes':expected,'target_vertices':len(h),'distinct_recoveries':len(components),'deletion_component_counts':components}


def local_states():
    # Directly enumerate private colors, including anchors forced by reservoirs.
    binary = [(0,1),(0,2),(3,1),(3,2),(4,5),(4,6),(7,5),(7,6),(1,5),(2,6)]
    selector = [(1,i) for i in (2,3,4)]+[(0,i) for i in (5,6,7)]+[(2+i,5+j) for i in range(3) for j in range(3) if i != j]
    counts = {}
    for name,edges,anchors in [('binary',binary,{0:1,3:0,4:0,7:1}),('selector',selector,{0:1,1:0})]:
        for opposite in (False,True):
            accepted=[]
            for bits in itertools.product((0,1),repeat=8):
                if any(bits[v] != (color if opposite else 0) for v,color in anchors.items()):continue
                degrees=[0]*8
                for u,v in edges:
                    if bits[u] != bits[v]:degrees[u]+=1;degrees[v]+=1
                if max(degrees)<=1:
                    accepted.append(bits)
                    if opposite:assert degrees == [1]*8
            assert len(accepted) == ((2 if name=='binary' else 3) if opposite else 1)
            if not opposite:assert accepted == [(0,)*8]
            counts[f'{name}_{opposite}']=len(accepted)
    # The added vertices repair both residual sides after the joining edge is used.
    reservoir=nx.complete_bipartite_graph(4,3)
    reservoir.remove_node(0)
    assert len(nx.max_weight_matching(reservoir,maxcardinality=True)) == 3
    return counts


if __name__ == '__main__':
    cases = [(nx.complete_bipartite_graph(2,4),'unbalanced_dense'),(nx.cubical_graph(),'cube'),(nx.path_graph(9),'odd_radius_four_path')]
    invalid=[{'n':True,'edges':[]},{'n':3,'edges':[[0,1],[1,2],[0,2]]},{'n':2,'edges':[[0,1],[0,1]]},{'n':2,'edges':[[1,0]]}]
    assert all(call(x)=={} for x in invalid)
    result={'local_states':local_states(),'invalid_encodings':len(invalid),'cases':[audit(g,name) for g,name in cases]}
    (HERE/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
