# Bipartite radius-four Matching Cut to radius-three Matching Cut

Status: complete argument; executable checks passed and independent review advanced.
Human expert validation remains outstanding.
The predicate throughout is a nonconstant vertex coloring with at most one
opposite neighbor. No perfect-matching condition is used.

## Statement and encoding

For each connected simple bipartite input G of radius at most four, construct a
connected simple bipartite root f(G) of radius at most three such that G has a
matching cut iff f(G) has one. From every valid target witness recover a source
witness deterministically in polynomial time. Invalid source strings map to `{}`,
outside the target language. The precise JSON contract is in `contract.md`.

## Boolean bridge

Use one bit x_v per source vertex. For every vertex b and unordered pair a,c of
its distinct neighbors, prohibit x_a=x_c!=x_b. The two CNF clauses are
(x_a OR NOT x_b OR x_c) and (NOT x_a OR x_b OR NOT x_c).
These are equivalent to saying no source vertex has two opposite neighbors.
Add OR_v x_v and OR_v NOT x_v to require both colors.

For a clause with k>3 literals, replace its first two literals l1,l2 by a fresh
chain bit z: emit (l1 OR l2 OR z) and continue with (NOT z,l3,...,lk). Repeating
produces three-literal clauses. If the original clause is true, choose each z
to indicate that the prefix processed so far is false. Conversely, resolution
on the fresh chain bits shows every satisfying extension satisfies the original
clause. Clauses of length one or two repeat their final literal to length three.
This preserves their truth condition. Repetition is permitted in the later signed
exact-one constraints because distinct selector vertices can attach to the same
variable port without creating parallel edges.

For each three-literal OR(l1,l2,l3), introduce fresh s1,s2,s3,t1,t2,t3. Emit
E(s1,s2,s3) and E(si,NOT li,ti) for i=1,2,3, where E means exactly one true
literal. Algebraically, ti=li-si, so si<=li. Exactly one selected literal is true.
Conversely, choose the first true literal, set its selector to one, all other
selectors to zero, and set ti=li-si. Fresh variables make clauses independent.
The bridge is standard and is not claimed as novel.

## Reservoirs and fixed colors

Start with reservoirs U=K3,3 on sides {0,1,2}/{3,4,5} and W=K3,3 on sides
{6,7,8}/{9,10,11}, joined by edge 0-6. Their bipartitions have opposite
orientation: the global first side contains U's first side and W's second side.

Every K3,3 is monochromatic in every matching cut, including after attachments.
If one side contained two colors, its majority color occurs at least twice;
every vertex on the other side must have that majority color, else it has two
opposites. The minority vertex on the first side would then have three opposites.
Thus each side is monochromatic, and their colors agree because opposite sides
otherwise give three opposites per vertex. Restricting a full coloring to the
reservoir preserves the at-most-one condition, so attachments cannot defeat this.

A vertex adjacent to two reservoir vertices must have their common color,
regardless of any further edges. Normalize U's color to zero. We will prove
that every nonconstant target coloring has W color one.

## Binary block

For every encoded Boolean variable create f,p,r,z,a,v,w,q, with edges
f-6,f-7,z-3,z-4,a-0,a-1,q-9,q-10,
fp,fr,zp,zr,av,aw,qv,qw,pv,rw.
The first eight edges force f,q to W's color and z,a to U's color.
If U=0,W=1, each of p,r sees f=1,z=0, and each of v,w sees a=0,q=1.
All four therefore already spend their crossing budget. Edges pv,rw imply
p=v and r=w. The bounds at a and q imply that exactly one of v,w is one.
Thus p=v represents a free bit and r=w its complement. Conversely either bit
extends legally by those fixed colors. Both occurrence ports v,w are saturated,
so any further incident edge must be monochromatic. The same holds for p,r.

If U=W=0, then f=z=a=q=0. A one on p or r would see two zero neighbors f,z;
a one on v or w would see a,q. Consequently every binary vertex is zero.
Complementing handles the other common reservoir color.

## Selector block

For every signed exact-one triple create F,A,d1,d2,d3,T1,T2,T3. Add
F-6,F-7,A-0,A-1, A-di and F-Ti for i=1,2,3, and di-Tj for i!=j.
The two-neighbor attachments force A=U and F=W. At the high ports Ti we permit
arbitrary external attachments; all bounds below use only internal neighbors.

Assume U=0,W=1. The bound at A permits at most one one among the di. If all di
were zero, each Ti would have to be zero: a one sees two zero d-neighbors.
But then F would have three opposites. Therefore exactly one di, say dk, is one.
Its edge to A spends its budget, forcing Tj=1 for j!=k. For j!=k, vertex dj=0
already sees one of those one-colored high ports and therefore forces Tk=0.
Thus Ti=1-di. Each high port has exactly one internal opposite: Tk sees F,
and each other Tj sees the remaining zero d-neighbor. High ports are saturated.
All private vertices satisfy the bound, and every one-hot choice extends.

If U=W=0 and some di were one, its opposite A would force both other high
ports to one, contradicting the bound at F=0. Hence all di are zero, and any
one-colored Ti would have three zero neighbors F and its two d-neighbors.
Every selector vertex is therefore zero. Again color complementation is valid.

These are newly checked at-most-one arguments. The previous exact-one PMC
selector was a design lead, not an assumed theorem under a different predicate.

## Attachment and general equivalence

For the ith literal of each signed exact-one triple, attach Ti to the binary
port w if that literal is positive, and to v if it is negative. When reservoirs
differ, this port has the complement of the literal's value. Saturation forces
the attachment monochromatic, so di is exactly the literal value. The selector
therefore enforces the triple's exact-one condition. Repeated literals still use
distinct Ti and private cores, so no edge is repeated. Any number of clauses can
reuse a variable's occurrence ports; all attachments are monochromatic.

A satisfying source matching cut extends through the Boolean bridge. Color U=0,
W=1, each binary block by its encoded bit, and each selector by its unique true
literal. All attachment edges are monochromatic. Inside reservoirs all edges
are monochromatic, and the single edge 0-6 is the only opposite edge incident
to either endpoint. All other reservoir vertices have zero opposites, which is
allowed. Thus the target has a nonconstant matching cut.

Conversely, take any nonconstant target matching cut. The reservoirs are
monochromatic. If their colors agreed, the same-color arguments for the binary
and selector blocks would force every private vertex to that same color, a
contradiction. Normalize U=0,W=1 by complementing if necessary. The binary and
selector relations and saturated attachments then give a satisfying signed
exact-one assignment. Projecting through the bridge gives a nonconstant source
matching cut. The executable returns p_i XOR color(0) for each original source
vertex i. Its fixed position is 13+8i, since reservoirs precede binary blocks.
This applies to every valid target witness, not only a chosen extension, and
requires no source-solving oracle or state from the forward call.

For the singleton source, output K3,3, a legal radius-two NO target by reservoir
rigidity. It has no target witness, so no recovery obligation. Invalid source
encodings map to `{}`. All other legal sources use the construction above.

## Target structure and radius

The first bipartition side contains reservoir vertices {0,1,2,9,10,11}, binary
vertices f,z,v,w, and selector vertices F,d1,d2,d3. The other side contains all
remaining vertices. Every listed edge, including every literal attachment,
joins opposite sides. Private labels and distinct terminal vertices guarantee
simplicity. Each block is connected to the reservoirs, which are joined by 0-6;
the root is connected even for NO sources.

Distances from vertex 0 are at most these bounds: U's other first-side vertices
are at distance two and its second side at distance one; vertex 6 is at one,
W's vertices 9,10,11 at two, and 7,8 at three. In a binary block, a is at one;
f,z,v,w at two; p,r,q at three. In a selector, A is at one, F and all di at two,
and all Ti at three. Therefore eccentricity(0)<=3 on every legal output.
This proof uses only listed paths, so extra literal edges cannot invalidate it.

## Determinism and resource bounds

For n>=2 let T=sum_b binom(deg(b),2), Z=2 max(n-3,0), and
C=2T+2 max(n-2,1). The three-CNF instance has C clauses and n+Z variables.
The exact-one instance has N=n+Z+6C variables and K=4C clauses. The output has
exactly 12+8N+8K vertices and 19+18N+19K edges. Since T=O(n^3), both are O(n^3),
with O(n^3 log(n+1)) output bits. Recovery outputs n bits.

The implementation orders vertices, source neighbor pairs, auxiliaries and
clauses deterministically. It uses only Python's standard library. Before
allocating n vertices it rejects n>2m+1, where m is the listed edge count, a
necessary condition for connectedness. Schema, numeric types, duplicate edges,
bipartiteness, connectivity and existence of a center of eccentricity at most
four are checked explicitly. Invalid JSON and excessive nesting map to `{}`;
integer parsing has no decimal digit cap. No source property is checked by
an oracle. A direct BFS from each possible center gives polynomial domain testing.
A conservative bound for all parsing, integer/set operations, graph validation,
Boolean construction and serialization is O((L+1)^5) bit operations for encoded
input length L. Here n=O(L) whenever allocation occurs; worst-case dictionary
comparisons may be charged polynomially, with no expected-time assumption.
Recovery, including reading its full input, is polynomial in the source plus
witness encoding length and uses O(n) indexed selections. JSON decimal numeral
syntax is polynomially equivalent to the binary-integer size convention.

## Novelty and significance boundary

Lucke, *Matching Cut and Variants on Bipartite Graphs of Bounded Radius and
Diameter*, TCS 1052 (2025), 115429, https://arxiv.org/html/2501.08735,
Table 1 and Section 5 Open Problem 1, records Matching Cut hardness at radius
four, tractability at radius two, and explicitly asks the radius-three case.
Source hardness also follows from the cited bipartite diameter-four hardness.
The proposed result would close this bipartite radius boundary. The previous
local PMC campaign and the line-graph result concern different predicates or
restrictions and do not imply it by identity. Clique/biclique rigidity and the
Boolean encodings are known techniques, not novelty claims.

Search date 2026-09-15: `"Matching Cut" "radius three" bipartite 2026`,
`"Matching Cut" "radius 3" 2026 bipartite`. The primary HTML was read at its
Table 1, definitions and conclusion. No exact later resolution was located;
unpublished, unindexed or overlooked work remains outside coverage. The independent complete-rule review advanced after separately assessing
correctness, novelty and significance; human expert validation remains outstanding.
