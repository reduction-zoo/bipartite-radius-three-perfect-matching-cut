# Independent complete-rule review

Decision: **advance**, round 001, 2026-09-15. The unchanged candidate is eligible
for expert review and manuscript preparation. This is an independent native-agent
review, not independent human verification or publication acceptance.

## Correctness

I read the fixed question, contract, implementation, complete proof, preparation
and verification reports, and the shared dual-reservoir experience entry together
with its supporting Matching Cut proof. No blocking mathematical or implementation
gap was found.

The source CNF encodes exactly one selected edge at every vertex, requires both
vertex colors, and permits a crossing edge only when selected. These conditions
are equivalent to DPM, including the NO instances that merely possess a Matching
Cut. The singleton exception is a valid NO-to-NO map. All other connected source
graphs have nonempty incident lists, so short-clause padding is defined. The chain
conversion and selector/slack equations preserve satisfiability and project back
to the original matching bits. Repeated literals attach distinct high vertices
to a shared saturated occurrence port and do not introduce parallel edges.

The changed premise relative to the shared experience is perfect-matching
extension. The embedded K3,3 forces every old reservoir vertex monochromatic;
the additional vertex has three neighbors of that color and is forced with it.
The added edges are monochromatic in every intended extension, so they do not
consume any crossing budget. Opposite reservoirs give the two binary states and
three selector states, with exactly one opposite *private* neighbor at every
private vertex. Equal reservoirs collapse both blocks to the reservoir color.
This verifies the experience entry's applicability from its actual argument,
without assuming that a prior Matching Cut result already proves DPM.

For sufficiency, all crossing edges cover the private vertices and the two joined
centers. Removing those centers leaves K3,3 in each enlarged reservoir. The six
specific internal edges in proof.md complete a perfect matching, and no literal
or anchor attachment crosses. Thus the constructed matching disconnects the
whole graph. This resolves the residual matching obstruction left by K3,3
reservoirs; no parity obligation is hidden in the private blocks.

For necessity and universal recovery, any supplied valid target matching M gives
a nonconstant cut by taking the component of zero in H-M. Every crossing edge
belongs to M, hence the local crossing-degree arguments apply independently of
which monochromatic edges M used. Equal reservoir colors are impossible. The
binary assignments satisfy all exact-one constraints and therefore the source
CNF. algorithm.py:86–96 implements precisely this projection: it rebuilds the
actual target, deletes the promised ordered matching edges, performs BFS from
zero, then selects source edge j using port 13+8(n+j). Both edge orders are
lexicographic when the formula and recovery refer to j. This recovers a valid
source perfect matching containing a nontrivial cut. The argument does not assume
that H-M has exactly two components. It also proves the full NO direction.

All graph edges respect the stated bipartition; each block joins a reservoir;
and the displayed root-to-vertex paths have length at most three, even on NO
inputs. The extra reservoir labels and their orientation are correct. I recounted
14+8N+8K vertices and 25+18N+19K edges and checked the formulas for Z and C,
including degree-one clauses and nonconstant-color clauses. The O(n^3 log(n+1))
output and O(n log(n+1)) recovered-witness bounds hold. Both algorithms use fixed
iteration choices for emitted data and no solver or randomness. Validation and
recovery remain polynomial on their stated encoding domains. In particular,
B <= (n-1)m and n,m=O(L) on allocated valid graphs bound graph size by O(L^2),
which supports the deliberately loose fifth-power bit bound even when charging
polynomial worst-case set comparisons rather than expected constant lookup time.

## Independent executable evidence

Run:

```sh
python3 campaigns/bipartite-radius-three-disconnected-perfect-matching/reviews/complete-rule/check.py
```

The independently authored checker imports neither the candidate nor author
checkers. It invokes both maps in fresh subprocesses. Source decisions use direct
matching-subset enumeration; target decisions use a separately written Boolean
matching/cut formulation; returned witnesses are checked directly by deletion
connectivity and vertex incidence. It passed:

- K2,4: NO, target order 4030; exercises degree-four clause splitting and lack
  of a perfect matching despite a small-radius connected bipartite input.
- Cube: YES, target order 5694; three distinct solver-found target matchings
  each yielded a valid source DPM witness.
- P9: NO, target order 3926; exercises the source radius-four boundary and odd order.
- Exact target-size formulas, simplicity, connectedness, bipartiteness and root
  eccentricity at most three for all three actual outputs; four malformed-domain
  objects correctly mapped to {}.
- Exhaustive enumeration of all 256 colorings of each eight-vertex block for
  each normalized reservoir relation: one same-color state for either block,
  two opposite-color binary states and three opposite-color selector states.
  Every accepted opposite-color state saturates every private vertex internally.
  Removing a distinguished vertex from K4,3 leaves a perfect matching.

Results are saved in checks.json. I reused the unchanged author's 9-case/16-call
prepared evidence and 15-case/14-call additional evidence rather than repeating
those suites. The new target witnesses all had two deletion components; finite
coverage did not exercise more components or enumerate all target matchings.
The general necessity proof, not these finite checks, establishes arbitrary-witness
recovery and unrestricted sizes. No timeout, candidate repair or failed test occurred.

## Novelty

Primary-literature checks on 2026-09-15 support the claim within the following
explicit coverage:

1. Felicia Lucke, *Matching Cut and Variants on Bipartite Graphs of Bounded Radius
   and Diameter*, https://arxiv.org/html/2501.08735: Table 1 gives DPM hardness
   at radius four; Corollary 17 gives radius-two tractability; Section 5,
   Open Problem 1 asks the bipartite radius-three DPM question. Theorem 24 is
   maximum DPM optimization hardness, which does not establish this decision
   result. The publisher record confirms TCS 1052 (2025), 115429:
   https://doi.org/10.1016/j.tcs.2025.115429.
2. Bouquet and Picouleau, *The complexity of the Perfect Matching-Cut problem*,
   https://arxiv.org/pdf/2011.03318 (v2): Section 2, PDF page 3, explicitly defines
   the historical hyphenated problem as a perfect matching whose deletion
   disconnects the graph, so this is the present DPM predicate. Theorem 3.3,
   PDF page 6, states NP-completeness on bipartite diameter-four graphs. These
   connected instances have radius at most four, establishing the precise source
   hardness. Its construction uses paired source copies and much larger
   complete-bipartite attachments; the theorem does not already restrict radius
   to three. The published paper is https://doi.org/10.1002/jgt.23167.
3. Searches included `"Disconnected Perfect Matching" "radius 3"`, the
   `"radius three"` spelling, `"Disconnected Perfect Matching" bipartite 2026
   radius complexity`, and `"perfect matching-cut" "radius" bipartite three`.
   The newer induced-path/cycle and high-girth hardness results surfaced by the
   search do not state the required simultaneous bipartite radius-three bound.
   A publisher full-text request for the 2026 induced-path paper failed; its
   complete argument was not audited. Secondary open-problem aggregators were
   not used as evidence of openness.

No exact existing resolution or theorem consequence was located in this scope.
This does not exclude unpublished, unindexed, overlooked or differently phrased
work. The standard CNF conversions, biclique rigidity, and two-neighbor forcing
are not original contributions. The local Matching Cut campaign already supplies
the binary/selector topology; the present balanced-reservoir extension and actual
perfect-matching encoding/recovery are a related result. The claim is not a new
independent discovery mechanism or a separately established publication unit.

## Significance

The rule settles the fixed moderate-significance classification target:
NP-completeness at bipartite radius at most three, alongside tractability at
radius at most two. Target membership in NP is direct. This is a concrete named
boundary beyond merely implementing known constructions. Its incremental nature
relative to the immediately preceding local Matching Cut result is substantial
context, and the candidate explicitly acknowledges it. A combined treatment is
appropriate; any separate-paper significance judgment belongs to human experts.
All three review judgments therefore support advance with the coverage and
human-validation limitations stated above.
