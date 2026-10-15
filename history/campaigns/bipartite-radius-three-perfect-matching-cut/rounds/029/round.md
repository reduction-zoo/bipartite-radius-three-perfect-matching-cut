# Round 029: robustness of occurrence ports under external attachment

## Plan
Status: completed. Action: Investigate.
The round-028 whole-wire tests assume all internal budgets are exactly one.
A clause attachment could spend the port's budget outside instead. On the same
nine graphs, allow occurrence v,w internal crossing counts <=1 and retain exact
one at other vertices. Query for a zero-budget occurrence or inconsistent bits
with u=0. Reuse the 42 positive assignments from round 028. End with a counterexample
or a proof of robustness supported by nine queries. No larger construction scope.

## Evidence and diagnosis
Nine relaxed-boundary queries are UNSAT. Supporting argument: if u=0 and a=0,
q cannot be zero: a color-one occurrence would have two opposite neighbors a,q,
while both occurrences zero leave q unmatched. Hence q=1; a,q force each
occurrence to spend exactly one crossing internally. If u-b crossed, every a
would be zero and b's already consumed budget would force z=1; the first a would
then see both z and one occurrence as opposite, a contradiction. If u-a crossed,
that a forces its two occurrences one, leaving q unable to have exactly one
opposite neighbor. Thus u-h crosses, b and all a are zero. The saturated b
forces z=0; f adjacent h is one, forcing complementary p,r. Port-occurrence
edges must be monochromatic, giving consistency. Author-side general argument;
no independent review or novelty assessment. This justifies zero additional
crossing budgets at occurrence terminals in a separate clause gadget.
## Next action
Synthesize a NAE clause with these actual zero-budget L2 occurrence terminals.

Experience extraction (retrospective, 2026-09-15): created
[Occurrence ports exhaust their crossing budget inside the variable wire](../../../../research/experience/occurrence-ports-exhaust-crossing-budget.md).
This entry was saved after round 040; no earlier retrieval is claimed.
