from pathlib import Path
import importlib.util,json
import networkx as nx
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('synchronized_cover',HERE.parent/'019/check.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
records=json.loads((HERE.parent/'019/result.json').read_text());centers=0
for record in records:
    g=nx.Graph();g.add_nodes_from(range(record['n']));g.add_edges_from(record['edges'])
    h=module.construct(g);dist=dict(nx.all_pairs_shortest_path_length(h));n=len(g)
    for c in h:
        group=c//2 if c<2*n else (c-2*n)//6
        w=1 if group==0 else 0
        d0,d1=dist[c][2*w],dist[c][2*w+1]
        p,q=2*n+6*w+3,2*n+6*w+4
        assert abs(d0-d1)==1
        assert max(dist[c][p],dist[c][q])==min(d0,d1)+3>=4
        centers+=1
result=dict(graphs=len(records),centers=centers,solver_queries=0)
(HERE/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));print('PASS: distance obstruction at every checked target center')
