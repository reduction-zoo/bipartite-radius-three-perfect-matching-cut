# Round 031: exact-one primitive instead of a direct NAE clause

## Plan
Status: completed. Action: Reconsider.
Keep round 030's two templates and boundary budgets but require exactly one of
the three terminals to be one. This changes the logical primitive, not the fixed
campaign endpoints. If it succeeds, an explicit NAE-to-primitive gadget and
witness recovery must be constructed before any full reduction claim. If both
templates fail, compare a different primitive rather than asserting the clause
family impossible. Scope: (b,f)=(1,3),(2,3), at most eight candidates per template;
whole-boundary exclusions, no timeouts. No directly applicable experience entry.

## Evidence and diagnosis
Both exact-one templates returned UNSAT after one candidate and one forbidden
boundary pattern, six queries total. This excludes these two templates, not
other exact-one encodings. No source conversion or reduction was constructed.
## Next action
Change where the clause meets the wire: use an extra L3 vertex per occurrence,
whose color is pinned by the saturated L2 occurrence but whose crossing must be
supplied by the clause. This returns to the old L3 interface with a now-tested
variable composition; expand only one previously untested template.
