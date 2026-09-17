# Private robust equality synchronizers force radius at least four

Evidence type: conditional general argument with finite checks.
Review status: author-side; no independent review or novelty assessment.
Recorded: 2026-09-15, retrospectively after round 040.
Tags: perfect-matching-cut, bipartite, radius, equality, private-gadget.

## Claim and applicability

Consider a connected bipartite gadget with two terminals on opposite sides.
A local coloring is admissible when each internal vertex has exactly one
opposite neighbor and each terminal has at most one. Assume admissible colorings
exist and every such coloring gives equal terminal colors and zero opposite
neighbors at both terminals. In a connected bipartite composition with at least
two copies having disjoint private interiors, where only terminals attach outside,
the radius is at least four.

The argument permits edges among terminals. It does not cover shared interiors,
external attachments to internal vertices or weaker boundary relations.

## Evidence and status

Round 023 gives the conditional general argument and checks twelve interfaces,
360 composed graphs and 9864 possible centers. These finite checks support the
argument but do not establish it for all gadgets.
See [originating round](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/023/round.md),
[check](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/023/check.py) and [original output](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/023/check.log).

## Consequence for search

Before enlarging or shrinking a private equality gadget, check the boundary
and attachment premises. If they hold, change the composition or interface;
changing the private gadget alone cannot meet radius three.

## Use history

Extracted retrospectively; no subsequent use of this saved entry is recorded.
Earlier experiments are evidence, not evidence of retrieval from this entry.
