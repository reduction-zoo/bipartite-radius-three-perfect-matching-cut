# Round 009: logical ports in both bipartition classes

Status: completed; declared before execution.
Hypothesis: placing all logical ports on one bipartition side may impose an
unnecessary capacity constraint. Test two L2 ports plus one L3 port, and one
L2 port plus two L3 ports, for (L1,L3)=(2,3),(3,3), graph orders 10 and 12.
Keep center color zero but do not fix its crossing neighbor. Other vertices
are auxiliary, all crossing budgets are one. Optional edges and whole-boundary
exclusion follow round 008. Four templates, at most eight candidates each;
stop on exact local relation or finite exhaustion. No timeouts. A mixed-side
interface needs separate variable wiring and radius proofs if it succeeds.

Result: all four templates returned UNSAT: five synthesis queries, one candidate
and one bad-witness oracle query. The (3,3,2) template admitted all positive
patterns but also an unwanted pattern. Other templates failed positive constraints.
Evidence: search.log and result-*.json; no repairs or reruns. Propose only.
Next test whether center-independent completeness is too strong, using the
previously checked cube relation as a diagnostic baseline.
