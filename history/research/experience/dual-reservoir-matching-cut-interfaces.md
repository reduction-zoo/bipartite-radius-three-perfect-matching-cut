# Dual reservoirs for radius-three Matching Cut interfaces

Recorded: 2026-09-15. Tags: matching-cut, bipartite, radius-three,
reservoir, same-color-collapse, saturated-port, exact-one-selector.

## Claim and applicability

For Matching Cut (at most one opposite neighbor), two disjoint K3,3 reservoirs
joined by one distinguished edge can support the binary and selector interfaces
specified in the [proof](../../campaigns/bipartite-radius-three-matching-cut/work/proof.md).
Each private anchor has two distinct neighbors in its assigned reservoir.
With opposite reservoir colors, the binary ports encode a bit and its complement,
and the selector lows are one-hot with complementary saturated high ports.
Literal attachments join high ports to complementary occurrences. All such edges
are monochromatic, so arbitrary occurrence multiplicity is permitted.

With equal reservoir colors, every private vertex in these exact interfaces has
that same color. Thus nonconstant cuts in the complete composition force opposite
reservoirs; arbitrary local nontriviality cannot bypass the Boolean constraints.
The stated bipartition and paths put every vertex within three steps of the first
distinguished reservoir vertex, on YES and NO inputs.

Premises include the exact edges, distinct anchors, private labels and specified
attachment orientation. Extra edges preserve necessary local upper-bound
implications but can destroy intended extensions; their sufficiency needs checking.
This is not a Perfect Matching Cut lemma: most reservoir vertices have zero
opposite neighbors. No diameter-three or perfect-matching extension is asserted.

## Evidence and status

General interface and composition proof, supported by executable finite checks.
[Originating round](../../campaigns/bipartite-radius-three-matching-cut/rounds/001/round.md).
[Independent review and checks](../../campaigns/bipartite-radius-three-matching-cut/reviews/complete-rule/review.md)
advanced the complete Karp pair without repair. Human expert validation remains
outstanding. The earlier exact-one PMC topology was a design lead; its stronger
predicate was rechecked from first principles under Matching Cut.

## Consequence for search

For an at-most-one cut construction requiring shared reference colors, test
same-color collapse as well as the opposite-color relation. Two-neighbor forcing
can make anchor colors mandatory while keeping intended reservoir attachments
monochromatic. Use the reviewed exact interfaces when their premises apply;
metric or predicate changes require a new proof, not an assumption of transfer.

## Use history

Origin: round 001 of the bipartite radius-three Matching Cut campaign.
- [DPM round 001](../../campaigns/bipartite-radius-three-disconnected-perfect-matching/rounds/001/round.md)
  reused the binary/selector topology and rechecked every private vertex's crossing
  coverage. Enlarging both reservoirs to K4,3 left balanced residual matchings;
  encoding source-edge choices supported recovery from arbitrary target matching
  witnesses. Independent review advanced the full pair. Effect: a useful related
  extension under newly checked premises. See the
  [new finding](balanced-reservoir-perfect-matching-extension.md).

One successful transfer does not measure a causal improvement in research efficiency.
