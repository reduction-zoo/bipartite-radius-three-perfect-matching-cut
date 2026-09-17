# Round 027: binary ports with a non-leaf center mate

## Plan
Status: completed. Action: Reconsider.
The leaf-center residual choices are matching-like. Let the mate h have an F
neighbor f, whose two third-layer ports p,r must have opposite colors. A zero
L2 vertex z should supply the crossing for the color-one port; two L2 occurrences
v,w use a K/q four-cycle to provide their own crossing edges and equal p,r.
Use vertices u,h,b,t,a,f,z,v,w,q,p,r numbered 0..11. Fixed edges:
u-h,u-b,u-a,b-t,h-f,f-p,f-r,z-b,z-a,z-p,z-r,a-v,a-w,q-v,q-w,p-v,r-w.
Scope: all 4096 colorings, normalize u=0, verify full PMC and radius <=3;
check that ports are complementary and both values occur. This supports variable
wiring only; a clause relation remains missing. The shared count lemma predicts
one zero in L3, consistent with p,r and q=1.

## Evidence and diagnosis
All 4096 colorings checked; four perfect cuts, two with u=0. Both port values
occur, ports are complementary, h=1, q=1, z=0, and v,w agree with p,r.
The graph has radius three. This is a binary interface, not a NAE clause or a
full reduction. Evidence in result.json and check.log; no novelty claim.
## Next action
Test independent variables and repeated occurrences under the shared center.
