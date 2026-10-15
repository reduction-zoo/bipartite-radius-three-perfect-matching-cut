# Round 041: directed synthesis of three mate choices

## Plan
Status: completed. Action: Investigate.
The finite binary-mate observation in rounds 033–040 could hide a structural
obstruction to clauses. Instead of sampling graphs, synthesize one bipartite
graph with three perfect cuts sharing center edge (0,k), but assigning vertex 1
three distinct crossing neighbors. Test balanced orders 10,12,14,16; stop at the
first SAT graph or four UNSAT answers. Encode eccentricity <=3 directly via a
common root neighbor for every other left vertex and nonzero right degrees.
Retrieve fixed-center-edge-color-count: its fixed edge and bipartite premises
apply, but it does not itself prove binary choice. Complete gadget construction
and source recovery remain absent. Run python3 rounds/041/check.py from campaign
root; save result.json and check.log. No time or token measurement is available.

## Evidence and diagnosis
One synthesis query found a ten-vertex radius-three graph with three valid cuts
sharing (0,5) and distinct mates 6,7,8 for vertex 1. Direct predicates verify
all three witnesses and radius. This refutes the prior finite binary-choice
conjecture; previous sampling was not a structural exclusion. Only the first
order was needed. An initial path error prevented script creation; corrected
the working-directory-relative path, preserving path-error.log. It was not a
mathematical failed attempt.

Experience extraction: created [three mate choices](../../../../research/experience/three-mate-choices-at-radius-three.md).

## Next action
Use any counterexample to inspect how it realizes three choices; otherwise
analyze the shared-center restriction rather than increasing random samples.
