# Round 006: logical ports in the second layer

Status: completed; declared before execution.
Use rounds 004–005: third-layer dual rails failed in the tested exact templates,
and mixed terminal budgets do not remove the count obstruction. New hypothesis:
place three single logical ports in layer two, with remaining second-layer and
third-layer vertices able to compensate color counts. All vertices again have
exactly one crossing; keep uh crossing. Test (ordinary L1,L3) sizes (1,3),
(2,2),(2,3), with |L2|=|L1 minus h|+|L3|; graph orders 10,10,12.
All L2-to-L1/L3 edges are optional subject to the distance requirements. Seek
exactly the six NAE patterns on the first three L2 vertices. Use whole-boundary
exclusion, up to eight candidates per template; stop at a checked local relation
or exhaustion. No degree bound, no timeouts. Composition is not presumed.

Result: all three templates returned UNSAT from their positive-extension
constraints alone (three synthesis queries, zero candidate graphs). No full
rule was produced. Each logical L2 port must be able to take color one, so
it cannot touch h and must have exactly one neighbor among the zero L1 vertices.
Every pair of ports is simultaneously one in a required NAE assignment; they
therefore cannot share that neighbor, whose crossing budget is one. Hence at
least three ordinary L1 neighbors are necessary. This proves why the tested
one/two-anchor templates cannot work, without extending their finite UNSAT
results to the entire question. Next use three separate anchors.
