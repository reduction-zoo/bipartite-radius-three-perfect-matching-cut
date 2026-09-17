# Round 028: shared-center binary variables with repeated occurrences

## Plan
Status: completed. Action: Continue.
Share u,h,b,t between variable gadgets; retain f,p,r,z per variable and create
an a,v,w,q four-cycle per occurrence. Link z to the first a and to b,p,r.
Scope: variable counts 1,2,3 and occurrence counts 1,2,4, nine constructions.
For every variable assignment query a normalized target extension; query also
for any normalized target with h!=1, unequal occurrence/port colors, or equal
paired ports. Check exact target legality and radius. A scalable variable wire
would justify attempting a clause interface; it is not a complete reduction.

## Evidence and diagnosis
Nine constructions through 64 vertices / 51 solver queries. All 42 binary
assignments extend; nine bad-consistency queries were UNSAT. All centers have
eccentricity <=3. Finite evidence only. The components share u,h,b,t without
coupling the independent bits in these tests. No clause is encoded.
## Next action
Challenge external attachment: replace occurrence budgets by at-most-one and
ask whether new clause edges could alter the internal wire behavior.
