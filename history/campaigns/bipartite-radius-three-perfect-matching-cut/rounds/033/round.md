# Round 033: can a fixed-center vertex have three different crossing mates?

## Plan
Status: completed. Action: Investigate.
Hypothesis to test, not assume: fixed-center radius-three PMC instances might
only admit binary mate choices. Exhaust all 32768 subgraphs of K4,4 containing
edge (0,4), retaining connected graphs with eccentricity(0)<=3. Enumerate all
balanced colorings with c(0)=0,c(4)=1; balance is necessary because the crossing
edges form a perfect matching across the bipartition. Look for any vertex with
three distinct mates across valid colorings; also record coloring counts.
End after this finite domain. A lack of examples is not a general theorem.
This diagnosis targets clause expressiveness rather than another template size.

## Evidence and diagnosis
32768 edge masks / 655360 balanced-coloring checks. Among 1584 feasible connected
graphs with center eccentricity <=3, coloring counts are one or two, and maximum
mate diversity is two. This does not prove a binary-choice theorem. The domain
is only K4,4 with one fixed crossing center edge.
## Next action
Test larger sampled graphs and include an explicit radius-four control with
three cube choices so the diagnostic is capable of seeing the missing behavior.
