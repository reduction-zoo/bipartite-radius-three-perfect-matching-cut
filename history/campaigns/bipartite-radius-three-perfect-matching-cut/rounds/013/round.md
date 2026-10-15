# Round 013: completeness of fixed cube shortcuts

Status: completed; declared before execution.
Action: Continue diagnosis from round 012. Hypothesis: although fixed shortcuts
admit some perfect cuts, any attachment to a leaf-saturated center at distance
at most three excludes some of the cube's six NAE port assignments. Scope:
use the same 15 connected attachment graphs, enumerate 1024 colorings each,
and project to binary cube ports 1,2,4 with center free. Check all valid target
colorings, not only colorings assumed to preserve the cube. Classify the relation
against full NAE. Stop with a counterexample or finite exclusion, then derive
its cause. This revisits completeness, not graph-size expansion. The older
fixed-center count does not explain these direct cube attachments.

Result: 15 graphs / 15360 colorings. A single attachment permits all six port
patterns but leaves center eccentricity four. Two attachments lower it to three
but permit just two patterns; three or four permit none. Records include all
relations. The center's private leaf forces all attachment vertices to agree;
the cube's six internal patterns have two vertices of each color on each side.
These fixed equality constraints discard legal assignments. This is a finite
classification of the declared family, not a theorem about all connectors.
Next reconsider the private leaf: let the center's mate participate in the
connector and test whether opposite-colored access paths preserve more freedom.
No code repairs, source injections or full candidate verification in this round.
