# Independent review: bipartite radius-three Matching Cut

Decision: **advance to expert review**.

Reviewed on 2026-09-15. No correctness blocker was found in the current forward
construction, recovery algorithm, or general proof. Novelty is supported within
the primary-literature coverage below; significance meets the fixed question.
This is an independent native agent review, not formal verification, human
expert approval, or publication acceptance.

## Scope

I read the repository contract, fixed question, and current
`work/{contract.md,algorithm.py,proof.md,preparation.md,verification.md}`. I also
read the retrieved PMC selector and occurrence-port experience entries. I wrote
[check.py](check.py) independently; it executes the candidate as a subprocess
and imports neither the candidate nor either existing checker. Candidate and
original evidence files were not changed. Mathematical scope remains the fixed
radius-four to radius-three Matching Cut rule.

## Correctness

The analytic argument handles arbitrary input size and every valid target
witness, rather than inferring correctness from the finite tests.

- **Source language and Boolean encoding.** `algorithm.py:7–38` checks the
  graph schema, simple ordered edges, connectivity, bipartiteness, and radius
  at most four. The preliminary order bound prevents allocation according to
  a huge invalid vertex count. At lines 43–46, the two clauses for each
  neighbor pair exclude exactly the two assignments with both neighbors
  opposite their common neighbor; the two long clauses require both colors.
  The fresh-variable chain at lines 49–53 preserves each disjunction in both
  directions. The selector/slack equations at lines 55–58 correctly encode
  OR by signed exact-one constraints: slack equals literal minus selector.
  Repeated literals in padded clauses are harmless.
- **Reservoirs.** Restriction to an embedded K3,3 preserves the upper bound
  on crossing degree. Its monochromaticity proof is valid even after arbitrary
  attachments. Two *distinct* reservoir neighbors force each designated
  private anchor to the reservoir color; the code indeed uses distinct pairs.
  In an intended extension these edges are all monochromatic. The only
  reservoir crossing edge is 0–6, so sharing reservoirs across arbitrarily
  many blocks does not accumulate crossing degree.
- **Binary interface.** With opposite reservoir colors, each of p,r,v,w sees
  a fixed neighbor of each color. Thus it is already saturated, and pv,rw
  enforce equality. The bounds at a and q force v,w to differ. The anchors
  f,z then also have exactly one opposite private neighbor. With equal
  reservoir colors, two same-colored neighbors force each free vertex to
  that color. This argument uses upper bounds throughout.
- **Selector interface.** A permits at most one selected low vertex. Zero
  selected low vertices force all high vertices to A's color, violating F's
  bound when the reservoirs differ. One selected low vertex forces the
  claimed complementary high colors; all high vertices are internally
  saturated. If reservoirs agree, any selected low vertex would force two
  high vertices opposite F; this is impossible. All remaining vertices then
  share the common color. These are valid fresh Matching Cut arguments;
  the stronger exact-one PMC predicate was not assumed.
- **Composition and universal recovery.** Both endpoints of every literal
  attachment are already saturated under opposite reservoir colors, so
  each attachment must be monochromatic. The positive-literal port is w,
  the complement of p; the negative-literal port is v=p. Consequently each
  low selector bit equals the corresponding signed literal. Any number of
  attachments can share a binary port because all are monochromatic.
  If reservoir colors agreed, *all* binary and selector blocks would be
  constant, contradicting target nontriviality. Therefore every nonconstant
  target witness supplies a satisfying Boolean assignment. The extractor
  at lines 80–82 reads p at position 13+8i and normalizes by vertex 0;
  the two source nontriviality clauses ensure its result is nonconstant.
- **NO direction and exceptional inputs.** The universal implication just
  proved rules out target witnesses for every legal NO source. Singleton
  inputs map to K3,3, a structurally legal NO target; extraction has no
  obligation there. Invalid encodings map outside the target language.
  The executable disables Python's integer digit cap and handles JSON
  syntax and nesting rejection explicitly. Recovery assumes the promised
  valid target witness, as permitted by the fixed contract.
- **Metric and size bounds.** The stated bipartition agrees with every
  constructor edge, including literal attachments. The listed paths from
  vertex 0 cover every vertex within three steps on YES and NO inputs.
  Each private label is new, and repeated occurrences connect distinct
  selector vertices, so there are no parallel edges. Directly counting
  the code gives 19 reservoir edges, 18 edges per binary block and 19 per
  selector; the claimed 12+8N+8K vertices and 19+18N+19K edges are correct.
  The formulas for C, N and K account for the n=2 padded clauses and long
  nontriviality clauses. Construction and output have polynomial size,
  with O(n^3 log(n+1)) output bits. The conservative polynomial bit-time
  claim and polynomial recovery bound are supported; neither map contains
  solver calls or random choices.

### Independent executed checks

Run from the repository root:

```sh
python3 campaigns/bipartite-radius-three-matching-cut/reviews/complete-rule/check.py
```

All checks passed; machine-readable results are in [checks.json](checks.json).

- Enumerated all 256 private colorings in each of four local settings: binary
  and selector blocks, with equal and opposite anchors. Equal anchors allow
  only the constant coloring; opposite anchors allow exactly two binary or
  three selector states. All occurrence/high-port saturation assertions pass.
- Executed the full candidate on K2, P3 and K2,3. Independently brute-forced
  source decisions and solved actual target outputs: YES, YES, NO. Output
  orders were 188, 356 and 2004, with 423, 809 and 4597 edges. Each output
  is simple, connected, bipartite, has eccentricity three at vertex 0, and
  matches the exact size formula.
- On every output, queried existence of a nonconstant target matching cut
  with equal reservoir colors: UNSAT. Also queried a valid target cut whose
  source-port projection is constant or has two opposite neighbors: UNSAT.
  These are six bounded counterexample queries. The two NO-output queries
  are vacuous once its base UNSAT result is known; the four YES-output
  queries provide nonvacuous bounded checks of the critical implications.
- Independently recounted solver witnesses and passed each YES witness and
  its complement through the actual extractor: four successful recovery
  calls. Rejected a radius-five path, Boolean vertex count, duplicated edge,
  odd cycle, disconnected graph and huge invalid vertex count. Checked the
  singleton's NO output separately.

The earlier 8 prepared cases/20 recoveries and 18 additional cases/56 recoveries
are author-side evidence, not independent instances added by this review.
Their overlapping families must not be presented as distinct graphs. The
interrupted arithmetic solver run is correctly excluded from passing evidence;
its unknown result is not interpreted as NO. I did not repeat those suites.
Finite UNSAT results do not establish the arbitrary-size theorem; the separate
analytic arguments above are essential.

## Novelty

Search date: 2026-09-15. Primary baselines actually inspected:

1. Felicia Lucke, *Matching cut and variants on bipartite graphs of bounded
   radius and diameter*, TCS 1052 (2025), 115429. The
   [published PDF](https://durham-repository.worktribe.com/OutputFile/4275060),
   page 2, Table 1 and introduction, retain the radius-two tractability and
   radius-four hardness boundary and explicitly describe radius three as
   open for Matching Cut. The
   [arXiv text](https://arxiv.org/html/2501.08735), Section 5, Open Problem 1,
   asks this exact case. The arXiv record currently exposes only v1. I
   obtained the published table and introduction through the repository's
   download link; later attempts to retrieve its conclusion/full local PDF
   returned HTTP 403. Thus the specific Open Problem 1 location was checked
   in the preprint, not asserted from an unread published conclusion.
2. Hoàng-Oanh Le and Van Bang Le, *A complexity dichotomy for Matching Cut
   in (bipartite) graphs of fixed diameter*, TCS 770 (2019), 69–78,
   [primary preprint](https://arxiv.org/html/1804.11102), Section 3,
   Lemmas 4–6 and Theorem 2. Its bipartite diameter-four hardness gives
   the fixed source hardness because radius is at most diameter. The
   construction uses private bicliques and occurrence connections; it does
   not establish the radius-three target. The matching-cut witness
   convention agrees with this campaign's nonconstant coloring predicate.

Queries included `"Matching Cut" "radius three" bipartite`,
`"Matching Cut" "radius 3" bipartite 2026`,
`"Matching Cut" "radius-three"`,
`"Matching Cut" "bipartite" "radius" "2026" NP-complete`,
`"decomposable" "bipartite" "radius three"`,
`"Matching Cut" bipartite "diameter 4" NP-complete`, and
`"Matching cut and variants" "115429"`.
No later exact resolution was located. General d-Cut hardness with d>=2,
maximum-cut variants, diameter-four results, and the previous PMC predicate
cannot simply be substituted for this target. The biclique rigidity and
Boolean bridge are established techniques; novelty attaches to the radius-three
construction and resulting classification, not those ingredients.

Coverage remains incomplete for unindexed, unpublished, overlooked and
inaccessible material. A search failure is not proof of novelty. Within the
checked primary baselines, the final theorem resolves the stated open case.

## Significance

The fixed source is NP-hard, the target lies in NP, and the complete Karp rule
therefore establishes NP-completeness at bipartite radius at most three, subject
to expert validation. Together with the known radius-two algorithm, this closes
the indicated bounded-radius threshold. That is a concrete classification
contribution meeting the campaign's moderate-importance criterion. No claim is
made about production integration, publication acceptance, or a separate result
for perfect/disconnected perfect matching.

## Disposition

Advance the unchanged candidate to paper preparation and human expert review.
No mathematical or implementation repair is required by this review. Keep the
literature coverage and finite-versus-general evidence distinctions explicit.
