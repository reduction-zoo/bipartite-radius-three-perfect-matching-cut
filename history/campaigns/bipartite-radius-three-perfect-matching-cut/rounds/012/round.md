# Round 012: can an intact cube approach a leaf-saturated center?

Status: completed; declared before execution.
Action: Investigate a general obstruction suggested by round 011. Suppose a
bipartite graph contains an intact cube whose vertices already have one internal
crossing edge in the target coloring, and a distinct leaf-saturated center u.
Can every cube vertex be within distance three of u? Derive a proof and check
all 16 graphs obtained by attaching u to a subset of one cube side and adding
its private leaf. Enumerate all 1024 colorings per connected graph; distinguish
u's eccentricity from the radius of the whole graph. End with a proof or a
counterexample under these exact premises. The previous center-layer experience
suggests checking saturation before adding shortcut auxiliaries. No full rule.

Result: the proposed obstruction is FALSE. The first assertion failed on mask 3:
attach center 8 to cube vertices 1 and 2 and leaf 9. Coloring
(0,0,0,0,1,1,1,1,0,1) is a perfect cut; the center has eccentricity three.
The mistaken reasoning overlooked that cube vertices can themselves lie in L1
and supply the internal crossing edges into L2. No prior proved lemma is refuted.
After this mathematical counterexample, the same declared enumeration was rerun
to collect all records: 15 connected graphs, 15360 colorings, 11 graphs with
center eccentricity <=3, 36 intact-cube witnesses across all connected graphs.
Six masks gave short-center counterexamples. check.log preserves the explicit
witnesses and edges. The original failed assertion and rerun are disclosed here;
they are not another round. No general impossibility or novel rule is claimed.
Next ask which assignments these successful attachments exclude, rather than
abandoning intact cubes because of the disproved conjecture.
