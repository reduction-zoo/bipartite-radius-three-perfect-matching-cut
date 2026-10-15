from pathlib import Path
import json,importlib.util
import networkx as nx
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cover',HERE.parent/'022/check.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
interfaces=json.loads((HERE.parent/'021/result.json').read_text())['successes']
for it in interfaces:
    for w in it['witnesses']:
        assert any(w[v]!=w[0] for v in range(3))
        assert any(w[v]!=w[0] for v in range(3,6))
centers=0
records=json.loads((HERE.parent/'022/result.json').read_text())
for rec in records:
    g=nx.Graph();g.add_nodes_from(range(rec['n']));g.add_edges_from(rec['edges'])
    h=module.construct(g,interfaces[rec['interface']]['edges'])
    assert min(nx.eccentricity(h).values())>=4
    centers+=len(h)
print(json.dumps(dict(interfaces=len(interfaces),outputs=len(records),centers=centers,solver_queries=0)))
print('PASS: private-interface obstruction consistency checks')
