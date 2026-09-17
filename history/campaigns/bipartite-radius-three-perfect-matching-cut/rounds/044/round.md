# Round 044: selector ports and shared-center budgets

## Plan
Status: completed. Action: Investigate.
Use the exact selector relation from the three-mate entry, but relax the internal
crossing counts at center 0, its mate 1, and all high ports to <=1. These are
exactly the vertices used for shared-center clause composition and external wire
attachments. On the three round-043 graphs, query for an unused high-port budget,
a wrong relation, or a changed center edge. Require exact one elsewhere. Three
queries; retain positive evidence from round 043. Run python3 rounds/044/check.py
at campaign root; save check.log/result.json. Time/token usage unavailable.

## Evidence and diagnosis
Three relaxed-boundary queries were UNSAT. Even with shared-center and high-port
budgets relaxed, the tested graphs force the original center edge, complementary
one-hot relation and saturated high ports. Thus external edges at those ports
must be monochromatic. Evidence is finite, awaiting a general interface proof.
Experience extraction: updated the three-mate entry with the boundary premises
and three checks. No repairs or preparation rerun.

## Next action
Check the existing binary wire under the same shared-center relaxation.
