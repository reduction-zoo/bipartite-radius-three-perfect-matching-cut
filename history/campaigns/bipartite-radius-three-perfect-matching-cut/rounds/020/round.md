# Round 020: is the private synchronizer itself a radius obstruction?

Status: completed; declared before execution.
Action: Investigate the universal radius failure from round 019. Prove or
refute radius >=4 for every graph produced by that exact transformation on a
connected source with at least two vertices. For any proposed center choose a
different vertex's private synchronizer and compare distances to its two leaf
types. Check the distance identities on the same 142 saved source graphs and
every target center, reusing construction but making no additional solver calls.
End with a general argument or a counterexample; the twenty-round budget then
ends. This diagnoses the current mechanism and does not claim all bipartizations
fail. No independent reviewer is needed before a complete campaign rule exists.

Result: the obstruction holds for the exact round-019 transformation. Check
passed on 142 graphs and all 6472 possible target centers, with zero solver
queries. Proof: let c belong to one source vertex's gadget and choose another
vertex w. External edges of w's gadget meet only terminals w0,w1. Their distances
d0,d1 from c differ by exactly one: they are adjacent and in opposite bipartition
classes. Both are at least one. The private leaf p on the extra left biclique
vertex has distance min(d0+3,d1+2); a leaf q on an extra right biclique vertex
has distance min(d0+2,d1+3). These expressions follow by entering at a terminal;
the internal distances are 3/2 and 2/3 respectively. Their maximum equals
min(d0,d1)+3 >=4. Thus every target vertex has eccentricity at least four.

This is an author-side argument with finite consistency checks, not independent
review or a novelty claim. It excludes the private synchronizer transformation
for this campaign regardless of the base graph's density. It does not exclude
other synchronization gadgets or shared constructions. Stop without discovery:
twenty total rounds are complete, no complete fixed-endpoint reduction exists.

## Assessment of rounds 011–020

Recorded after the ten-round allocation closed.

The new run used 510 solver queries (including 142 searches for an invalid decoded
witness), five Web search queries and 276736 colorings in completed enumerations.
Round 012 also executed 3072 colorings before its conjecture assertion failed;
that counterexample prompted a disclosed same-scope rerun to collect the full
classification. This is a mathematical rejection, not a fixed solver or weakened
oracle. No other failed or repeated execution occurred in these ten rounds.
Radius and boundary checks are not source-to-target acceptance tests. Only round
015 injected the campaign's actual source formulas; it remained a diagnostic
construction and failed. Round 019 checked an intermediate graph transformation,
not a full Positive NAE-3-SAT reduction. All existing preparation was reused.
Wall-clock campaign time and token usage are unavailable; no timeouts were set.

## Observed effect of the revised skill

The action choices are recorded before execution, without predetermined quotas.
Two rounds performed focused literature investigation. The cube mechanism was
modified at its private-leaf assumption after a completeness failure; after
composition failed, work moved to whole-graph bipartization rather than larger
clause gadgets. A false conjecture was retained as a counterexample in round 012.
Local successes in rounds 014 and 018 were followed immediately by composition
checks, exposing both correctness and distance failures.

These are two broad construction mechanisms with several refinements and
diagnostic rounds, not ten independent ideas. In contrast to rounds 004–010's
local template emphasis, this run tested global compositions and did not resume
any previously excluded synthesis template. Some same-family enumeration was
still repeated to answer a new completeness question in round 013; action labels
do not imply absence of repeated work.

This is an observed continuation under the new instructions, not a controlled
comparison. The agent also received the preceding discussion and ten rounds of
accumulated evidence. Action selection cannot be attributed causally to the skill;
no discovery-rate, cost or speed improvement is established. The failed conjecture
also shows that explicit reasoning still needs executable checks. No skills,
runner, search tree or orchestration code were changed during this campaign.

