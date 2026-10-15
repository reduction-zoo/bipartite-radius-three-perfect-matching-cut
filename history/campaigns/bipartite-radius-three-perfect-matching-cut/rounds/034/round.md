# Round 034: larger mate-choice probe with a positive control

## Plan
Status: completed. Action: Continue a structural diagnostic.
Generate 5000 bipartite graphs: orders 10 and 12, densities .2,.3,.4,.5,.6,
500 graphs per order/density, seed 3401, fixed crossing edge (0,n/2). Retain
connected graphs with center eccentricity <=3 and enumerate every balanced
normalized coloring. Check mate diversity and count distinct solutions. Positive
control: binary cube plus center 8 attached to cube vertex 1 and leaf 9; center
has eccentricity four and should preserve three cube modes. End at the finite
sample. Sampling is for discovery only, not part of any final algorithm.

## Evidence and diagnosis
5000 generated graphs; 1635 passed structural filtering, 267876 balanced-coloring
checks, 23 feasible sampled graphs. Their mate diversity is at most two and
coloring counts are one or two. The radius-four control has exactly three
normalized solutions, so the test can observe nonbinary behavior. This remains
finite evidence; neither two-valued mate choices nor tractability is proved for
all radius-three inputs. The sampling regime may miss structured examples.
## Next action
Look for a mathematical characterization of perfect cuts and the observed
solution restrictions, rather than drawing a conclusion from sparse random data.
