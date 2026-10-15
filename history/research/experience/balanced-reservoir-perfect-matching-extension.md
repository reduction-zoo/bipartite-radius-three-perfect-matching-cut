# Balanced residual reservoirs extend encoded cuts to perfect matchings

Recorded: 2026-09-15. Tags: disconnected-perfect-matching, matching-cut,
bipartite, radius-three, residual-matching, reservoir, witness-recovery.

## Claim and applicability

In the exact binary/selector composition of the
[dual-reservoir interface](dual-reservoir-matching-cut-interfaces.md), enlarge
each K3,3 reservoir to K4,3 by adding one vertex to the side containing its
joined distinguished vertex. Give the added vertex only its three reservoir
neighbors. Every satisfying opposite-reservoir coloring has a crossing matching
covering all private vertices and the two joined centers. Removing those centers
leaves a balanced K3,3 in each reservoir, so six monochromatic internal edges
complete a perfect matching. All vertices remain within three steps of the first
center. Equal reservoir colors still force a constant coloring.

The premise that EVERY private vertex has exactly one PRIVATE opposite neighbor
is essential: occurrence-port saturation alone would not cover unmatched private
vertices. Extra attachments, changed interface topology, other reservoir sizes
or different distinguished sides require rechecking both coverage and radius.
This is a DPM extension, not a claim that the crossing edges form a perfect cut.
The same center-edge extension fails for the original K3,3 pair: its residual
sides are unbalanced. That failure is a named construction obstruction, not a
negative theorem about all radius-three DPM graphs.

For recovery from an arbitrary disconnected perfect matching M, take the component
of zero in H-M as one cut side and all other components as the other. Every
crossing edge lies in M. This lets the Matching Cut interface relations decode
source matching-choice bits without receiving cut colors or assuming exactly two
deletion components. The source formula must explicitly enforce perfect matching;
a Matching Cut source encoding alone is insufficient for the DPM-to-DPM contract.

## Evidence and status

General proof in [the originating campaign](../../campaigns/bipartite-radius-three-disconnected-perfect-matching/work/proof.md),
with [round 001](../../campaigns/bipartite-radius-three-disconnected-perfect-matching/rounds/001/round.md)
and [independent advance review](../../campaigns/bipartite-radius-three-disconnected-perfect-matching/reviews/complete-rule/review.md).
Finite checks supplement the proof. Tested recovered witnesses had two deletion
components; arbitrary-component recovery is an analytic conclusion. Human expert
validation remains outstanding. This is a related extension of the prior local
Matching Cut construction, not a new independent discovery mechanism.

## Consequence for search

When transferring a matching-cut construction to DPM, inspect the graph left
unmatched by the intended cut. Here a one-vertex enlargement of each reservoir
repairs its residual side imbalance while preserving color forcing and radius.
Check unmatched PRIVATE vertices separately. Recover actual matching witnesses
through deletion components and encoded source edge choices, not through an
unjustified identity between the cut variants.

## Use history

Origin: DPM round 001. No later use yet. This successful transfer is evidence for
this mechanism, not a controlled measurement of framework efficiency.
