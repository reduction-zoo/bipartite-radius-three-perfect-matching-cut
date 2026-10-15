# Round 018: synchronize opposite-side terminals without spending their budgets

Status: completed; declared before execution.
Action: Reconsider the missing twin-equality condition from round 017. Use K2,3
with one terminal in each side and a private leaf on each of its three other
vertices. Terminals must have zero internal crossing edges; all other vertices
must have one. Derive its complete boundary relation by all 256 colorings and
prove that even allowing at most one internal crossing at terminals forces
the biclique monochromatic. This lets terminals retain their crossing edges
in the double cover. End with the boundary relation and applicability proof,
or a counterexample. The monochromatic biclique is a literature ingredient
(Observation 2 in arXiv:2501.08735), not an original hardness claim.

Result: all 256 colorings checked. Exactly two satisfy the internal-vertex
budgets and at-most-one terminal budgets; both have zero crossings at terminals
and equal terminal colors. Proof: if the two vertices on the size-two side of
K2,3 differed, each of the other three vertices would send a crossing edge to
that side, exceeding its total capacity two. Hence those two agree; any opposite
vertex on the size-three side would have two crossings, so the biclique is
monochromatic. The auxiliary leaves supply the remaining internal budgets.
This argument holds inside larger graphs whose vertices have at most one
crossing neighbor. Author-side proof only; no independent review or novelty
assessment. Next compose this synchronization gadget with the double cover and
measure the resulting radius, rather than assuming local success suffices.
