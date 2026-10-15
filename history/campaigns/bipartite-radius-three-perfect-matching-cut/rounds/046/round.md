# Round 046: connect the selector to binary variables

## Plan
Status: completed. Action: Continue.
Retrieve the selector and occurrence-budget entries with their shared-center
checks. Build three one-occurrence binary wires, share center/mate with one
selector, and connect its three high ports to the complementary occurrence
ports. These edges force a one-hot relation on the three decoded bits. Test all
eight assignments for both all-positive and one-negative signed clauses (16
queries), checking radius and direct target witnesses. This changes the clause
mechanism: the selector supplies non-literal internal colors, outside round-037's
preserved-extension obstruction. Run python3 rounds/046/check.py at campaign root;
save check.log/result.json. Time/token usage unavailable.

## Evidence and diagnosis
Both signed exact-one truth tables pass all sixteen queries, with legal bipartite
radius-three graphs and directly valid target witnesses. The clause relation
works when attached to the binary wire in these instances. This is finite local
composition evidence, not a general reduction proof.
Experience extraction: updated the selector entry with the clause interface and
the occurrence entry with its successful tested use. No repairs.

## Next action
Test interacting signed clauses if both truth tables are exact.
