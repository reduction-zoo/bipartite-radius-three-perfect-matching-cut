"""Exact vector diagrams for the two graph interfaces."""
from pathlib import Path
from html import escape
import json

HERE=Path(__file__).resolve().parent
ROUND=HERE.parent.parent/'rounds'

def draw(path, positions, edges, colors, ports, width, height):
    assert set(colors)==set(positions)
    assert all(a in positions and b in positions for a,b in edges)
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">',
           '<rect width="100%" height="100%" fill="white"/>']
    for a,b in edges:
        x,y=positions[a];u,v=positions[b];cross=colors[a]!=colors[b]
        parts.append(f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="{"#111" if cross else "#aaa"}" stroke-width="{3.5 if cross else 1.3}"/>')
    assert all(sum(colors[a]!=colors[b] for a,b in edges if v in (a,b))==1 for v in positions)
    for name,(x,y) in positions.items():
        if name in ports:parts.append(f'<circle cx="{x}" cy="{y}" r="19" fill="white" stroke="#555" stroke-width="1"/>')
        parts.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{"#333" if colors[name] else "white"}" stroke="#111" stroke-width="1.6"/>')
        parts.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="serif" font-size="15" fill="{"white" if colors[name] else "black"}">{escape(name)}</text>')
    parts.append('</svg>');path.write_text('\n'.join(parts))

names={0:'u',5:'h',9:'A',1:'F',2:'d₁',3:'d₂',4:'d₃',6:'T₁',7:'T₂',8:'T₃'}
r=json.loads((ROUND/'041/result.json').read_text())[0]
edges=[(names[a],names[b]) for a,b in r['edges']]
positions={'u':(210,30),'h':(75,100),'A':(285,100),'F':(75,190),'d₁':(185,190),'d₂':(285,190),'d₃':(385,190),'T₁':(175,290),'T₂':(275,290),'T₃':(375,290)}
colors={names[v]:c for v,c in enumerate(r['cuts'][0])}
draw(HERE/'selector.svg',positions,edges,colors,{'T₁','T₂','T₃'},440,325)

names={0:'u',1:'h',2:'b',3:'t',4:'f',5:'p',6:'r',7:'z',8:'a',9:'v',10:'w',11:'q'}
r=json.loads((ROUND/'028/result.json').read_text())[0]
assert r['variables']==1 and r['occurrences']==1
edges=[(names[a],names[b]) for a,b in r['edges']]
positions={'u':(205,30),'h':(45,100),'b':(175,100),'a':(340,100),'t':(130,190),'f':(35,190),'z':(210,190),'v':(310,190),'w':(400,190),'p':(95,290),'r':(205,290),'q':(365,290)}
colors=dict(u=0,h=1,b=0,t=1,f=1,p=1,r=0,z=0,a=0,v=1,w=0,q=1)
draw(HERE/'variable.svg',positions,edges,colors,{'v','w'},440,325)
print('PASS: diagram adjacency taken from saved gadgets; displayed cuts satisfy all vertices')
