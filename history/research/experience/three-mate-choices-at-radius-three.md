# Radius-three PMC admits three mate choices at a fixed center edge

Evidence type: explicit counterexample and general interface proof.
Review status: native independent review of the complete application advanced;
human expert review remains outstanding.
Recorded: 2026-09-15.
Tags: perfect-matching-cut, bipartite, radius-three, center, mate, selector.

## Claim and applicability

A connected bipartite graph of order ten and radius three admits three perfect
cuts sharing the same center crossing edge, with three different crossing mates
at another vertex. Thus binary mate choice is not a general property of this
class. The example does not supply an arbitrary-size reduction or clause composition.

## Evidence and status

[Round 041](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/041/round.md)
synthesized the graph; [result.json](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/041/result.json)
contains every edge and all three checked witnesses. The
[check](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/041/check.py)
validates the target predicates directly. This contradicts the tentative
interpretation of the earlier samples, not their recorded finite observations.

## Consequence for search

Use the example as a regression against binary-choice obstructions. Investigate
its selector relation and attachment budgets before attempting clause composition.
A directed constraint query can challenge a sampling hypothesis without more
samples from the same generator.

## Use history

Origin: round 041; subsequent uses are recorded below.

- [Round 042](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/042/round.md)
  exhaustively checked the saved example: with center color zero, vertices
  (2,3,4) are one-hot and (6,7,8) are their complements; the center mate is fixed.
  This supplied a candidate selector interface, with composition still untested.

- [Round 043](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/043/round.md)
  reused the relation for shared-center composition: 39 assignments on one to
  three copies extend, and three universal finite bad-relation checks pass.
  Effect: local choices compose; external attachment still requires validation.

- [Round 044](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/044/round.md)
  relaxed center, center-mate and high-port budgets in the three compositions.
  Three bad-relation queries are UNSAT: high ports remain saturated. This is
  finite attachment evidence, not yet a general robust-interface proof.

- [Round 046](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/046/round.md)
  applied the shared-center, saturated-port interface. Connecting selector high
  ports to complementary binary occurrences passed sixteen signed exact-one
  truth-table checks. Effect: a tested clause composition, still no full proof.

- [Round 047](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/047/round.md)
  reused one occurrence pair per variable across two signed clauses. All 288
  pinned assignments on 36 clause pairs agree with exact-one semantics. Effect:
  no observed interference from repeated saturated-port attachments.

- [Round 048](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/048/round.md)
  composed the source bridge and graph interfaces into executable forward and
  recovery maps. All six prepared cases pass, including a NO source. Effect:
  first complete candidate; general proof and independent review still pending.

- [Round 049](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/049/round.md)
  supplied a general argument for the exact interfaces used in the complete
  construction; see [candidate proof](../../campaigns/bipartite-radius-three-perfect-matching-cut/work/proof.md).
  Status: author-side proof, independent review pending. The argument establishes
  boundary saturation for arbitrary attachment multiplicity under its named
  shared vertices and permits recovery from every full target witness.

- [Complete-rule review](../../campaigns/bipartite-radius-three-perfect-matching-cut/reviews/complete-rule/review.md)
  independently checked the boundary proof and its use in the final construction.
  The [follow-up](../../campaigns/bipartite-radius-three-perfect-matching-cut/reviews/parser-followup/review.md)
  advanced after a parser repair. Effect: this finding supports a complete
  reviewed rule, not merely a local test. This is native agent review, not human
  validation or measured evidence of a discovery-rate improvement.

- [Matching Cut round 001](../../campaigns/bipartite-radius-three-matching-cut/rounds/001/round.md)
  used this topology as a design lead with two K3,3 reservoirs. Fresh proofs and
  exhaustive local checks established the at-most-one relation, same-color
  collapse and arbitrary saturated-port attachment. The complete Karp pair
  passed independent review. Effect: a useful transferred topology after
  rechecking the changed predicate, not reuse of an exact-one theorem or a
  measured discovery-rate gain. See the [new interface finding](dual-reservoir-matching-cut-interfaces.md).
