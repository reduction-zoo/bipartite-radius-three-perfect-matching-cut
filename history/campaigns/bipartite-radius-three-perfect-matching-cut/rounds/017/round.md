# Round 017: decision preservation by the ordinary bipartite double cover

Status: completed; declared before execution.
Action: Investigate the prerequisite of round 016's alternate mechanism. For
each connected atlas graph of order two through five, replace each vertex v by
(v,0),(v,1) and each edge uv by u0-v1 and u1-v0. Compare PMC decisions using
the existing oracle without a radius-domain assumption. Record any false
positives, connectivity and radius, with witnesses. Scope: all such atlas graphs;
no expansion past five vertices. A counterexample rejects plain doubling but
may identify a synchronization requirement. This is a component test for the
fixed campaign, not a change of the campaign's Karp endpoints.

Result: 30 graphs, 60 solver queries, three NO-to-YES mismatches. The first
is a triangle with a pendant vertex; its double cover has radius three and a
valid cut. K4 is another counterexample: its double cover is the cube. Full
records and witnesses are in result.json. Plain duplication admits disagreeing
twin colors, so projecting one side cannot establish the reverse implication.
Bipartite inputs may also give disconnected covers. Next enforce equality of
twins with a monochromatic biclique while reserving their original crossing
budgets. No repair or rerun; this rejects the unsynchronized transformation.
