# Round 042: exact relation of the ten-vertex selector

## Plan
Status: completed. Action: Investigate.
Use the round-041 counterexample entry; the same center edge and full graph apply.
Enumerate all 1024 colorings and identify the normalized center-edge relations
on L2 vertices 2,3,4 and L3 vertices 6,7,8. Check if they are complementary
one-hot tuples, whether unwanted center mates exist, and which vertices could
serve as saturated clause ports. One graph, no solver or changed size scope.
Run python3 rounds/042/check.py from campaign root, saving check.log/result.json.
Full source recovery remains missing. Time/token usage unavailable.

## Evidence and diagnosis
All 1024 colorings were checked. Exactly six perfect cuts exist (three up to
complement), all using center edge (0,5). The tuple (2,3,4) is exactly one-hot;
(6,7,8) is its complement. No alternative center edge occurs.
Experience extraction: updated the three-mate entry with this exact local relation.
No executions failed and no solver queries were used.

## Next action
Compose independent copies if the local relation is exact.
