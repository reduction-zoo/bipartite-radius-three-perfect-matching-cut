# Balanced reservoirs for Disconnected Perfect Matching

Status: complete proof; independent review advanced without repair. Human expert
validation remains outstanding.

## Fixed statement

Construct a deterministic polynomial-time Karp map from connected simple bipartite
radius-at-most-four Disconnected Perfect Matching to the same language at radius
at most three. A witness is a perfect matching M with G-M disconnected. Recover
such a source matching from every valid target matching. The graph and witness
JSON encodings are in contract.md. Invalid source encodings map to {}; the legal
singleton (a NO input) maps to K3,3, which has no matching cut and hence no DPM.

## Source formula

For legal connected inputs with n>=2, order edges (u,v) lexicographically.
Use n vertex-color bits x_v, followed by m edge-selection bits h_e.
For every vertex v, impose OR_{e incident v} h_e and all pairwise clauses
(NOT h_e OR NOT h_f) on distinct incident edges. Every incident list is nonempty.
Thus the selected edges form a perfect matching. For each edge e=uv, impose
(h_e OR NOT x_u OR x_v) and (h_e OR x_u OR NOT x_v), expressing that every
crossing edge is selected. Finally require OR_v x_v and OR_v NOT x_v.

A satisfying assignment supplies a perfect matching containing the whole
nontrivial cut, so deleting it disconnects G. Conversely, given any DPM witness,
color the component of vertex zero in G-M zero and all other components one.
No unselected edge crosses that cut, so this coloring and the matching bits
satisfy the formula. This equivalence accounts for matchings with more than two
deletion components. The source formula, not a Matching Cut identity, is needed:
P3 and the stored eight-vertex leaf example have Matching Cuts but no DPM.

Convert long clauses to 3-CNF by repeatedly emitting (l1 OR l2 OR z) for fresh z
and continuing on (NOT z,l3,...,lk); short clauses repeat the final literal.
Set chain bits to indicate a false processed prefix for a constructive extension;
resolution eliminates them in the reverse direction. For each three-literal OR,
introduce fresh s1,s2,s3,t1,t2,t3 and exact-one constraints E(s1,s2,s3) and
E(si,NOT li,ti) for i=1,2,3. Their equations give ti=li-si and si<=li. Selecting
the first true literal supplies the extension; a selected literal must be true
in every solution. These standard Boolean conversions are not novelty claims.

## Graph construction

The binary and selector topology comes from the preceding local Matching Cut
campaign; its full argument is restated here with the changed reservoirs.
Reservoir U has sides {0,1,2,u*}/{3,4,5}; W has sides {6,7,8,w*}/{9,10,11}.
Each induces K4,3; add edge 0-6. The two new vertices u*,w* are labeled after
all private blocks, so the previous twelve reference labels and binary positions
are unchanged. There are no further edges at u*,w*.

For each encoded variable i, introduce private f,p,r,z,a,v,w,q in that order,
with labels 12+8i through 19+8i. Add
f-6,f-7,z-3,z-4,a-0,a-1,q-9,q-10,
fp,fr,zp,zr,av,aw,qv,qw,pv,rw.

For each signed exact-one clause introduce private F,A,d1,d2,d3,T1,T2,T3.
Add F-6,F-7,A-0,A-1, A-di and F-Ti for all i, and di-Tj for all i!=j.
Attach Ti to the corresponding variable's w port for a positive literal and
v port for a negative literal. Every high port is distinct even when literals
repeat. The private vertices of different blocks are distinct. All old reservoir
and anchor edges are shared only as explicitly specified.

## Necessary Matching Cut relations

A cut contained in a perfect matching has crossing degree at most one. Every
embedded K3,3 is monochromatic under this predicate: a mixed side has a majority
of at least two, forcing the other side entirely that color, after which its
minority vertex has three opposites. Uniform sides must agree as well. Additional
edges preserve this necessary implication. Each new reservoir vertex sees three
old vertices of its reservoir and must have their color. Thus both K4,3 reservoirs
are monochromatic. An anchor with two distinct neighbors in a reservoir has its
color. Normalize U=0.

When W=1, binary anchors f,q equal one and z,a equal zero. Each p,r sees one
anchor of each color, as does each v,w. Each has already one opposite neighbor;
the edges pv,rw are therefore monochromatic. Bounds at a and q force v,w to
have opposite colors. Exactly two states are possible: p=v=b and r=w=1-b.
All eight binary vertices have exactly one internal opposite neighbor. In
particular occurrence ports are saturated, and arbitrarily many external edges
are permitted precisely when all are monochromatic.

For a selector with U=0,W=1, anchors A=0,F=1. At most one low vertex di can
be one by the bound at A. If all were zero, each Ti would have to be zero to
avoid its two zero low neighbors, giving F three opposites. Hence a unique dk
is one. Its edge to A forces Tj=1 for j!=k. For each j!=k, vertex dj=0 then
has one opposite among those high ports, forcing Tk=0. Thus Ti=1-di. Each Ti
has exactly one internal opposite: Tk sees F, while each other high port sees
the remaining zero low vertex. All other selector vertices also have exactly
one internal opposite (A sees dk, F sees Tk, dk sees A, and each other dj sees
one high vertex). Each one-hot assignment extends legally.

If both reservoirs are zero, every binary private vertex is zero by the two
same-colored anchor neighbors. In a selector, any di=1 would force the two other
high vertices to one, contradicting the bound at F=0. Thus all low vertices,
then all high vertices, are zero. Complementation covers the common color one.
Consequently any nonconstant matching cut of the whole graph has opposite
reservoir colors. Its saturated literal attachments imply that each di equals
its signed literal value: the attached variable port and Ti both have the
complementary value. This gives a satisfying exact-one assignment, and then a
satisfying source formula, for every nonconstant target matching cut.

## Perfect-matching extension and equivalence

A satisfying source formula extends to the exact-one assignment, then the graph
coloring above with opposite reservoirs. Each private vertex has exactly one
opposite private neighbor: all anchor-to-reservoir edges and literal attachments
are monochromatic. The only crossing edge at any reservoir vertex is 0-6.
Thus the crossing edges form a matching covering all private vertices and 0,6.
After removing these endpoints, the vertices of U remaining are
{1,2,u*}/{3,4,5}, and those of W are {7,8,w*}/{9,10,11}. Match them by
1-3,2-4,u*-5 and 7-9,8-10,w*-11. These are monochromatic edges, disjoint from
all crossing edges. Their union with the crossing edges is a perfect matching.
It contains the nontrivial cut, so its deletion disconnects the target.

Conversely, take any target perfect matching M whose deletion disconnects the
constructed graph H. Let S be the component of zero in H-M. Color S zero and
V(H)-S one. This is nonconstant and every crossing edge lies in M, so crossing
degree is at most one. The preceding necessary relations apply to this cut
regardless of how many components H-M has, or which monochromatic edges M uses.
The binary values therefore satisfy the source formula. Return exactly those
lexicographically ordered source edges e_j whose binary port p at
13+8(n+j) is outside S. The formula ensures these edges form a perfect matching
and contain every edge of a nontrivial source cut. Its deletion disconnects the
source. This is recovery for every target witness, not only the explicitly
constructed extension. The same implication proves the NO direction.

Both maps run in fresh processes. Recovery recomputes H from the source, removes
the supplied matching, and runs BFS from zero. It does not call a source solver.
The matching witness contains only edges, so the cut is reconstructed explicitly.

## Structural and resource bounds

The bipartition's first side is {0,1,2,u*,9,10,11}, binary f,z,v,w, and selector
F,d1,d2,d3. All other vertices, including w*, are in the other side. Every edge
listed crosses these sides. Distinct labels and ports prevent loops and duplicates.
Every block connects to the joined reservoirs, so outputs are connected.

Distances from zero: 3,4,5 and 6 at one; 1,2,u*,9,10,11 at two; 7,8,w* at three.
For each binary block a is at one, f,z,v,w at two, and p,r,q at three.
For each selector A is at one, F,di at two, and Ti at three. Literal edges only
shorten distances. Thus all outputs, including those of legal NO sources, have
radius at most three. The singleton's K3,3 has radius two.

For n>=2, put B=sum_v binom(deg(v),2),
Z=sum_v max(deg(v)-3,0)+2max(n-3,0), and
C=sum_v max(deg(v)-2,1)+B+2m+2max(n-2,1).
The 3-CNF has n+m+Z variables and C clauses. The signed exact-one instance has
N=n+m+Z+6C variables and K=4C clauses. The graph has exactly 14+8N+8K vertices
and 25+18N+19K edges. Since m=O(n^2) and B=O(n^3), both are O(n^3); output
integer endpoint encodings take O(n^3 log(n+1)) bits. Recovered matching size is
n/2 edges, encoded in O(n log(n+1)) bits.

Source validation is the same explicit standard-library schema and graph-domain
validation as the previous rule: require exact integer types, ordered unique
edges, bipartiteness, connectivity and a BFS center of eccentricity at most four.
Before allocation reject n>2m+1. Invalid JSON/excessive nesting map to {}, while
integer parsing has no decimal digit cap. On allocated inputs n=O(L), where L is
source encoding length. A conservative O((L+1)^5) bit-operation bound covers
parsing, worst-case dictionary/set comparisons, BFS, clause generation and output.
Recovery reconstructs this same polynomial graph, parses the full witness and
uses polynomially many integer/set operations and BFS steps. A conservative
O((L+Y+1)^5) bit bound holds for witness length Y under the promised-valid-witness
contract. There is no randomized runtime, solver call, hidden state or oracle.

## Novelty and significance

Lucke, Matching Cut and Variants on Bipartite Graphs of Bounded Radius and
Diameter, TCS 1052 (2025), 115429, https://arxiv.org/html/2501.08735, Table 1,
Corollary 17 and Section 5 Open Problem 1, records the radius-two tractability,
radius-four hardness and asks exactly the radius-three DPM case. The source is
therefore NP-hard; target membership in NP follows by matching and connectivity
checks. The rule would establish NP-completeness at radius three.

The new ingredient relative to this repository's Matching Cut rule is a residual
matching extension by two enlarged reservoirs, plus a source encoding and recovery
for actual matching witnesses. The interface topology and Boolean conversions
are reused, not independent discoveries. This is a closely related classification
extension, potentially part of the same paper, not claimed as an unrelated result.
Matching Cut or PMC identity substitution is invalid on general source instances.
The published maximum-size DPM optimization hardness is not this decision case.

Search date 2026-09-15: exact radius-three and radius-3 DPM queries plus the primary
HTML locations above. No exact later resolution was located within coverage.
Unindexed, unpublished and overlooked work remains possible. The [independent review](../reviews/complete-rule/review.md) assessed correctness,
novelty and significance and confirmed source hardness directly in Bouquet and
Picouleau, https://arxiv.org/pdf/2011.03318v2, Section 2 (DPM definition),
Theorem 3.3 (bipartite diameter-four hardness). Human review remains outstanding.
