# Round 043: compose selectors at one center edge

## Plan
Status: completed. Action: Continue.
Retrieve the three-mate entry's exact local relation. Share vertices 0 and 5
across one, two and three copies; all other vertices remain private. Test all
3^n intended independent selector choices and one bad-relation query per graph.
Check connected bipartite radius <=3. This tests whether the selector survives
composition before treating it as a clause. Run python3 rounds/043/check.py at
campaign root; save check.log/result.json. Time/token usage unavailable.

## Evidence and diagnosis
All three graphs have center eccentricity three and are bipartite. All 39
independent selector assignments extend; three bad-relation queries are UNSAT
(42 queries total). Shared-center composition preserves the tested relation.
Experience extraction: updated the three-mate entry with composition evidence.
No repairs. Complete forward/recovery maps remain absent.

## Next action
Relax attachment budgets if independence passes.
