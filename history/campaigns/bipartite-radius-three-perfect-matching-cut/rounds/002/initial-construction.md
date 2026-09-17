# Initial construction attempt

Historical account of rounds 001–002; retained with the originating evidence.
See [current state](../../state.md) for subsequent work.

Outcome: no complete rule. The testing foundation passed, two finite synthesis
families were exhausted, and a general obstruction explains the first family.
The fixed Positive NAE-3-SAT to bipartite radius-three PMC target is unchanged.

## Center interface and exact search

Try a shared crossing edge u-h, with u colored zero and h colored one. Their
unique crossing budgets are already consumed by that edge. There are b other
neighbors of u, all forced zero; a second layer A; and three designated ports
in the third layer. In the expanded family there are also t auxiliary vertices
in the third layer. All edges from A to the first and third layers are optional.
Every A vertex must touch the first layer; every third-layer vertex must touch
A. This ensures a connected bipartite graph within distance three of u.

A contains b+t+3 vertices, as required by equal bipartition sizes in a graph
with a perfect matching. The total order is 2b+2t+8. Colors of u,h and the
other first-layer vertices are fixed. For each of the six NAE port assignments,
Z3 chooses colors for A and third-layer auxiliaries. For each of the two
forbidden assignments, the encoding explicitly excludes every internal Boolean
coloring. At every vertex the sum of present opposite-color edges equals one.
The same edge variables occur in all assignments. This is a finite exact
existence test for the specified interface; it does not encode a whole reduction.

The first family fixed t=0 and tested b=0,1,2,3 (orders 8,10,12,14). All four
queries returned UNSAT. The exact script and records were preserved in
../001/ before modifying the family. The fixed center-edge
lemma in [proof.md](../001/fixed-center-proof.md) now explains this failure for every size in that family:
the third-layer zero count is fixed, whereas full NAE requires two counts.

The second family allowed (b,t)=(0,1),(1,1),(2,1),(0,2),(1,2), with orders ten
through fourteen. All five queries returned UNSAT. The script is center_search.py;
its center-search.json and center-search.log preserve results. Both runs exited zero.
No solver or process timeout, random sampling or tuning was used. Each UNSAT
result is trusted solver evidence for the encoding, not a separately checked
proof certificate. The structural lemma does not explain these five exclusions.

## Remaining obligations and next decision

Third-layer auxiliaries are necessary for this fixed-center NAE interface, but
the tested one- and two-auxiliary choices did not suffice. Before expanding sizes,
analyze the residual exact-crossing constraints to identify a specific interface
that can compensate the fixed third-layer color count. Arbitrarily increasing
search size is not the next default action.

A successful local relation would still need variable consistency, radius-safe
occurrence composition, legal outputs for NO sources, both executable maps,
universal recovery, resource bounds and independent review. None of these is
claimed complete. No algorithm.py or publication manuscript is fabricated for
this partial result. The initial finite investigation is finished; the campaign
remains incomplete, with construction feasibility now uncertain.
