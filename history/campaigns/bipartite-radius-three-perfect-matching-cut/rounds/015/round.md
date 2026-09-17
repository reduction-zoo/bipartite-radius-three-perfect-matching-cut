# Round 015: compose the successful two-access cube interfaces

Status: completed; declared before execution.
Action: Continue to the missing global step. Identify u and h across clause
copies of each of round 014's four successful connector types. Add one variable
vertex and its leaf for each source variable, and connect it to the corresponding
cube port as in Theorem 19. Scope: the four types on three fixed formulas:
one clause, the three clauses (0,1,2),(1,2,3),(2,3,4), and all four triples on
four variables. Solve each source and target with the existing Z3 oracles; check
bipartiteness, connectivity, actual radius and decoded target witnesses. Preserve
YES/NO counterexamples and structural failures. This is a diagnostic construction,
not a candidate accepted into work/algorithm.py. End after 12 pairs.

Result: 12 source/target pairs, 12 source and 12 target solver queries. All
sources are YES. Each interface fails on at least one source: the first three
fail on the three-clause chain; the fourth fails on all triples on four variables.
The eight multi-clause outputs all have radius four; the four one-clause outputs
have radius three. Eight target witnesses were returned and their variable
projections validated. Full witnesses and YES-to-NO examples are in result.json.
Sharing the access edge imposes a common phase across clauses, and variable leaves
also increase distances. These defects are decisive for this specific composition.
No candidate was submitted to final Verify or independent Review. No repairs.
Next investigate a whole-graph bipartization mechanism from the adjacent literature,
rather than searching larger versions of the failed shared-center interface.
