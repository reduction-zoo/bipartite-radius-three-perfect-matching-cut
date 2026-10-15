# Round 047: interacting signed exact-one clauses

## Plan
Status: completed. Action: Continue.
Use the selector and occurrence entries from round 046. Reuse its construction
with one occurrence pair per variable; arbitrary many monochromatic attachments
should not consume more crossing budget. Test all 36 unordered pairs (including
repetition) of the eight signed clauses on three variables, all eight input
assignments: 288 queries. This includes incompatible clauses and repeated use
of the same ports. Check target domain and direct witnesses. Run python3
rounds/047/check.py at campaign root, save check.log/result.json.
Time/token usage unavailable; full source encoding and proof remain missing.

## Evidence and diagnosis
All 36 two-clause graphs have legal radius-three structure. All 288 pinned
assignments agree with the signed exact-one predicate; 48 admit valid witnesses.
Repeated use of one saturated occurrence pair causes no observed interference.
Experience extraction: updated the selector entry with interacting-clause checks.
No experimental repairs. A subsequent closeout command used the wrong working
directory and failed before writing; it was corrected without rerunning research.

## Next action
Compose the existing NAE-to-exact-one source bridge if universal truth tables pass.
