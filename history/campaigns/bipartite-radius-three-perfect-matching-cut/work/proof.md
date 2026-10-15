# Positive NAE-3-SAT to bipartite radius-three Perfect Matching Cut

Status: native independent review advanced on 2026-09-15; expert assessment pending.
See [complete review](../reviews/complete-rule/review.md) and
[parser follow-up](../reviews/parser-followup/review.md).
Implementation: [algorithm.py](algorithm.py). The source and target are fixed by
[contract.md](contract.md). Colors are bits; a perfect cut has exactly one
opposite-colored neighbor at every vertex. Complementing every color preserves
validity, so normalize the distinguished vertex u to zero.

## Source encoding

Write E(l1,l2,l3) for exactly one true signed literal. Replace each positive
NAE clause (a,b,c) by OR(a,b,c) and OR(not a,not b,not c). For each OR(l1,l2,l3),
introduce fresh selectors s1,s2,s3 and slack bits t1,t2,t3, and require
E(s1,s2,s3) and E(si,not li,ti) for i=1,2,3.
The latter equation is si + (1-li) + ti = 1, hence ti=li-si and si<=li.
Exactly one selector is true, so its literal is true. Conversely, select the
first true literal and set ti=li-si. This extends every satisfying OR assignment.
Fresh variables make the two encodings and all source clauses independent.

For n original variables and m clauses, the signed exact-one instance has
N=n+12m variables and C=8m clauses. Restricting any satisfying extension to the
first n variables satisfies the original NAE formula. This is a supporting
Boolean encoding; no originality is claimed for it.

## Graph construction

Start with vertices u,h,b,t and edges uh,ub,bt. For each of the N encoded variables,
add f,p,r,z,a,v,w,q with edges
hf, fp, fr, zb, zp, zr, ua, av, aw, qv, qw, pv, rw, za.
The bit is represented by p and its complement by r; v,w are occurrence ports.
Each variable has just one pair, reused across all clauses.

For each signed exact-one clause, add F,d1,d2,d3,T1,T2,T3,A with edges
hF, uA, FT1, FT2, FT3, Ad1, Ad2, Ad3, and diTj for i!=j.
If its ith literal is the positive variable x, add Ti-w_x; if it is negative,
add Ti-v_x. All vertices in different blocks are distinct except the named
shared u,h,b,t. These are exactly the edges emitted by algorithm.py.

## Robust selector lemma

Consider one clause block together with u,h and uh. Allow at most one internal
opposite neighbor at u,h,T1,T2,T3; require exactly one at F,A,d1,d2,d3.
These premises hold on restriction of any perfect cut of the full graph.
Assume u=0. If A=1, the crossing edge Au forces all di=1. Each di then requires
exactly one zero among the other two T vertices. Summing these three equations
gives twice the number of zero T vertices equal to three, impossible. Thus A=0.

Exactly one di, say di*, is one, because A must have exactly one opposite
neighbor. Its crossing edge to A forces Tj=1 for j!=i*. Each remaining dj=0
then forces Ti*=0, since its other T neighbor is one. Vertex F cannot be zero:
it already sees two one-colored T vertices. Therefore F=1, and its unique
opposite neighbor is Ti*, so h=1. The three T vertices are internally saturated:
Ti* has F as its opposite neighbor; each other Tj has the remaining zero d
neighbor. Thus di is one-hot and Ti=1-di, and every external edge incident to
Ti must be monochromatic. The selector also forces uh to cross. Conversely,
any one-hot tuple extends in exactly these colors and satisfies all internal
requirements; u and h use only uh as a crossing edge.

## Binary variable lemma

Assume u=0,h=1. They already spend their crossing budgets on uh, so a=0,f=1
in every variable block. The leaf t makes bt a crossing edge; b must therefore
be zero and z=0. The occurrence vertices v,w have internal crossing counts at
most one. If q=0, a vertex among v,w colored one would see both a and q as
opposite neighbors. Hence both would be zero, leaving q without an opposite
neighbor. Thus q=1. Each occurrence now spends exactly one crossing on a or q.
The edges pv,rw must be monochromatic, including in arbitrary full extensions.
Vertex a, whose other neighbors u,z are zero, forces exactly one of v,w to be
one. Therefore p=v and r=w=1-p.

Conversely any bit p extends by these colors, with q=f=1 and z=a=b=u=0,
h=t=1. Vertices p,r each see f=1,z=0 and their equal-colored occurrence; z sees
exactly one opposite neighbor among p,r. All budgets are satisfied. Any number
of monochromatic attachments at v,w preserves them.

## Equivalence and witness recovery

For m>0 there is a selector, so its lemma forces uh to cross in every perfect
cut. The variable lemma applies to every block. A clause attachment equates Ti
to the complement of its signed literal value. Since Ti=1-di, the literal value
is di. The selector's one-hot relation gives the required signed exact-one clause.
The source encoding therefore recovers a valid NAE assignment from any perfect
cut by reading the first n variable p colors relative to u.

Conversely, extend a satisfying NAE assignment using the deterministic source
encoding, color each binary block, and color every selector using its unique
true literal. All attachments are monochromatic. Shared vertices u,h spend
only uh as a crossing edge, while b spends only bt; every private vertex has
exactly one opposite neighbor. This gives a perfect cut of the emitted graph.
This proves both YES and NO directions, not just validity of selected witnesses.

In the implementation, u has label 0 and p_i has label 5+8i. Thus recovery returns
y[5+8i] XOR y[0], for 0<=i<n, after checking the target witness. No source solving
is performed. Reconstructing the graph from the input makes recovery independent
of prior process state.

## Target domain and bounds

Give u distance layer 0; h,b and every a,A layer 1; t and every f,z,v,w,F,di
layer 2; every p,r,q,Ti layer 3. Every edge connects adjacent layers, and every
listed vertex has a path to u of at most its layer number. In particular, all
clause attachments join layers 3 and 2. This proves connectedness, bipartiteness
by layer parity, and radius at most three. Distinct private labels and distinct
ports in each block prevent loops and duplicate edges.

For m>0 the output has exactly 4+8N+8C=4+8n+160m vertices and
3+14N+17C=3+14n+304m edges. The construction uses O(n+m) graph operations and
O((n+m)log(n+m+1)) output bits. All loops and labels are explicit in the code.
Including input parsing and integer validation, a conservative bound is O(L^2)
bit operations for forward construction, where L is the encoded source length;
the explicit variables list ensures n=O(L). Recovery reconstructs the graph,
checks each edge once and reads n ports. It takes polynomial time, bounded by
O((L+|y|)^2) bit operations, with O(n) output bits. No randomness or solver calls
occur in either map.

For empty formulas, return K2 and recover n zero bits. Malformed source encodings
map to C6. This cycle is a connected bipartite radius-three NO instance: crossing
edges would form a perfect matching of three edges, but every cut meets a cycle
in an even number of edges. Malformed recovery inputs fail explicitly. These
cases make the forward map total without changing the source language.

## Evidence boundary

Rounds 041–048 contain synthesis, exhaustive local checks, composition checks
and the first prepared full-rule run. They support implementation consistency;
the general argument above is separate from finite evidence. Novelty and
significance require primary-literature assessment, and the complete candidate
requires independent review before any discovery claim.
