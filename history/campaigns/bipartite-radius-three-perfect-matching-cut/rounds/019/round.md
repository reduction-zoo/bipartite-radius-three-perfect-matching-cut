# Round 019: synchronized double cover and its distance cost

Status: completed; declared before execution.
Action: Continue the complete transformation prerequisite. Add round 018's
synchronizer between every pair v0,v1 in the double cover. Forward coloring
duplicates each original color; recovery reads v0. Derive YES/NO and universal
recovery under the synchronizer proof, then test every connected atlas graph
of order two through six with the prepared oracles. Query also for a target
witness whose decoded original coloring is invalid. Record actual source and
target radii. Scope: these atlas graphs only, three solver queries each.
The fixed campaign endpoints remain Positive NAE-3-SAT to radius-three PMC;
this intermediate transformation is not a completed campaign rule. End with
correctness evidence and the unresolved radius bound or a counterexample.

Result: 142 graphs and 426 solver queries. Decisions agreed on all pairs; every
query for an invalid decoded target witness was UNSAT. Every output is connected
and bipartite. All 142 outputs violate radius <=3, with maximum radius six;
even the source K2 produces radius four. See result.json and check.log.

Author-side general correctness argument: each synchronizer is monochromatic
on its K2,3 by round 018. Its twins therefore agree and spend no crossing
budget internally; each twin must have exactly one crossing edge to an original
neighbor's copy. Reading either twin recovers a perfect cut of the source.
Conversely duplicate a source coloring, give the three biclique auxiliaries its
vertex color and their leaves the opposite color. This gives exactly one crossing
at every vertex. For a connected n-vertex source (n>=2), twin edges connect the
cover's components. The construction has 8n vertices and 2m+9n edges, takes
O(n+m) word operations and O((n+m)log(n+1)) output bits; recovery is O(n).
This auxiliary correctness argument has no independent review or novelty claim
and does not satisfy the campaign's radius requirement or fixed source endpoint.
Next diagnose whether the radius failure is inherent to this private synchronizer,
instead of varying the base graph or growing the gadget without evidence.
