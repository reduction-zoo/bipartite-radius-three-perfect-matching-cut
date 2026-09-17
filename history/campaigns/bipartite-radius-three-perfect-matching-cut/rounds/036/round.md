# Round 036: does the spectral relaxation lose the sign constraint?

## Plan
Status: completed. Action: Investigate.
Test all connected subgraphs of K3,3. Compare existence of a nonzero real
solution of (L-2I)x=0 with exact PMC, using Z3 rational linear arithmetic and
the prepared Boolean oracle. Scope: all 512 edge masks; report explicit spectral
false positives. The linear identity is exact for sign vectors but the relaxed
condition is only necessary. A false positive would prevent treating eigenvalue
existence as a solved reduction or using it as the target decision oracle.

## Evidence and diagnosis
205 connected graphs / 410 solver queries. Eighteen spectral false positives;
the first is a balanced six-vertex radius-two graph whose real eigenvector has
zeros. The sign restriction is essential. The relaxed eigenproblem cannot
replace the prepared PMC oracle or establish hardness. Explicit graphs and
rational eigenvectors are preserved in result.json.
## Next action
Use the local sign interpretation to test a concrete limitation: can adding
edges while preserving the wire's six intended colorings exclude all-equal inputs?
