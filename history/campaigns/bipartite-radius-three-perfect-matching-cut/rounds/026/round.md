# Round 026: residual choices with a leaf-saturated center

## Plan
Status: completed. Action: Investigate.
Use the shared fixed-center lemma: a leaf mate implies every L3 color is one,
while other L1 vertices are zero. Hypothesis: a coloring of L2 reduces to assigning
flexible vertices to their unique L1 or L3 neighbor, with unit residual demands.
Derive a matching/flow construction and compare it with the exact PMC oracle for
all connected bipartite atlas graphs through order seven, every eccentricity<=3
center with a leaf neighbor. Recover and directly validate each resulting coloring.
No new reduction candidate is claimed; a tractable restricted interface would
rule out using this center restriction for hardness unless P=NP. Author-side only.

## Evidence and diagnosis
121 center/mate cases / 121 exact-oracle queries; all decisions agreed, eight
recovered witnesses passed direct validation. The general residual argument:
L2 color one is possible exactly when it has one K neighbor; color zero exactly
when it has one L3 neighbor. A forced choice subtracts one from the demand of
that crossing neighbor. A flexible vertex has one neighbor of each type and
chooses which endpoint receives its crossing edge. Match each flexible vertex
to an endpoint with residual demand one; negative demands or unmatched vertices
reject. Integral unit flow is equivalent in both directions and recovers all
colors. The network has O(n+m) size and ordinary max-flow is polynomial. The
all-L3-one premise is the earlier lemma. Author-side, no novelty assessment.
## Next action
To retain a hardness mechanism, allow nonempty F and variable L3 colors. Try an
explicit binary port pair with a color-one F vertex instead of a leaf center.
