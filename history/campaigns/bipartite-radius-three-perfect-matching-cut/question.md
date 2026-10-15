---
status: ready-for-attempt
openness: supported-within-search-coverage
difficulty: moderate
importance: moderate
tags: [graph-cuts, bipartite, radius, NP-hardness]
last-literature-check: 2026-09-14
---

# Positive NAE-3-SAT to bipartite radius-three Perfect Matching Cut

[Board](../../research/open-problems/README.md) · [Karp contract](../../research/open-problems/README.md#shared-karp-contract)

**Reduction target:** Positive NAE-3-SAT → bipartite radius-three Perfect Matching Cut

| Assessment | Evidence |
|---|---|
| Difficulty | Moderate, provisional: known NAE relation; distance connector missing |
| Importance | Moderate: complete the corresponding bipartite radius boundary |
| Proof readiness | Provisionally ready for a bounded attempt; second priority; no blocking gate |

**Exact endpoints.** Each source clause contains three distinct unnegated
variables and must receive both truth values. The target is a connected simple
bipartite graph of radius at most three admitting a cut with exactly one
opposite neighbor at every vertex.

**Gap.** R3, Theorem 19 and Open Problem 2, leave this case between radius-two
tractability and radius-four hardness. A perfect matching containing a cut is a
different predicate and its hardness does not settle this target.

**Route and evidence.** Earlier enumeration of all 256 cube colorings confirmed
the known NAE relation on three designated ports. A pinned shortcut with an
already saturated hub had no extension in 12 cases. The connector must replace
part of the clause rather than simply spend an unavailable crossing-edge budget.
These finite checks support a focused attempt, not the existence of the connector.

In the cube with vertices labeled 0 through 7 in binary, the designated ports are
1,2,4. There are six perfect-cut colorings; vertices 0 and 7 always differ. The
failed shortcut adds a helper between a hub and vertex 0, pins the hub to the
color of vertex 7, and assumes its required crossing edge is already supplied
elsewhere. Preserving the cube forces the helper to color 0, while preserving
the hub budget forces the other color. This
excludes the pinned saturated shortcut, not general radius-three connectors.

**Next exercise.** Specify and synthesize one connector with boundary color and
crossing-budget states, then prove the global radius bound. This would resolve
the radius boundary for PMC alone, not automatically for other cut variants.

## Primary sources

- **R3:** [Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter](https://arxiv.org/html/2501.08735), January 2025, Theorem 19 and Open Problem 2.

## Research history

- [Recorded probe](../../research/evidence/cut-and-augmentation-probes.py): finite evidence only, not an independent proof review.

- 2026-09-14: Web and arXiv update queries: `"Disconnected Perfect Matching" "radius 3" bipartite`; `"Perfect Matching Cut" "diameter" "open" 2026`; `"Matching Cut" "radius 3" 2026 bipartite`; `"2-cut" "line graphs" 2026`; `"perfect matching cut" "radius" 2026`; `"Perfect Matching Cut" "radius 3"`.
  No exact resolution was located within this search; unpublished, unindexed,
  and overlooked results remain outside the supported openness claim.

- 2026-09-14, campaign handoff: selected the board's second-priority target.
  Rechecked arXiv:2501.08735v1 and the published TCS 1052 (2025) 115429
  [journal PDF](https://durham-repository.worktribe.com/OutputFile/4275060),
  Theorem 19 and Open Problem 2. The radius-three case remains explicit there.
  Publisher HTML access failed; the university-hosted published PDF succeeded.
  Checked [author updates](https://felicialucke.github.io/publications.html).
  Queries included `"Perfect Matching Cut" "radius" "three" 2026`,
  `"perfect matching cut" "radius 3" bipartite 2026`, and
  `"perfect matching cut" "radius three" bipartite`.
  No resolving primary theorem was found; unpublished and unexamined work remain
  outside coverage. The source predicate is positive NAE, and the target requires
  exactly one crossing neighbor, not a perfect matching containing a cut.
  The [campaign](../../campaigns/bipartite-radius-three-perfect-matching-cut/state.md)
  will first establish exact solver-based oracles, then investigate a replacement
  clause with an explicit center interface. Difficulty remains moderate only
  provisionally; no radius-three connector or complete rule is known here.

## Fixed campaign acceptance

Construct an original deterministic polynomial-time Karp reduction f from the
positive NAE-3-SAT language above to the stated graph language. Give a general
proof of YES/NO equivalence and polynomial worst-case running time and output
bit size. Deliver g(x,y), recovering a satisfying NAE assignment from every
valid perfect-cut coloring y of f(x), in polynomial time in the encoded input.
The executable contract is work/contract.md. Invalid source encodings are NO
strings and must map to the legal target NO instance C6. Empty formulas and
unused variables are legal. A partial gadget or a family exclusion is progress,
not completion. Do not weaken the radius or bipartiteness requirements.

Initial scope: establish solver oracles and investigate finite center-interface
families, plus structural obstructions suggested by their constraints. No
wall-clock timeouts. A search-family exhaustion is reported as partial research;
it does not rule out the reduction or settle the open problem.
