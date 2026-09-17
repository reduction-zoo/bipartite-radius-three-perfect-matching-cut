# Round 008: assignment-dependent crossing neighbor of the center

Status: completed; declared before execution.
Hypothesis: fixing a common center edge in every coloring is stronger than the
original target requires. Let the unique crossing neighbor vary with the NAE
assignment, avoiding that premise of the stored center-edge lemma. Pin only
center color zero; all first-layer colors are free, subject to exact-one crossing.
Use three L2 logical ports. Test (L1,L3)=(3,2),(3,3),(4,2), orders 10,12,12.
Set |L2|=|L1|+|L3|-1 for equal bipartition sizes. All center-L1 edges are fixed;
L2-L1/L3 edges are optional subject to distance requirements. Up to eight candidates
per template, whole-boundary exclusions, exact NAE projection. No timeouts.
A successful gadget cannot simply share centers across clauses: center crossing
budgets and the final radius would still require proof. No target change is made.

Result: all three declared templates returned UNSAT on the positive extensions
alone (three synthesis queries, zero graphs). Allowing the crossing neighbor to
vary did not suffice at these sizes with all logical ports in L2 and center
color zero. This does not exclude mixed-layer ports or phase-dependent relations.
Next test mixed L2/L3 interfaces, retaining the same target problem.
