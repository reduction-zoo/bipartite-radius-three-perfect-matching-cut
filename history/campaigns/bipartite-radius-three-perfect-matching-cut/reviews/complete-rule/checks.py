"""Independent finite checks: no candidate imports, no timeouts."""
import itertools
import json
from pathlib import Path
import subprocess
import sys
import z3

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE.parents[1] / 'work' / 'algorithm.py'
records = []

def run(raw, extract=False):
    p = subprocess.run([sys.executable, str(CANDIDATE)] + (['--extract'] if extract else []), input=raw, text=True, capture_output=True)
    records.append(dict(input=raw, extract=extract, returncode=p.returncode, stdout=p.stdout, stderr=p.stderr))
    return p

def call(x, extract=False):
    p = run(json.dumps(x), extract)
    assert p.returncode == 0, p.stderr
    return json.loads(p.stdout)

def local(names, edges, relaxed, pinned):
    out = []
    for bits in itertools.product((0, 1), repeat=len(names)):
        c = dict(zip(names, bits))
        if any(c[v] != bit for v, bit in pinned.items()):
            continue
        counts = {v: sum(c[v] != c[b if a == v else a] for a, b in edges if v in (a,b)) for v in names}
        if all(counts[v] <= 1 if v in relaxed else counts[v] == 1 for v in names):
            out.append(dict(colors=c, counts=counts))
    return out

# Write the named edges independently from the mathematical specification.
selector_edges = [('u','h'),('h','F'),('u','A')]
selector_edges += [('F',f'T{i}') for i in range(3)] + [('A',f'd{i}') for i in range(3)]
selector_edges += [(f'd{i}',f'T{j}') for i in range(3) for j in range(3) if i != j]
selector = local(['u','h','F','A','d0','d1','d2','T0','T1','T2'], selector_edges, {'u','h','T0','T1','T2'}, {'u':0})
assert len(selector) == 3
for row in selector:
    c,k = row['colors'],row['counts']
    assert c['h'] == c['F'] == 1 and c['A'] == 0
    assert sum(c[f'd{i}'] for i in range(3)) == 1
    assert all(c[f'T{i}'] == 1-c[f'd{i}'] and k[f'T{i}'] == 1 for i in range(3))
variable_edges = [('u','h'),('u','b'),('b','t'),('h','f'),('f','p'),('f','r'),('z','b'),('z','p'),('z','r'),('u','a'),('a','v'),('a','w'),('q','v'),('q','w'),('p','v'),('r','w'),('z','a')]
variable = local(['u','h','b','t','f','p','r','z','a','v','w','q'], variable_edges, {'u','h','b','v','w'}, {'u':0,'h':1})
assert len(variable) == 2
for row in variable:
    c,k = row['colors'],row['counts']
    assert c['p'] == c['v'] == 1-c['r'] == 1-c['w']
    assert k['v'] == k['w'] == 1
(HERE/'local-states.json').write_text(json.dumps(dict(selector=selector,variable=variable),indent=2)+'\n')
print('PASS: all 512 normalized selector states and 1024 pinned variable states; exactly 3 and 2 survive')

formulas = [(3,[[0,1,2]]), (5,[[0,1,2]]*7+[[0,3,4],[1,3,4]]), (5,list(map(list,itertools.combinations(range(5),3)))), (0,[]),(4,[])]
full = []
for n, clauses in formulas:
    x = dict(n=n,variables=list(range(n)),clauses=clauses)
    g = call(x); order = g['n']; edges = g['edges']
    assert set(g)=={'n','edges'} and len({tuple(sorted(e)) for e in edges})==len(edges)
    adj = [[] for _ in range(order)]
    for a,b in edges:
        assert 0 <= a < b < order
        adj[a].append(b); adj[b].append(a)
    distance = {0:0}; queue = [0]
    for a in queue:
        for b in adj[a]:
            if b not in distance: distance[b]=distance[a]+1; queue.append(b)
    assert len(distance)==order and max(distance.values())<=3
    assert all(distance[a]%2 != distance[b]%2 for a,b in edges)
    if clauses: assert order==4+8*n+160*len(clauses) and len(edges)==3+14*n+304*len(clauses)
    c = [z3.Bool(f'x{i}') for i in range(order)]
    solver = z3.Solver()
    for a in range(order): solver.add(z3.Sum([z3.If(c[a]!=c[b],1,0) for b in adj[a]])==1)
    satisfiers = [bits for bits in itertools.product((0,1),repeat=n) if all(0 < sum(bits[v] for v in cl) < 3 for cl in clauses)]
    answer = solver.check(); assert answer != z3.unknown and (answer==z3.sat)==bool(satisfiers)
    detail=dict(source=x,target=g,decision=str(answer),recoveries=[])
    if clauses:
        solver.push()
        solver.add(z3.Or([z3.And(c[5+8*a]==c[5+8*b],c[5+8*b]==c[5+8*d]) for a,b,d in clauses]))
        assert solver.check()==z3.unsat
        solver.pop()
        detail['all_bad_projected_witnesses']='unsat'
    if n==3:
        for bits in itertools.product((0,1),repeat=n):
            solver.push()
            solver.add(*[z3.Xor(c[5+8*i],c[0])==bool(bits[i]) for i in range(n)])
            assert (solver.check()==z3.sat)==(bits in satisfiers)
            if bits in satisfiers:
                model=solver.model(); y=[int(z3.is_true(model.eval(v))) for v in c]
                for witness in (y,[1-v for v in y]):
                    recovered=call(dict(source=x,target_solution=witness),True)
                    assert tuple(recovered)==bits
                    detail['recoveries'].append(dict(y=witness,recovered=recovered))
            solver.pop()
    elif answer==z3.sat:
        assert solver.check()==z3.sat
        model=solver.model(); y=[int(z3.is_true(model.eval(v))) for v in c]
        for witness in (y,[1-v for v in y]):
            assert all(sum(witness[a]!=witness[b] for b in adj[a])==1 for a in range(order))
            recovered=call(dict(source=x,target_solution=witness),True)
            assert tuple(recovered) in satisfiers
            detail['recoveries'].append(dict(y=witness,recovered=recovered))
    full.append(detail)
(HERE/'full-checks.json').write_text(json.dumps(full,indent=2)+'\n')
print('PASS: 5 injected graphs, 8 fixed source projections, 3 exhaustive bad-projection exclusions, 18 fresh recoveries')

invalid = ['{','null','[]','{"n":true,"variables":[],"clauses":[]}', '{"n":0,"variables":[],"clauses":[[0,0,0]]}', '{"n":'+('1'*5000)+',"variables":[],"clauses":[]}', '['*1200+'0'+']'*1200]
failures=[]
for i,raw in enumerate(invalid):
    p=run(raw)
    if p.returncode!=0 or json.loads(p.stdout)!={'n':6,'edges':[[0,1],[1,2],[2,3],[3,4],[4,5],[0,5]]}:
        failures.append(i)
(HERE/'process-records.json').write_text(json.dumps(records,indent=2)+'\n')
print('Malformed-source failures:', failures)
assert not failures, f'Totality failed for malformed input indices {failures}; originals in process-records.json'
