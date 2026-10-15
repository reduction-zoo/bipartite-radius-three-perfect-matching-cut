# Partial center-layer obstruction

This is a supporting lemma, not a reduction or a resolution of the fixed question.
Its novelty has not been independently assessed.

## Fixed center-edge lemma

Let G be a connected bipartite graph with a vertex u of eccentricity at most
three. Let L_i be the vertices at distance i from u. Fix h in L_1. In any perfect
cut coloring c with c(u)=0 and c(h)=1, define

    K = L_1 minus {h},
    F = {v in L_2 : v is adjacent to h and has no neighbor in K}.

Then exactly |F| vertices of L_3 have color zero. The number is determined by
the graph and chosen center edge uh, not by the remaining coloring choices.

Proof. The edge uh consumes the unique crossing edge of both endpoints.
Every vertex of K therefore has color zero, and every neighbor of h in L_2
has color one. Bipartiteness permits edges only between consecutive distance
layers.

Take a color-zero vertex z in L_3. Its unique opposite neighbor v lies in L_2
and has color one. Vertex v cannot have a neighbor in K, since that would give
it a second opposite neighbor. Every L_2 vertex has a neighbor in L_1, so v
must be adjacent to h and belongs to F.

Conversely, every v in F has color one, has no neighbor in K, and agrees with
h. Its required opposite neighbor must therefore be a color-zero vertex of
L_3. Unique crossing neighbors on both sides give a bijection between F and
the color-zero vertices of L_3, proving the equality.

## Consequences for the attempted interface

If h is a leaf, F is empty: every third-layer vertex has the opposite color
from u. A leaf-saturated center cannot support independently varying third-layer
variable ports.

If L_3 consists of exactly three designated ports and the center edge uh is
fixed as crossing, the projection cannot be the full NAE relation. NAE includes
assignments with one zero and assignments with two zeros, whereas the lemma
forces a fixed zero count. This excludes the entire near-layer-only template,
regardless of its size, subject to the fixed-edge and layer premises.

Extra third-layer auxiliary vertices can absorb the count difference. Thus the
lemma does not exclude the expanded search family or all radius-three
reductions. In particular, it does not justify changing the research question
to a decision algorithm or claiming that hardness is impossible.

## Finite check

`python3 ../rounds/002/obstruction_check.py` independently enumerated perfect-cut colorings
of the bipartite graph atlas through order seven. The lemma passed for 33
feasible ordered center/mate choices and 34 associated colorings, including
nine leaf-mate colorings. These counts are finite consistency checks of the
argument, not its proof and not independent author review.
