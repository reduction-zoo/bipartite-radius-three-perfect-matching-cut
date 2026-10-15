# Round 023: obstruction for any private robust equality interface

## Plan
Status: completed. Action: Investigate.
Try to generalize round 020 to a connected bipartite gadget with terminals on
opposite sides, whose admissible local colorings (internal budgets one, terminal
budgets at most one) are exactly equal-terminal colorings with zero terminal
budgets. Hypothesis: every such coloring contains opposite-to-terminal colors
on both bipartition sides. Then any external vertex is at distance at least
four from one of them, when only terminals connect outside. Prove this and
check all twelve round-021 gadgets and every center of round-022 outputs.
No synthesis or solver rerun. A proof excludes this private-interface mechanism,
not shared internal vertices or other witness encodings.

## Evidence and diagnosis
Proof under the declared robust boundary premise: normalize terminal color to
zero. If one bipartition side were all zero, every internal vertex on the other
side must be one. The zero-budget terminal on the all-zero side could then only
be adjacent to the other terminal. Connectedness makes it a degree-one terminal.
Flipping that terminal gives a legal local coloring with both terminal budgets
one and unequal terminal colors, contradicting robustness. Thus each side has a
one-colored internal vertex. Neither can be adjacent to a terminal. For an
external vertex c on side A, an internal one-colored A vertex has distance at
least four: a path entering at terminal A needs at least 2+2 edges; one entering
at terminal B needs at least 1+3. Reverse sides for c on B. With at least two
private gadgets, every center is outside one of them. Radius is therefore >=4.
This argument permits arbitrary edges among terminals but no other external
attachments. It does not require a leaf or a direct terminal edge. Author-side,
not independently reviewed or claimed novel. The checks passed 12 gadgets,
360 outputs and 9864 centers; no additional solver calls.
## Next action
Reconsider private internal vertices: test a shared two-pair synchronizer.

Experience extraction (retrospective, 2026-09-15): created
[Private robust equality synchronizers force radius at least four](../../../../research/experience/private-equality-synchronizers-force-radius-four.md).
This entry was saved after round 040; no earlier retrieval is claimed.
