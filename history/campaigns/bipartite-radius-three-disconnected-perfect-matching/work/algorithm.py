import itertools
import json
import sys
from collections import deque


def source_graph(data):
    if type(data) is not dict or set(data) != {'n','edges'}:
        return None
    n,edges=data['n'],data['edges']
    if type(n) is not int or n<1 or type(edges) is not list or n>2*len(edges)+1:
        return None
    adj=[set() for _ in range(n)]
    for e in edges:
        if (type(e) is not list or len(e)!=2 or any(type(v)is not int for v in e)
                or not 0<=e[0]<e[1]<n or e[1] in adj[e[0]]):
            return None
        u,v=e;adj[u].add(v);adj[v].add(u)
    colors={0:0};queue=deque([0])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if v not in colors:
                colors[v]=1-colors[u];queue.append(v)
            elif colors[v]==colors[u]:
                return None
    if len(colors)!=n:
        return None
    for center in range(n):
        distances={center:0};queue=deque([center])
        while queue:
            u=queue.popleft()
            if distances[u]==4:continue
            for v in adj[u]:
                if v not in distances:
                    distances[v]=distances[u]+1;queue.append(v)
        if len(distances)==n:return adj
    return None


def encode(adj):
    n=len(adj);source_edges=[(u,v) for u in range(n) for v in sorted(adj[u]) if u<v]
    variables=n+len(source_edges);cnf=[];incident=[[] for _ in adj]
    for j,(u,v) in enumerate(source_edges):
        bit=n+j;incident[u].append(bit);incident[v].append(bit)
        cnf.extend([[(bit,True),(u,False),(v,True)],[(bit,True),(u,True),(v,False)]])
    for row in incident:
        cnf.append([(bit,True) for bit in row])
        cnf.extend([[(a,False),(b,False)] for a,b in itertools.combinations(row,2)])
    cnf.extend([[(v,True) for v in range(n)],[(v,False) for v in range(n)]])
    triples=[]
    for clause in cnf:
        while len(clause)>3:
            z=variables;variables+=1
            triples.append(clause[:2]+[(z,True)])
            clause=[(z,False)]+clause[2:]
        triples.append(clause+[clause[-1]]*(3-len(clause)))
    exact=[]
    for clause in triples:
        selectors=list(range(variables,variables+3));slack=list(range(variables+3,variables+6));variables+=6
        exact.append([(v,True) for v in selectors])
        exact.extend([[(a,True),(b,not positive),(c,True)] for a,(b,positive),c in zip(selectors,clause,slack)])
    return variables,exact


def forward(data):
    adj=source_graph(data)
    if adj is None:return {}
    if len(adj)==1:
        return {'n':6,'edges':[[u,v] for u in range(3) for v in range(3,6)]}
    variables,clauses=encode(adj)
    edges=list(itertools.product(range(3),range(3,6)))+list(itertools.product(range(6,9),range(9,12)))+[(0,6)]
    for i in range(variables):
        f,p,r,z,a,v,w,q=range(12+8*i,20+8*i)
        edges.extend([(f,6),(f,7),(z,3),(z,4),(a,0),(a,1),(q,9),(q,10),(f,p),(f,r),(z,p),(z,r),(a,v),(a,w),(q,v),(q,w),(p,v),(r,w)])
    for i,clause in enumerate(clauses):
        f,a,d,e,k,t,s,r=range(12+8*variables+8*i,20+8*variables+8*i)
        low=[d,e,k];high=[t,s,r]
        edges.extend([(f,6),(f,7),(a,0),(a,1)]+[(a,v) for v in low]+[(f,v) for v in high]+[(u,v) for j,u in enumerate(low) for k,v in enumerate(high) if j!=k])
        edges.extend((port,12+8*v+(6 if positive else 5)) for port,(v,positive) in zip(high,clause))
    end=12+8*variables+8*len(clauses)
    edges.extend([(end,i) for i in (3,4,5)]+[(end+1,i) for i in (9,10,11)])
    return {'n':end+2,'edges':[sorted(e) for e in edges]}


def extract(data):
    source,matching=data['source'],data['target_solution']
    target=forward(source);removed=set(map(tuple,matching));adj=[[] for _ in range(target['n'])]
    for u,v in target['edges']:
        if (u,v) not in removed:adj[u].append(v);adj[v].append(u)
    reached={0};queue=deque([0])
    while queue:
        for v in adj[queue.popleft()]:
            if v not in reached:reached.add(v);queue.append(v)
    edges=sorted(map(tuple,source['edges']));n=source['n']
    return [list(e) for j,e in enumerate(edges) if 13+8*(n+j) not in reached]



if __name__=='__main__':
    sys.set_int_max_str_digits(0)
    try:
        data=json.load(sys.stdin)
    except (json.JSONDecodeError,RecursionError):
        if '--extract' in sys.argv:raise
        print('{}')
    else:
        print(json.dumps(extract(data) if '--extract' in sys.argv else forward(data)))
