# Bipartite radius-three Perfect Matching Cut

Status: **ready_for_expert_review**. Updated: 2026-09-15.
Budget: 60 total rounds authorized; 50 completed, 10 remaining. The [question](question.md) is fixed.
The complete rule, general proof, passing checks, independent advance review and
inspected English Typst manuscript are available:

- [Forward construction and witness recovery](work/algorithm.py), with
  [general proof](work/proof.md).
- [Verification](work/verification.md): six prepared cases with 28 recoveries;
  38 additional cases with 134 recoveries, including three NO cases.
- [Independent review](reviews/complete-rule/review.md) and
  [advance follow-up](reviews/parser-followup/review.md). The sole required
  repair was integer-parser totality; no mathematical construction change.
- [Paper](work/manuscript.pdf), [Typst source](work/manuscript.typ), and
  [six-page visual inspection](work/evidence/manuscript-layout/inspection.txt).

## Current assessment

The rule reduces Positive NAE-3-SAT to connected simple bipartite Perfect Matching
Cut at radius at most three. For nonempty sources it emits 4+8n+160m vertices and
3+14n+304m edges. The proof covers arbitrary inputs and recovery from every valid
target witness; finite tests remain separate evidence. Native independent review
supports correctness, novelty within the recorded search coverage, and significance.
Human expert assessment and inaccessible or unlocated literature remain outstanding.
No publication, submission or production integration has occurred.

The new allocation used ten rounds (041–050). Round 041 refuted the binary-mate
conjecture with a ten-vertex example; its exact-one interface completed the
missing clause mechanism. Once the complete candidate passed review, the same
conversation finished writing. Verification, parser repair and writing did not
consume artificial research rounds. Ten of the sixty authorized rounds remain
unused; no further construction is recommended without a substantive new finding.
Full wall-clock time and token usage were not measured. There is no calibrated
success probability or controlled evidence that the skill improved discovery rate.

## Round index

Rounds 001–002 were reconstructed; later rounds were declared before execution.
Round counts do not measure independent ideas. Historical initial reasoning is
preserved with [round 002](rounds/002/initial-construction.md).

| Round | Hypothesis / scope | Actual work | Outcome |
|---|---|---|---|
| [001](rounds/001/round.md) | Three L3 ports, no L3 auxiliaries | 4 templates, 4 synthesis queries | UNSAT; conditional general obstruction |
| [002](rounds/002/round.md) | One or two L3 auxiliaries | 5 templates, 5 synthesis queries | Declared templates UNSAT |
| [003](rounds/003/round.md) | Complementary port pairs; full-coloring exclusions | 2 templates, 64 graphs, 64 synthesis + 64 oracle queries | Both candidate limits reached |
| [004](rounds/004/round.md) | Same templates; exclude every extension of bad boundary | 2 templates, 2 graphs, 4 synthesis + 2 oracle queries | Both templates UNSAT |
| [005](rounds/005/round.md) | Paired ports with internal budgets (1,0) | General argument; 100 partial colorings through order 7 | Count obstruction extends under stated premises |
| [006](rounds/006/round.md) | Three L2 ports, fixed center edge | 3 templates, 3 synthesis queries, no graphs | Positive constraints UNSAT; too few distinct anchors |
| [007](rounds/007/round.md) | Give L2 ports distinct anchors | 3 templates, 3 graphs, 6 synthesis + 3 oracle queries | All templates UNSAT |
| [008](rounds/008/round.md) | Let center crossing neighbor vary | 3 templates, 3 synthesis queries, no graphs | Positive constraints UNSAT |
| [009](rounds/009/round.md) | Logical ports on both bipartition sides | 4 templates, 1 graph, 5 synthesis + 1 oracle queries | All templates UNSAT |
| [010](rounds/010/round.md) | Let center color depend on ports | 1 of 2 declared templates, 1 graph, 1 synthesis + 1 oracle queries | Exact local NAE relation; known cube |

| Round | Chosen action and question | Actual work | Result |
|---|---|---|---|
| [011](rounds/011/round.md) | Investigate the known radius-four composition | Primary theorem inspection; 2 Web queries | Identified saturated interfaces and distance gap |
| [012](rounds/012/round.md) | Investigate intact-cube shortcut obstruction | 15 graphs / 15360 colorings in completed enumeration | Proposed obstruction refuted; private-leaf center can reach some valid cubes |
| [013](rounds/013/round.md) | Continue by checking all input patterns | 15 graphs / 15360 colorings | Short attachments lose full NAE completeness |
| [014](rounds/014/round.md) | Reconsider private leaf; give mate a second access path | 240 graphs / 245760 colorings | 4 exact local NAE interfaces at center eccentricity 3 |
| [015](rounds/015/round.md) | Continue to actual shared-center composition | 12 source/target pairs; 24 solver queries | Each interface has a YES-to-NO example; all 8 multi-clause outputs have radius 4 |
| [016](rounds/016/round.md) | Investigate whole-graph bipartization | Adjacent primary construction inspection; 3 Web queries | Identified twin synchronization as an unproved prerequisite |
| [017](rounds/017/round.md) | Investigate ordinary double cover | 30 graphs / 60 solver queries | 3 NO-to-YES counterexamples |
| [018](rounds/018/round.md) | Reconsider unsynchronized twins | 256 boundary colorings and biclique argument | Equality gadget preserves terminal crossing budgets |
| [019](rounds/019/round.md) | Continue to synchronized whole-graph transformation | 142 graph pairs / 426 solver queries | Decisions and finite-instance universal recovery pass; all radii exceed 3 |
| [020](rounds/020/round.md) | Investigate structural radius failure | General argument; 142 graphs / 6472 target centers | This private synchronizer always gives radius at least 4 |

## Evidence to resume from

- [Preparation](work/preparation.md): existing oracle foundation, reused unchanged.
- [Round 003 audit](rounds/003/evidence-check.log) and
  [rounds 004–010 audit](work/audit-rounds.log): saved candidate and witness checks.
- [Round 015](rounds/015/round.md): actual source-formula composition counterexamples.
- [Round 019](rounds/019/round.md): intermediate transformation, 142 graph pairs
  and universal finite-instance recovery checks; radius fails.
- [Round 020](rounds/020/round.md): radius obstruction, 6472 center checks, and
  the measured activity and limitations of the ten-round skill assessment.

The revised skill was followed by focused literature investigations and a change
of mechanism. This continuation had prior evidence and explicit user discussion;
it does not establish a causal improvement or calibrated success prediction.


## Rounds 021–040

| Round | Action / scope | Result |
|---|---|---|
| [021](rounds/021/round.md) | Reconsider smaller synchronizers; 205 connected graphs | 12 exact boundary interfaces |
| [022](rounds/022/round.md) | Compose 12 interfaces on 30 graphs; 1080 queries | Decisions pass; all radii 4–5 |
| [023](rounds/023/round.md) | Diagnose privacy; 9864 centers checked | Conditional general radius >=4 obstruction |
| [024](rounds/024/round.md) | Shared two-pair interface; 1 synthesis query | Eight-vertex template UNSAT |
| [025](rounds/025/round.md) | Structural literature; 3 Web queries | Residual center constraints identified |
| [026](rounds/026/round.md) | Leaf-center flow; 121 queries | Restricted decisions and recovered witnesses pass |
| [027](rounds/027/round.md) | Binary variable gadget; 4096 colorings | Four perfect cuts, radius 3 |
| [028](rounds/028/round.md) | Nine variable/occurrence compositions; 51 queries | Independent inputs extend, consistency checks pass |
| [029](rounds/029/round.md) | External-budget robustness; 9 queries | Occurrence ports remain internally saturated |
| [030](rounds/030/round.md) | Saturated L2 NAE ports; 2 templates, 6 queries | Both UNSAT |
| [031](rounds/031/round.md) | Exact-one primitive; 2 templates, 6 queries | Both UNSAT |
| [032](rounds/032/round.md) | L3 ports with tested wire; 1 synthesis query | Order-16 template UNSAT |
| [033](rounds/033/round.md) | All 32768 fixed-edge K4,4 masks | 1584 feasible center graphs; mate diversity <=2 |
| [034](rounds/034/round.md) | 5000 larger random graphs plus radius-four control | 23 feasible sampled graphs; control has 3 modes |
| [035](rounds/035/round.md) | Spectral literature; 3 Web queries | Sign-eigenvector characterization, not a solution |
| [036](rounds/036/round.md) | Spectral relaxation; 205 graphs, 410 queries | 18 false positives |
| [037](rounds/037/round.md) | Preserve wire colorings; 9 queries, 19 added edges | Both all-equal inputs survive |
| [038](rounds/038/round.md) | Allow new extensions on entire wire; 3 queries | Edge-augmentation template UNSAT |
| [039](rounds/039/round.md) | Intermediate exact-one encoding; 18 pairs, 54 queries | Source equivalence and recovery checks pass; graph primitive missing |
| [040](rounds/040/round.md) | 600 planted-PMC graphs; 431640 eligible-coloring checks | 284 eligible graphs; binary-choice observation remains unproved |

The [allocation assessment](rounds/040/round.md) records costs, what was reused,
what changed and why these observations do not establish a skill-effectiveness
improvement. The [closing audit](work/evidence/additional-rounds/audit.log)
checked saved synthesized graphs without rerunning discovery or preparation.

## Experience extraction closeout

Retrospective extraction on 2026-09-15 for rounds 021–040: three new entries,
zero existing entries updated, zero pending extractions. At that closeout, the shared collection
had four finding files; round records are not counted as experience entries.

- [Private robust equality synchronizers force radius at least four](../../research/experience/private-equality-synchronizers-force-radius-four.md).
- [Occurrence ports exhaust their crossing budget inside the variable wire](../../research/experience/occurrence-ports-exhaust-crossing-budget.md).
- [Preserving literal-colored extensions by adding edges cannot enforce NAE](../../research/experience/literal-colored-edge-additions-cannot-enforce-nae.md).

Other observations remain in their rounds: bounded template results and sampling
hypotheses have not been promoted to broader exclusions. Detailed positive wire
checks support the occurrence-interface entry rather than a duplicate entry.

## Rounds 041–050

| Round | Scope | Result |
|---|---|---|
| [041](rounds/041/round.md) | Directed three-mate synthesis | 10-vertex counterexample; one query |
| [042](rounds/042/round.md) | Exact selector truth table | 1024 colorings; three normalized cuts |
| [043](rounds/043/round.md) | Shared-center selector copies | 42 queries; independent choices pass |
| [044](rounds/044/round.md) | Relaxed selector boundaries | Three UNSAT bad-interface queries |
| [045](rounds/045/round.md) | Relaxed wire center | Nine UNSAT bad-interface queries |
| [046](rounds/046/round.md) | Signed exact-one clause | 16 truth-table queries pass |
| [047](rounds/047/round.md) | Interacting signed clauses | 36 graphs, 288 queries pass |
| [048](rounds/048/round.md) | Full NAE source composition | Six prepared cases and 28 recoveries pass |
| [049](rounds/049/round.md) | General composition proof | Author-side proof and polynomial bounds |
| [050](rounds/050/round.md) | Primary novelty check | Six queries; no prior resolution found within coverage |

## Experience closeout for rounds 041–050

Created **one** entry: [three-mate selector](../../research/experience/three-mate-choices-at-radius-three.md).
Updated **two** pre-existing entries:
[color count](../../research/experience/fixed-center-edge-color-count.md) and
[occurrence budgets](../../research/experience/occurrence-ports-exhaust-crossing-budget.md).
There are **zero pending** extractions and **five total** shared finding files.
The new selector entry was updated in place throughout its later uses and is
counted once. Every new round records its extraction decision. Literature
coverage stays in round 050; the parser defect stays with its regression evidence.
Entry existence and successful use are not a controlled measure of skill benefit.
