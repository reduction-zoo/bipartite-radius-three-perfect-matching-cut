# Round 003: complementary port pairs

Status: completed — candidate limits exhausted. Scope recorded before execution on 2026-09-14.
Uses the remaining round of the three-round allocation; the fixed Karp endpoints
and complete-rule acceptance criteria are unchanged.

## Retrieved experience and hypothesis

Retrieved [fixed center-edge color count](../../../../research/experience/fixed-center-edge-color-count.md)
by repository search for center, layers and radius. Re-read its proof: the
bijection relies on bipartiteness, eccentricity at most three and exact-one
crossings with fixed center edge uh. These premises apply to the proposed
family. The proof remains author-side, without independent review.

Represent the three clause variables by six third-layer ports
(x,1-x,y,1-y,z,1-z). Every allowed assignment has exactly three zeros, including
all six NAE assignments. This removes the specific varying-count obstruction;
it does not prove realizability. Require exactly three second-layer vertices
adjacent to h and no other first-layer vertex, as dictated by the lemma.

## Declared scope

Two graph templates: one or two ordinary first-layer vertices, six third-layer
ports, no other third-layer vertices, and respectively seven or eight second-layer
vertices. Total orders: 16 and 18. The center edge is fixed crossing; all other
center neighbors have color zero. All second-to-first and second-to-third layer
edges are optional, subject to every second-layer vertex touching the first
layer and every port touching the second. These conditions ensure radius at
most three and bipartiteness. The desired projection contains precisely the six
complementary-pair NAE assignments among all 64 port assignments.

For each template, at most 32 candidate graphs from Z3. Require extensions of
all six positive assignments, then use a separately encoded exact target oracle
to search for a forbidden assignment on the actual graph. Save each counterexample
and forbid its coloring in subsequent synthesis. Stop at a verified exact local
relation, exact synthesis UNSAT, or the stated candidate limit. A limit is not
UNSAT. No timeouts or tuning. If a relation is found, exhaustively enumerate
its colorings and record outstanding composition and recovery obligations.

Reuse the prepared solver and witness predicates; no preparation rerun is needed.
Elapsed experiment time will be measured; token usage is unavailable. Compare
actual design choices with the cited experience, without claiming causal speedup
or cross-task transfer from this single run.

## Results and evidence

Executed `python3 search.py > search.log 2>&1`, exit zero. Both templates reached
32 candidates: 64 graphs, 64 synthesis queries and 64 forbidden-witness queries.
Every graph admitted an unwanted assignment; neither template reached synthesis
UNSAT. Candidate limits are not impossibility certificates. Full graphs and
counterexample colorings are in [result-1.json](result-1.json) and
[result-2.json](result-2.json); [search.log](search.log) records the outcomes.

Executed `python3 check_evidence.py > evidence-check.log 2>&1`, exit zero.
This audit imports the prepared definition-based oracles, not search.py. It
checked all 64 actual target domains and counterexamples, and used 384 additional
solver queries to confirm all six desired extensions for every graph. Direct
predicates validated returned witnesses. All 992 comparisons against earlier
counterexample colorings confirmed that subsequent graphs reject them. Total
solver queries across search and this audit: 512. No oracle or candidate repairs,
command retries, full preparation reruns, or timeouts occurred.

All 64 returned counterexamples have valid complementary pairs but all three
encoded variables equal. Thus the observed failure is residual acceptance of the
two forbidden NAE patterns, not failure to preserve the required three-zero
count in these witnesses. Excluding a specific full coloring can leave other
internal extensions of the same forbidden boundary pattern. The results do not
prove that every graph in either template has that defect, or that every legal
coloring of the sampled graphs satisfies the complementary-pair condition.

Search calls measured 1.720 and 3.907 seconds (5.627 seconds combined). These are
search-function wall times, not total round cost or a comparison with earlier
rounds. Token usage and complete round elapsed time are unavailable.

## Experience effect and stopping decision

The retrieved lemma changed the interface before execution from three single
ports to six complementary ports with invariant color count. Its premises were
rechecked, and it supplied the |F|=3 synthesis constraint. This is an observed
same-topic use of prior experience. It avoided proposing another varying-count
interface; there is no measured speedup, counterfactual baseline, cross-topic
transfer or new reduction success.

Within the round, counterexamples actually constrained later candidates: the
992 replay checks establish this finite behavior. Nevertheless, all 64 candidates
failed the required exact relation. Raw full-coloring exclusions did not remove
all extensions of the repeated forbidden boundary patterns within this budget.
If a future allocation revisits the family, investigate boundary-level exclusion
of all such extensions before increasing the graph or candidate limits.

Three of three rounds are now complete. Stop discovery on this topic under the
current allocation. There is no complete forward/recovery rule, general reduction
proof, independent review or manuscript. The fixed research question remains
unresolved here. The experience use history is updated with this qualified result.
