import argparse
import itertools
import json
from pathlib import Path
import subprocess
import sys
import networkx as nx
import z3


def witness(g,matching):
    if type(matching)!=list or any(type(e)!=list or len(e)!=2 or any(type(v)!=int for v in e) for e in matching):return False
    if any(u>=v or not g.has_edge(u,v) for u,v in matching):return False
    counts={v:0 for v in g}
    for u,v in matching:counts[u]+=1;counts[v]+=1
    if any(c!=1 for c in counts.values()):return False
    remaining=nx.Graph();remaining.add_nodes_from(g);remaining.add_edges_from(e for e in g.edges() if sorted(e) not in matching)
    return nx.number_connected_components(remaining)>1


def run(path,data,extract=False):
    p=subprocess.run([sys.executable,str(path)]+(['--extract'] if extract else []),input=json.dumps(data),text=True,capture_output=True,check=True)
    return json.loads(p.stdout)


def check(path,g):
    source={'n':len(g),'edges':sorted([sorted(e) for e in g.edges()])}
    yes=any(witness(g,[list(e) for e in es]) for es in itertools.combinations(g.edges(),len(g)//2))
    target=run(path,source)
    assert type(target)==dict and set(target)=={'n','edges'}
    n=target['n'];edges=target['edges'];assert type(n)==int and n>0 and type(edges)==list
    assert all(type(e)==list and len(e)==2 and all(type(v)==int for v in e) and 0<=e[0]<e[1]<n for e in edges)
    assert len(set(map(tuple,edges)))==len(edges)
    h=nx.Graph();h.add_nodes_from(range(n));h.add_edges_from(edges)
    assert nx.is_bipartite(h) and nx.is_connected(h)
    assert any(len(nx.single_source_shortest_path_length(h,v,cutoff=3))==n for v in h)
    s=z3.Solver();color={v:z3.Bool(f'c{v}') for v in h};selected={tuple(e):z3.Bool(f'e{e[0]}_{e[1]}') for e in edges}
    s.add(color[0],z3.Or([z3.Not(c) for c in color.values()]))
    for v in h:
        terms=[(selected[tuple(sorted((u,v)))],1) for u in h[v]]
        s.add(z3.PbEq(terms,1) if terms else False)
    for (u,v),bit in selected.items():s.add(z3.Or(bit,color[u]==color[v]))
    status=s.check();assert status in (z3.sat,z3.unsat)
    if (status==z3.sat)!=yes:
        Path(__file__).with_name('failure.json').write_text(json.dumps({'source':source,'target':target,'source_yes':yes,'target_status':str(status)}));raise AssertionError('Decision mismatch')
    recovered=0
    for _ in range(2 if yes else 0):
        status=s.check()
        if status==z3.unsat:break
        assert status==z3.sat
        model=s.model();values={e:z3.is_true(model.eval(bit,model_completion=True)) for e,bit in selected.items()}
        matching=[list(e) for e,t in values.items() if t];assert witness(h,matching)
        answer=run(path,{'source':source,'target_solution':matching},True)
        if not witness(g,answer):
            Path(__file__).with_name('failure.json').write_text(json.dumps({'source':source,'target':target,'matching':matching,'recovered':answer}));raise AssertionError('Recovery mismatch')
        recovered+=1;s.add(z3.Or([bit!=values[e] for e,bit in selected.items()]))
    return {'source_order':len(g),'source_edges':source['edges'],'yes':yes,'target_order':n,'target_size':len(edges),'recoveries':recovered}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--candidate',type=Path,required=True);a=p.parse_args()
    graphs=[g for g in nx.graph_atlas_g() if 1<=len(g)<=5 and nx.is_connected(g) and nx.is_bipartite(g)]
    ladder=nx.convert_node_labels_to_integers(nx.grid_2d_graph(2,3))
    graphs += [nx.cycle_graph(6),ladder,nx.cycle_graph(8),nx.path_graph(8)]
    results=[check(a.candidate.resolve(),g) for g in graphs]
    print(json.dumps(results,indent=2))
