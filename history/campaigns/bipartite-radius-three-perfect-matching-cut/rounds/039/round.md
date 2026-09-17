# Round 039: verify the source bridge for an exact-one primitive

## Plan
Status: completed. Action: Investigate a missing logical prerequisite.
NAE(a,b,c) is OR(a,b,c) AND OR(not a,not b,not c). For each OR clause with
literals l1,l2,l3 introduce selectors s1,s2,s3 and slack bits t1,t2,t3;
require E(s1,s2,s3) and E(si,not li,ti) for i=1..3, where E means exactly one.
Scope: prove both directions and deterministic witness recovery; test all sixteen
formulas made from triples on four variables, plus the zero-variable empty
formula and the Fano NO instance. Use Z3 and direct recovered-source checking.
This is an elementary intermediate encoding, not an original discovery or the
campaign's final target. Signed literal inputs would use complementary wire
ports if a suitable exact-one graph gadget is later obtained. End after 18 pairs.

## Evidence and diagnosis
18 formula pairs / 54 solver queries; 17 YES and one Fano NO. All universal
invalid-recovery queries were UNSAT. General proof: E(si,not li,ti) says
ti=li-si, hence si<=li. Exactly one selector is true, so the OR clause is true.
Conversely choose the first true literal, set its selector one and all others
zero, and set ti=li-si. Apply to both OR clauses for each NAE constraint.
Recovery reads the original variables from any valid target witness. Construction
uses n+12m variables and 8m exact-one constraints, O(n+m) word operations and
O((n+m)log(n+m+1)) bits; recovery O(n). This is an intermediate logical encoding
only, without a novelty claim. No radius-three exact-one graph primitive exists
in the tested templates, so it does not complete the campaign.
## Next action
Finish the allocated investigation by testing whether the binary-mate observation
survives a generator that guarantees perfect cuts instead of mostly NO graphs.
