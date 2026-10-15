"""Focused parser repair check; candidate runs in fresh processes."""
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE.parents[1] / 'work' / 'algorithm.py'
prior = HERE.parent / 'complete-rule'
records = []

def call(name, raw, extract=False):
    p = subprocess.run([sys.executable,str(CANDIDATE)]+(['--extract'] if extract else []),input=raw,text=True,capture_output=True)
    records.append(dict(name=name,input=raw,extract=extract,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
    return p

no = {'n':6,'edges':[[0,1],[1,2],[2,3],[3,4],[4,5],[0,5]]}
old = json.loads((prior/'process-records.json').read_text())[28]
assert old['returncode']==1 and len(old['input'])==5034
large = '1'*5000
cases = [
    ('original-oversized-n',old['input']),
    ('negative-oversized-n','{"n":-'+large+',"variables":[],"clauses":[]}'),
    ('oversized-variable-label','{"n":1,"variables":['+large+'],"clauses":[]}'),
    ('oversized-clause-label','{"n":3,"variables":[0,1,2],"clauses":[[0,1,'+large+']]}'),
    ('invalid-json','{'),
    ('nested-non-source','['*1200+'0'+']'*1200),
    ('integer-bool','{"n":true,"variables":[0],"clauses":[]}'),
]
for name,raw in cases:
    p=call(name,raw)
    assert p.returncode==0 and json.loads(p.stdout)==no, name
empty=dict(n=4,variables=list(range(4)),clauses=[])
p=call('legal-empty',json.dumps(empty))
assert p.returncode==0 and json.loads(p.stdout)==dict(n=2,edges=[[0,1]])
for y in ([0,1],[1,0]):
    p=call('legal-empty-recovery',json.dumps(dict(source=empty,target_solution=y)),True)
    assert p.returncode==0 and json.loads(p.stdout)==[0]*4
for raw in ('{','['*1200+'0'+']'*1200):
    p=call('malformed-recovery',raw,True)
    assert p.returncode!=0 and not p.stdout
example=json.loads((prior/'full-checks.json').read_text())[0]
p=call('unchanged-clause-graph',json.dumps(example['source']))
assert p.returncode==0 and json.loads(p.stdout)==example['target']
for evidence in example['recoveries'][:2]:
    p=call('unchanged-clause-recovery',json.dumps(dict(source=example['source'],target_solution=evidence['y'])),True)
    bits=json.loads(p.stdout)
    assert p.returncode==0 and bits==evidence['recovered']
    assert all(0<sum(bits[i] for i in clause)<3 for clause in example['source']['clauses'])
(HERE/'process-records.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS: 15 fresh processes; original totality failure repaired, 7 invalid forward inputs -> C6, valid source/recovery behavior retained, malformed recovery fails explicitly')
