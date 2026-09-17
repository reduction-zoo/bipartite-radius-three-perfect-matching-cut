from pathlib import Path
import json,subprocess,sys
H=Path(__file__).resolve().parent
candidate=H.parent.parent/'algorithm.py'
inputs=['{"n":'+'1'*5000+',"variables":[],"clauses":[]}', '['*20000+'0'+']'*20000, '{', '{}', '{"n":0,"variables":[],"clauses":[]}']
records=[]
for text in inputs:
 run=subprocess.run([sys.executable,str(candidate)],input=text,text=True,capture_output=True)
 record=dict(input=text,returncode=run.returncode,stdout=run.stdout,stderr=run.stderr);records.append(record)
 (H/'result.json').write_text(json.dumps(records,indent=2)+'\n')
 assert run.returncode==0
 result=json.loads(run.stdout)
 assert result['n']==(2 if text==inputs[-1] else 6)
 if result['n']==6:assert {tuple(sorted(e)) for e in result['edges']}=={(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)}
print('PASS: oversized integer, deeply nested invalid source, malformed JSON, wrong schema, valid empty formula')
