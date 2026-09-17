# Fixed center edge constrains third-layer color count

Evidence type: general lemma with finite consistency checks.
Review status: author-side proof; no independent review or novelty assessment.
Recorded: 2026-09-14.
Tags: perfect-matching-cut, bipartite, radius-three, center, layers, NAE, ports.

## Claim and applicability

Let G be connected and bipartite, with a vertex u of eccentricity at most three.
Write L_i for its distance-i layer. In a perfect-cut coloring, every vertex has
exactly one opposite neighbor. Fix the crossing edge uh with colors u=0 and h=1.
Let K=L_1 minus {h}, and let F contain those vertices of L_2 adjacent to h but
to no vertex of K. Exactly |F| vertices of L_3 have color zero.

The [argument](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/001/fixed-center-proof.md)
establishes a crossing-edge bijection between F and the zero-colored third-layer
vertices. It uses exact-one crossing budgets, bipartiteness and the fixed center
edge; check these premises before applying it elsewhere.

If L_3 consists only of three ports, their full NAE relation is impossible under
that fixed center edge: NAE permits both one and two zeros. If h is a leaf,
every vertex of L_3 has color one. These conclusions do not exclude interfaces
with third-layer auxiliary vertices, a different center-edge interface, ordinary
Matching Cut, or general reductions to radius-three PMC.

## Origin and design consequence

[Round 001](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/001/round.md)
tested four templates without third-layer auxiliaries; all were UNSAT.
[Round 002](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/002/round.md)
tested five expanded templates; all were UNSAT within their stated finite scopes.
The lemma was developed after these experiments. It explains the first family's
failure at every size, but does not explain all failures of the expanded family.
The [separate exhaustive check](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/002/obstruction_check.py)
passed for 33 feasible ordered center/mate choices and 34 colorings through order
seven; see its [log](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/002/obstruction-check.log).

Before searching a new NAE interface with these premises, explain how it absorbs
changes in port color count. Increasing the size of the three-port-only family
cannot help if the lemma applies. An auxiliary interface still needs its own
relation, composition and recovery proofs. Do not infer that the research target
is impossible, or that adding auxiliaries is sufficient.

## Use history

- Origin: extracted retrospectively after rounds 001–002. Their earlier move
  to auxiliaries preceded the proof and was not caused by retrieving this entry.
- 2026-09-14: [round 003](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/003/round.md)
  read the entry and its proof before proposing six complementary ports. The
  interface has three zeros in every intended assignment and uses |F|=3 as a
  synthesis constraint. Both templates reached 32 candidate graphs; all 64 graphs
  admitted unwanted all-equal encoded assignments. The audit confirmed 384 desired
  extensions and 992 rejections of prior full-coloring counterexamples.
  Effect: useful for choosing an interface consistent with the necessary count;
  inconclusive for finding an exact clause, with no complete reduction found.
  Constant color count is insufficient by itself. This is same-topic reuse,
  not measured speedup or demonstrated cross-task transfer. The lemma's evidence
  and review status remain unchanged.

- 2026-09-15: [round 041](../../campaigns/bipartite-radius-three-perfect-matching-cut/rounds/041/round.md)
  checked the fixed-center premises and distinguished constant color count from
  binary mate choice. Directed synthesis refuted the latter; the count lemma
  remains consistent with the example. Effect: avoided treating the count as
  a stronger obstruction; no complete reduction yet.
