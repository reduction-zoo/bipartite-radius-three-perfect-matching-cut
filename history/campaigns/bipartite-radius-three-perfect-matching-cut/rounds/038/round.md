# Round 038: whole-wire edge synthesis with new internal colorings

## Plan
Status: completed. Action: Reconsider.
Keep the three-variable one-occurrence wire topology but permit every missing
bipartite edge. Unlike round 037, positive NAE assignments may use new internal
colorings. Normalize only u=0, not the center mate; project to the three p ports.
Scope: one 28-vertex template, at most eight candidate graphs. Every positive
pattern must extend; each candidate is queried for an all-equal port coloring.
Exclude the actual bad full coloring before the next candidate. Additions preserve
connectivity, bipartiteness and the radius bound. An exact local relation would
still need variable sharing and full-formula validation; a candidate-cap result
is not UNSAT. No larger scope or repeated preparation.

## Evidence and diagnosis
One candidate graph, one explicit all-equal counterexample, then synthesis
UNSAT: three solver queries. This excludes every bipartite edge augmentation
of the declared 28-vertex wire satisfying all six positive extensions, even
when internal colorings may change. It does not exclude deleting edges, adding
vertices, different decoding, or different source normalization. No full rule.
## Next action
Before recommending further exact-one primitive searches, verify that an
explicit source-to-exact-one bridge with universal recovery is available.
