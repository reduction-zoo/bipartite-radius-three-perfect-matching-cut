# Round 037: can edge-only augmentation preserve the wire and create NAE?

## Plan
Status: completed. Action: Investigate a construction obstruction.
Take the three-variable, one-occurrence wire from round 028. Enumerate its
normalized perfect cuts, then add every missing bipartite edge that is
monochromatic in all six intended NAE colorings. Check whether the two all-equal
colorings survive. Derive a general explanation when each vertex color is a
constant, variable or complement. This tests the explicit witness-preserving
augmentation idea; it does not exclude rewiring or different extensions.
Scope: this one wire, complete enumeration by Z3, one maximal augmentation.

## Evidence and diagnosis
Nine solver queries enumerate eight normalized wire colorings. Adding all 19
edges safe on the six NAE colorings retains both all-equal colorings; radius is
three. General explanation under the literal-color premise: every new edge
requires equality of two constants/literals, a condition on at most two variables.
NAE on three variables projects onto every assignment on any two variables.
Thus an edge monochromatic on all six NAE assignments is monochromatic on all
eight assignments. Their conjunction cannot discard just the all-equal cases.
This is a conditional obstruction to retaining those specific extensions, not
a general impossibility theorem for edge additions with changed internal colors.
## Next action
Allow new internal extensions and test arbitrary bipartite edge additions to
this assembled wire, with explicit counterexamples and a finite candidate cap.

Experience extraction (retrospective, 2026-09-15): created
[Preserving literal-colored extensions by adding edges cannot enforce NAE](../../../../research/experience/literal-colored-edge-additions-cannot-enforce-nae.md).
This entry was saved after round 040; no earlier retrieval is claimed.
