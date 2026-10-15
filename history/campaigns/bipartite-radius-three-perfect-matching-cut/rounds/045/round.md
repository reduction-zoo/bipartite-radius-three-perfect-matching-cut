# Round 045: binary wire with externally shared center

## Plan
Status: completed. Action: Investigate.
Retrieve occurrence-ports-exhaust-crossing-budget. Its prior check relaxed only
occurrences; selector attachment also shares center and mate, so its premises
need extension. Reuse the nine round-028 graphs and query with <=1 internal
counts at 0,1 and occurrences, exact one elsewhere. Look for changed center
mate, unsaturated occurrences or inconsistent bits. Nine queries. Run python3
rounds/045/check.py from campaign root, saving check.log/result.json.
Time/token usage unavailable. Complete clause composition remains missing.

## Evidence and diagnosis
All nine queries were UNSAT. The wire retains its mate, complementary variables
and internally saturated occurrences even when center and mate counts are relaxed.
This closes a missing premise in combining its center with selector copies.
Experience extraction: updated occurrence-ports-exhaust-crossing-budget with the
new finite boundary checks. No repairs. A general composition proof remains due.

## Next action
Join the two validated boundary types by monochromatic edges if checks pass.
