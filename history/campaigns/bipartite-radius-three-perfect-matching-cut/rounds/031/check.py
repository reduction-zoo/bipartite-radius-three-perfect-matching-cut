from itertools import product
from pathlib import Path
import json
import z3
HERE=Path(__file__).resolve().parent
ALLOWED={p for p in product((0,1),repeat=3) if sum(p)==1}

def search(b,f):
    k=b+f;ports=[0,1,2];a=list(range(3,3+k));h=3+k
    anchors=list(range(h+1,h+1+b));far=list(range(h+1+b,h+1+b+f));n=h+1+b+f
    edges=[(v,w) for v in a for w in [h]+anchors+far]+[(v,w) for v in ports for w in far]
    e={p:z3.Bool(f'e{p[0]}_{p[1]}') for p in edges};s=z3.Solver()
    for v in a:s.add(z3.Or([e[v,w] for w in [h]+anchors]))
    for w in far:s.add(z3.Or([e[v,w] for v in a+ports]))
    def legal(c,selected):
        return z3.And([z3.Sum([z3.If(z3.And(present,c[v]!=c[w]),1,0) for (v,w),present in selected.items() if node in (v,w)])==int(node not in ports+[h]) for node in range(n)])
    def coloring(bits,free):
        c={v:z3.BoolVal(bool(bit)) for v,bit in zip(ports,bits)};c[h]=z3.BoolVal(True)
        c.update({v:z3.BoolVal(False) for v in anchors});c.update(zip(a+far,free));return c
    for i,bits in enumerate(sorted(ALLOWED)):
        s.add(legal(coloring(bits,[z3.Bool(f'c{i}_{v}') for v in a+far]),e))
    result=dict(b=b,f=f,vertices=n,queries=0,candidates=[],bad=[])
    for attempt in range(8):
        status=s.check();result['queries']+=1
        if status==z3.unsat:result['status']='unsat';break
        if status!=z3.sat:raise RuntimeError(s.reason_unknown())
        m=s.model();chosen={p:z3.BoolVal(z3.is_true(m.eval(present))) for p,present in e.items()}
        result['candidates'].append([p for p,present in chosen.items() if z3.is_true(present)])
        oracle=z3.Solver();c={v:z3.Bool(f'x{v}') for v in range(n)}
        oracle.add(c[h]==True,*[c[v]==False for v in anchors],legal(c,chosen))
        oracle.add(z3.Or(*[z3.And(*[c[v]==bool(bit) for v,bit in zip(ports,bits)]) for bits in set(product((0,1),repeat=3))-ALLOWED]))
        status=oracle.check();result['queries']+=1
        if status==z3.unsat:result.update(status='exact-interface',ports=ports,h=h,anchors=anchors,far=far,a=a);break
        if status!=z3.sat:raise RuntimeError(oracle.reason_unknown())
        model=oracle.model();bad=tuple(int(z3.is_true(model.eval(c[v],model_completion=True))) for v in ports);result['bad'].append(bad)
        for values in product((0,1),repeat=len(a+far)):
            s.add(z3.Not(legal(coloring(bad,[z3.BoolVal(bool(v)) for v in values]),e)))
    else:result['status']='candidate-limit'
    return result

if __name__=='__main__':
    for b,f in [(1,3),(2,3)]:
        result=search(b,f);(HERE/f'result-{b}-{f}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({key:value for key,value in result.items() if key not in ['candidates','bad']}),flush=True)
        if result['status']=='exact-interface':break
