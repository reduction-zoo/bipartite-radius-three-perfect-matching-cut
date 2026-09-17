# Round 007: separate anchors for second-layer logical ports

Status: completed; declared before execution.
Hypothesis: the L2 interface can work once each freely colored port has its
own zero L1 anchor. Round 006's crossing-budget argument requires at least
three distinct anchors. Test (ordinary L1,L3)=(3,3),(3,4),(4,3), graph orders
14,16,16, with the same full NAE relation and fixed center edge as round 006.
Normalize the distinct anchor assignment by symmetry: port i has exactly anchor
i in L1 and no edge to h. Other edges remain optional. This follows from the
required six positive assignments, not a weakening of acceptance. Up to eight
candidate graphs per template with whole-boundary exclusions; no timeouts.
End on exact local relation or finite exhaustion. Global composition remains open.

Result: all three templates returned UNSAT after one candidate and one forbidden
boundary pattern each (six synthesis and three oracle queries). Distinct anchors
remove the earlier positive-extension impossibility but are not sufficient for
an exact NAE relation in these sizes. Logs and actual counterexamples are saved.
Next change a structural premise: allow the center's crossing neighbor to depend
on the assignment. Such a local relation would require a new composition argument.
