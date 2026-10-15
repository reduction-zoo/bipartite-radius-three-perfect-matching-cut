# Round 010: assignment-dependent center color

Status: completed; declared before execution.
Hypothesis: a useful NAE interface may require its center color to depend on
its port assignment. Rounds 008–009 required all six patterns at center zero;
this is stronger than an unconditioned NAE relation. Test three L2 ports with
(L1,L3)=(3,1),(3,2), orders 8 and 10, allowing every center color and crossing
neighbor. All vertices retain crossing budget one. Up to eight candidates per
template; stop at the first exact relation or finite exhaustion. No timeouts.
Reuse round 008's solver and whole-boundary exclusion, with the center among
free internal variables. Exhaustively check every coloring of a successful graph,
including its center/port relation. Compare with the cube already documented in
question.md. Rediscovering that baseline is diagnostic, not an original result.
The fixed-edge experience does not exclude this scope: its center-edge premise
is absent. The next observation is whether conditioning the center removes
legal port patterns. No complete reduction or composition is assumed.

Result: the order-eight template produced an exact local relation on its first
candidate (one synthesis query and one forbidden-witness query). The order-ten
template was not executed, following the declared early completion condition.
All 256 colorings were checked; exactly six are perfect cuts. An additional
check using direct neighbor counts, without importing synthesis, confirmed the
relation and graph isomorphism with the cube. At center zero the port patterns
are only 011, 101 and 110. In all six witnesses the center equals the minority
port color. Thus the previous center-independent completeness requirement
excludes this known local baseline. It was an explicit interface premise, not
a conclusion about unrestricted reductions.

Evidence: search.py, search.log, result-3-1.json, and
../../work/audit-rounds.log. No repairs or reruns. Stage reached: Propose, local
relation only. No original construction, composition, forward map or recovery
algorithm has been obtained. The cube is already recorded in question.md;
this run supplies no novelty claim. The allocation is exhausted at ten rounds.
Stop without discovery. A later attempt needs a specific composition mechanism
for assignment-dependent center states and port crossing budgets; rediscovering
this local relation is not sufficient justification for another search.
