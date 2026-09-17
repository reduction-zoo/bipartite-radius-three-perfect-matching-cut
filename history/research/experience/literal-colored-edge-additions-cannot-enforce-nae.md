# Preserving literal-colored extensions by adding edges cannot enforce NAE

Evidence type: conditional general argument with finite checks.
Review status: author-side; no independent review or novelty assessment.
Recorded: 2026-09-15, retrospectively after round 040.
Tags: perfect-matching-cut, NAE, edge-augmentation, literals, projection.

## Claim and applicability

Suppose a graph has a specified PMC coloring for each assignment to three
independent bits, with every vertex color a constant, a bit or its complement.
Adding edges while retaining all six specified NAE colorings also retains the
two specified all-equal colorings. Each retained coloring already spends every
vertex's crossing budget, so each new edge must be monochromatic. That equality
depends on at most two bits, and NAE realizes every assignment on any two bits.
It therefore holds on all eight assignments.

This excludes preserving those particular extensions by edge additions. It does
not exclude new internal extensions, edge deletions, added vertices or different
encodings.

## Evidence and status

Round 037 gives the conditional argument and checks the three-variable wire:
all nineteen edges safe on its six NAE colorings preserve both all-equal cases.
Round 038 separately excludes one finite augmentation template allowing changed
extensions; that bounded result is not part of the general claim here.
See [originating round](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/037/round.md),
[check](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/037/check.py) and [original output](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/037/check.log).

## Consequence for search

Check whether a proposed clause merely conjoins pairwise equalities on literal
colors. Under these premises, further safe edges cannot realize NAE. A next
attempt must change an implicated premise, such as the internal extensions.

## Use history

Extracted retrospectively; no subsequent use of this saved entry is recorded.
Earlier experiments are evidence, not evidence of retrieval from this entry.
