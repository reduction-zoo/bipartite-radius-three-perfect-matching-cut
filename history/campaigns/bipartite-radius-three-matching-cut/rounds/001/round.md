# Round 001 — Full reservoir composition

## Plan

Allocation: 40 rounds. This is the first campaign round; prior topic-selection
probes are separately recorded and are not counted as campaign attempts.
Hypothesis: two K3,3 reservoirs, the tested binary blocks and selector blocks
compose into a full Matching Cut reduction at radius three.

Encode the source's neighbor-pair constraints and nontriviality as CNF, replace
long clauses by a standard three-clause chain, then encode each three-literal OR
with signed exact-one triples. Use the independently tested bit/selector blocks;
attach selector high ports to the complement of the corresponding signed literal.
Decode source ports relative to the first reservoir's color. The predicate here
is at most one crossing neighbor, not the previous PMC exact-one condition.

Experience retrieval: read the three-mate-choice selector entry and its original
proof. It supplies a design lead, not an applicable exact-one lemma. Reprove its
at-most-one relation under two reservoirs. The line-graph root edge-color lemmas
do not apply. The original bare-hub P3 counterexample is in the prepared cases.

First discriminating observation: compare actual outputs and recovered witnesses
on all eight prepared cases, especially the NO complete bipartite graphs and
P3. Additional finite verification scope: connected bipartite atlas graphs through
five vertices, four explicit six-vertex inputs, and three fixed radius-four trees.
No random generation, size expansion or timeout. A successful result proceeds to
general proof and independent review; a failure is diagnosed without restarting
preparation. Completion requires full equivalence, nontriviality, bipartiteness,
radius, totality and polynomial construction/recovery bounds.

## Evidence and diagnosis

One complete construction mechanism and one executable Karp pair were evaluated.
The prepared feedback passed eight source cases and twenty recovery calls;
[prepared-check.json](prepared-check.json) is the completed run. The separately
implemented verifier passed eighteen cases (fourteen YES, four NO), with fifty-six
recoveries and maximum output 3628 vertices/8331 edges; see
[verification.json](verification.json). These suites overlap and are not counts
of distinct source graphs. Commands appear in [verification](../../work/verification.md).

The first arithmetic-constraint prepared run was manually interrupted inside Z3,
returning unknown. Preserve [the explanation](arithmetic-interruption.txt),
[original checker](arithmetic-check.py) and [native sample](prepared-sample.txt).
Changing the same predicate to native Boolean cardinality was followed by a
passing [oracle self-test](cardinality-self-test.json) and full prepared rerun.
There was one checker encoding change, one interrupted run, zero candidate
algorithm repairs and no configured timeout. Unknown was not treated as NO.
The execution bottleneck was solver search under that encoding; no mathematical
counterexample or candidate defect was found. Time/token totals are unavailable.

The [general proof](../../work/proof.md) establishes reservoir rigidity,
same-color collapse, saturated-port composition, both implications, universal
recovery, bipartiteness, radius and polynomial bit bounds for arbitrary size.
The [independent review](../../reviews/complete-rule/review.md) advanced without
repair. It enumerated four local settings (256 assignments each), checked three
full outputs, six bounded bad-witness queries (four nonvacuous), four recoveries,
six invalid inputs and the singleton. Its programs import no author checker or
candidate. These finite checks supplement the analytic proof.

The primary-literature audit inspected Lucke's published Table 1/introduction
and the readable arXiv Section 5 Open Problem 1, together with Le and Le's
Section 3 hardness construction. Exact URLs, queries, date 2026-09-15 and access
limits are in the independent review. No later exact resolution was located.
Novelty is supported within that coverage; significance is the bipartite radius
classification boundary. Neither agent agreement nor absent search hits proves
novelty. Human expert assessment is outstanding.

The mechanism succeeds because two distinct reservoir neighbors force anchor
colors without consuming crossing budget in an intended extension. Same-color
collapse excludes spurious local nontrivial cuts, while saturated interfaces
permit arbitrarily many monochromatic literal attachments. The previous PMC
selector supplied a useful topology; its exact-one premise was not reused.
This is a supported general interface argument, not a measured workflow gain.

Experience extraction: saved during post-campaign maintenance after the restricted
research phase. Created [dual-reservoir interfaces](../../../../research/experience/dual-reservoir-matching-cut-interfaces.md)
and updated [selector use history](../../../../research/experience/three-mate-choices-at-radius-three.md).
Searched existing entries before extraction; none stated this at-most-one
reservoir mechanism. One new file, one pre-existing file updated, zero pending.

## Next action

Finish the campaign at ready_for_expert_review: the reviewed pair and proof,
passing evidence, and seven-page English Typst paper with two checked vector
figures are complete. Paper compilation and page inspection are recorded in
[paper-inspection.txt](../../work/evidence/paper-inspection.txt). No new proof
strategy or candidate modification was introduced in writing. One of forty
allocated rounds is complete; thirty-nine remain unused. More discovery on this
fixed target is not justified by a remaining agent-side proof obligation.
The next required assessment is human expert review, whose outcome is unknown;
no calibrated probability is available.

