# Round 022: compose the six-vertex synchronizers

## Plan
Status: completed. Action: Continue.
Replace each private synchronizer in round 019 with each of round 021's twelve
interfaces, preserving terminals 0,3 as twins and using four private internal
vertices. Scope: all 30 connected atlas graphs of order two through five,
12*30 transformations. Compare decisions and query for invalid decoded target
witnesses with Z3; measure connectivity and radius. This tests whether the local
size and leaf improvement resolves the global obstruction. No full source-NAE
construction is assumed. No applicable shared-center premise.

## Evidence and diagnosis
360 transformations / 1080 solver queries passed decision and finite-instance
universal recovery checks. All violate radius three; inspect check.log for the
observed range. Reducing gadget size and removing leaves did not fix distance.
## Next action
Investigate whether privacy and opposite-side equality themselves force radius
at least four, rather than enumerating larger synchronizers.
