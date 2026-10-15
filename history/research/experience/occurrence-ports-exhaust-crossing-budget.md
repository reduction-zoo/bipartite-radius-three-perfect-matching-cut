# Occurrence ports exhaust their crossing budget inside the variable wire

Evidence type: conditional general argument with finite checks.
Review status: native independent review supports the one-occurrence application
in the complete rule; other historical scopes retain their original review status.
Recorded: 2026-09-15, retrospectively after round 040.
Tags: perfect-matching-cut, radius-three, variable-wire, occurrence, interface-budget.

## Claim and applicability

For the variable wire constructed in round 028, allow the occurrence vertices
v,w to have at most one internal opposite neighbor while requiring exactly one
at every other vertex. The round-029 argument forces each occurrence to have
exactly one internal opposite neighbor and to copy its designated variable port.
Thus any PMC extension attaching only at these occurrence vertices must make
every added incident edge monochromatic.

This applies to that wire and its stated repetitions. It does not assert the
same property for arbitrary variable gadgets, rewired interiors or attachments
at other vertices. It supplies an interface condition, not a clause construction.

## Evidence and status

Round 029 gives the author-side argument and nine UNSAT relaxed-boundary
queries. [Round 028](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/028/round.md) supplies the construction and positive assignment checks.
The relaxed check tests whether external attachments could consume a budget
that the isolated gadget appeared to use internally.
See [originating round](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/029/round.md),
[check](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/029/check.py) and [original output](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/029/check.log).

## Consequence for search

Specify boundary colors and remaining crossing budgets before synthesizing a
clause. For this wire, give occurrence ports zero additional crossing budget.
When changing the wire, recheck this property with terminal counts relaxed to
at most one; isolated exact-one tests alone do not establish it.

## Use history

Extracted retrospectively after round 040; subsequent uses are recorded below.
Earlier experiments are evidence, not evidence of retrieval from this entry.

- [Round 045](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/045/round.md)
  checked the missing shared-center premise: relaxing counts at center and mate
  as well as occurrences still gave nine UNSAT bad-interface queries. Effect:
  finite evidence supports composing the wire with the selector at that edge;
  the broader boundary argument still needs proof.

- [Round 046](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/046/round.md)
  applied the shared-center, saturated-port interface. Connecting selector high
  ports to complementary binary occurrences passed sixteen signed exact-one
  truth-table checks. Effect: a tested clause composition, still no full proof.

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
