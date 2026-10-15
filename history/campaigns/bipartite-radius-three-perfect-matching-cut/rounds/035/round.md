# Round 035: spectral characterization as a construction constraint

## Plan
Status: completed. Action: Investigate literature.
Perfect cuts satisfy a local linear equation when colors are signs: each vertex
has one opposite neighbor. Search at most three queries for the relation to
Laplacian eigenvalue two and restrictions on perfect-cut solution spaces. Read
relevant primary statements. Determine whether the observations in rounds 033–034
have a known explanation or suggest a direct construction formulation. No general
tractability claim or change of target. End after this finite literature scope.

## Evidence and diagnosis
2026-09-15 queries: "perfect matching cut" "eigenvalue"; "Laplacian"
"bivalent" eigenvectors "2"; "perfect matching cut" "radius" "solutions".
Primary source read: Caputo, Khames and Knippel, Nonlinear normal modes in a
network with cubic couplings, AIMS Mathematics 7(12), 2022, Definition 2.2 and
Laplacian definition preceding equation (2.3):
https://www.aimspress.com/aimspress-data/math/2022/12/PDF/math-07-12-1127.pdf .
It defines bivalent eigenvectors with entries +/-1; it does not settle this
radius-three complexity question. Local derivation: for sign vector s,
(Ls)_v = 2 s_v times the number of opposite neighbors, so PMC is exactly
Ls=2s with every coordinate +/-1. This is an equivalent constraint, not a new
algorithm. Ordinary eigenvalue existence drops the sign restriction and may
be insufficient. No primary binary-choice theorem was found within coverage.
## Next action
Check that relaxation before using spectral feasibility to guide construction.
