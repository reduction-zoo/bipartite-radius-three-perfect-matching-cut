# Round 005: leave crossing budgets for external variable connections

Status: completed; declared before checking.
Hypothesis: a complementary pair could use internal crossing budgets (1,0),
leaving one port available for an external crossing edge. This changes a premise
of the exact-one experience lemma, so its conclusion cannot simply be reused.
Bounded proof exercise: derive the center-layer count with third-layer budgets
in {0,1}, while all vertices in layers zero through two still require exactly
one crossing and uh is fixed crossing. Check the generalized statement on all
connected bipartite atlas graphs through order seven, all eccentricity<=3
centers and all binary colorings satisfying those premises. No synthesis sizes
are expanded. End with a proof or counterexample and its consequences for the
three complementary pairs. A partial boundary is not itself a legal target.

Result: the generalized count is sum over z in L3 of [color(z)=0 and
internal_crossings(z)=1] = |F|. Proof: each vertex of F is forced one by h,
has no zero neighbor in L1, and needs exactly one zero L3 neighbor. That
neighbor necessarily has budget one. Conversely a zero L3 vertex of budget
one cannot match a second-layer vertex touching a zero L1 vertex, so its
unique mate lies in F. This is the same bijection with unmatched ports excluded.

With three pairs of budgets (1,0), and no other L3 vertices, the count measures
zeros among the three budget-one ports. Full NAE again needs counts one and
two, so this interface is impossible at every size under the stated premises.
The exhaustive check passed 100 partial colorings, including 66 with a zero
budget terminal. See check.py, check.log and result.json. No independent review
or novelty claim. The mixed-budget shortcut is rejected; next move the logical
ports to layer two, where this particular count does not directly apply.
