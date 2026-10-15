# Round 016: literature on bipartization instead of shared clause centers

Status: completed; declared before execution.
Action: Investigate an alternative mathematical mechanism. Round 015 exposed
phase coupling under shared centers. Theorem 22 next to the PMC proof uses
bipartite duplication for d-Cut. Scope: inspect that construction and its
exact budget assumptions, and use at most three Web queries to find primary
work on bipartite double covers and Perfect Matching Cut or radius-three PMC
on unrestricted graphs. Identify what must be synchronized for an exact-one
reduction. Stop with applicable facts, unresolved premises and a bounded next
check. No claim that the d>=2 theorem automatically applies to PMC.

Result: inspected the construction preceding Theorem 22 and its d>=2 premise
in https://arxiv.org/html/2501.08735v1 . It duplicates vertices on opposite
bipartition sides and replaces selected cliques by monochromatic bicliques;
this is not a general exact-one preservation theorem for arbitrary double covers.
The paper's Observation 2 provides the monochromatic-biclique ingredient.
Queries (2026-09-15): "perfect matching cut" "double cover";
"perfect matching cut" "radius 3" Heggernes Telle;
"perfect matching cut" "bipartite" duplication. Three queries used.
Primary abstract https://arxiv.org/abs/2107.06399 confirms separate bipartite
PMC hardness, but supplies no radius-three doubling guarantee. The title
"The complexity of the perfect matching-cut problem" (doi:10.1002/jgt.23167)
uses the contains-a-cut predicate in its abstract and is not interchangeable.
No ready-to-use theorem was found in this limited coverage; full coverage of
all original non-bipartite constructions remains unresolved.
Next test the simplest double cover's YES/NO equivalence before engineering
synchronization. This is a different whole-graph mechanism from clause-center
composition. No candidate or solver queries in this literature round.
