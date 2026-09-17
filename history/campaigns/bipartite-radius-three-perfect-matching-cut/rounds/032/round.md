# Round 032: third-layer clause ports supplied by the variable wire

## Plan
Status: completed. Action: Reconsider.
Attach a new L3 clause port to each saturated L2 occurrence from round 029.
That edge must be monochromatic, so the port encodes the variable but retains
its full crossing budget for the clause. Reuse the round-002 synthesis model
with two L1 anchors and two auxiliary L3 vertices, an untested order-16 template.
This is a same-center refinement, not a new independent route; the new reason
for considering it is the tested variable and occurrence composition.
Scope: exactly (b,t)=(2,2), all eight boundary patterns and all 512 interior
colorings per forbidden pattern. One exact synthesis query; exhaustively check
any SAT witness. A valid local clause still requires full formula injection.

## Evidence and diagnosis
One exact synthesis query returned UNSAT (16 vertices, 56 optional edges).
The previously available small-clause exclusions remain unchanged. Variable
wiring is now supported, but neither tested attachment interface supplies a
clause. No complete rule or new source encoding was obtained.
## Next action
Instead of enlarging the templates, inspect the solution structure of small
radius-three graphs with a fixed center edge. Multiple independent binary
choices may fail to provide the three alternatives a clause needs.
