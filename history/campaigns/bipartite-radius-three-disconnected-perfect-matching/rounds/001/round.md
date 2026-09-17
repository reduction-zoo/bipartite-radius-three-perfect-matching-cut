# Round 001 — Balanced reservoirs with matching-variable recovery

## Plan

User allocation: 40 rounds. First declared campaign attempt; the two-reservoir
screening exercise and test preparation precede this count.
One mechanism: enlarge both old K3,3 reservoirs to K4,3 on the distinguished
side, leaving the binary and selector edges unchanged. Every intended cut covers
all private vertices plus the two distinguished vertices; the remaining six
vertices in each reservoir then match internally. Encode source perfect-matching
choices as well as nonconstant cut colors. Recover from a component of the
actual target after deleting the supplied perfect matching.

Retrieved and read the dual-reservoir Matching Cut finding and underlying proof.
Its local forcing, saturation and same-color collapse are relevant; no inherited
perfect-matching extension claim exists. Fresh vertices have three old reservoir
neighbors. Check that arbitrary target matchings, not only intended cut edges,
produce valid source matching variables. Do not change to the PMC predicate.

Finite scope: all 9 prepared cases, then 11 connected bipartite atlas graphs
through 5 vertices plus C6, a six-vertex ladder, an eight-cycle and P8. These test
both decisions, exact target radius/bipartition, multiple solver matchings and
matching-list order. No expanded search family or timeout. First discriminator:
P3 and the leaf example must remain NO despite having Matching Cuts; C6 stays YES.

A complete arbitrary-size proof, polynomial maps, passing tests and fresh
independent review justify paper preparation. A failure is diagnosed at its
source-encoding, residual-matching or extraction premise without repeating setup.

## Evidence and diagnosis

One full construction mechanism and one executable Karp pair were evaluated.
The [prepared run](prepared.json) passed nine cases (four YES, five NO) and
sixteen recovery calls. Each of two solver matchings per YES output was also
supplied in reversed list order; order reversal is not a distinct witness.
The [additional run](verification.json) passed fifteen cases (seven YES, eight NO)
and fourteen recoveries. The source families overlap. Commands and exact scope
are in [verification.md](../../work/verification.md). No candidate or checker
repair, inconclusive solver outcome or timeout occurred. Total time/token usage
is unavailable; no measurement is inferred from round counts.

The first discriminator passed: P3 and the eight-vertex leaf example remained
NO despite their Matching Cuts; C6 remained YES despite having no perfect cut.
The source edge variables, rather than just the previous color constraints,
account for this distinction. The [general proof](../../work/proof.md) covers
perfect-matching extension, universal matching-only recovery, totality and size.
The mechanism addresses the precise prior obstruction: the center edge removes
one vertex from the distinguished side of each K4,3, leaving a balanced K3,3.
Every private vertex is already covered by its unique private crossing edge.
This sufficiency statement uses the exact interfaces and no extra unmatched
private vertices. An arbitrary supplied target matching gives a cut by deletion
components, so necessity needs no canonical matching or two-component premise.

The [independent review](../../reviews/complete-rule/review.md) advanced without
repair. Its new full cases were K2,4 (NO), cube (YES) and P9 (NO), with three
actual distinct matching recoveries and maximum target order 5694. Local states
were exhaustively enumerated, four invalid encodings rejected, and the residual
matching and exact size formulas checked. Finite recovered witnesses all had
two deletion components; the general proof provides unrestricted recovery.

The review confirmed the source hardness directly in Bouquet and Picouleau,
https://arxiv.org/pdf/2011.03318 (v2), Section 2, PDF page 3 (historical hyphenated
name means current DPM), Theorem 3.3, PDF page 6 (bipartite diameter four).
Lucke's Table 1, Corollary 17 and Section 5 Open Problem 1 identify the target gap:
https://arxiv.org/html/2501.08735. Dated queries and limits are in the review.
The 2026-09-15 audit found no exact existing resolution; a publisher full-text
request for a newer induced-path paper failed. Novelty remains coverage-limited.
Significance is a related moderate-importance classification extension of the
preceding Matching Cut result, not a new independent interface mechanism.

Experience extraction: searched shared entries for K4/residual/balanced/extension.
The existing interface entry explicitly leaves perfect-matching extension open.
The qualifying new finding is the balanced-reservoir extension under private
crossing saturation, with component-based recovery. Post-campaign maintenance saved the [new finding](../../../../research/experience/balanced-reservoir-perfect-matching-extension.md)
and updated the [old use history](../../../../research/experience/dual-reservoir-matching-cut-interfaces.md).
One new entry, one pre-existing entry updated, zero extractions pending.
No other qualifying finding is pending. This use helped construct the result,
but it does not measure a causal improvement in discovery efficiency.

## Next action

Stop discovery on this target at ready_for_expert_review: full pair, general
proof, independent advance review, and the inspected eight-page English Typst
paper are complete. [Paper inspection](../../work/evidence/paper-inspection.txt)
records the final compilation and editorial checks. One of forty rounds is
complete and thirty-nine unused. No additional construction is justified by a
known missing obligation. Human expert correctness, novelty and significance
assessment is next; its outcome is unknown. No calibrated probability is given.

