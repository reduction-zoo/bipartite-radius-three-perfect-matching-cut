# Round 025: structural alternatives to synchronization gadgets

## Plan
Status: completed. Action: Investigate literature.
The two synchronization variants now have either a general private-interface
obstruction or a finite shared-template exclusion. Inspect the primary paper's
radius-two algorithm and structural observations, and up to three targeted Web
queries about radius-three PMC, centers with a leaf neighbor, and matching-based
characterizations. Goal: identify a residual constraint system that could guide
a different encoding. Stop after that scope; no fresh broad openness sweep.
Existing center-layer experience is directly relevant and will be compared with
the paper's assumptions. This is a standalone research round.

## Evidence and diagnosis
2026-09-15: inspected Theorem 15 (radius-two matching-cut optimization),
Observations 1–2 and the still distinct PMC target in
https://arxiv.org/html/2501.08735v1 . Queries: "perfect matching cut" "leaf"
"radius"; "perfect matching cut" "center" "matching" bipartite;
"perfect matching cut" "exact cover". Three queries. No ready-made radius-three
residual characterization was found within this coverage. The observations
support color-budget propagation; the radius-two result cannot be asserted for
radius three. Newer similarly named contains-a-cut work was not substituted.
The existing center-edge count gives all L3 vertices color one when the mate is
a leaf. This suggests checking whether the remaining choices reduce to matching,
which would explain why that entire center choice is unpromising for hardness.
## Next action
Derive and check the leaf-center residual matching system. It is an obstruction
analysis for the fixed reduction question, not a replacement campaign theorem.
