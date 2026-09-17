# Executable verification

Prepared suite passed 9 cases with 16 recovery calls; largest target order 4182.
[Raw prepared evidence](../rounds/001/prepared.json). Two solver matchings per YES
case were each supplied in both list orders; serialization reversals are not
additional distinct matchings. The four YES and five NO source cases passed.

The separately implemented verifier passed 15 cases, 7 YES and 8 NO,
with 14 recoveries and largest target order 3742.
[Raw additional evidence](../rounds/001/verification.json). Sources were enumerated
by edge subsets; actual target matchings came from an independent Z3 encoding
and were recounted directly before recovery. Neither checker imports candidate
code. The additional family is all connected bipartite atlas graphs through five
vertices, C6, the six-vertex ladder, C8 and P8. Families overlap the prepared suite.

Commands from repository root:

```sh
python3 campaigns/bipartite-radius-three-disconnected-perfect-matching/work/check.py --candidate campaigns/bipartite-radius-three-disconnected-perfect-matching/work/algorithm.py
python3 campaigns/bipartite-radius-three-disconnected-perfect-matching/work/verify.py --candidate campaigns/bipartite-radius-three-disconnected-perfect-matching/work/algorithm.py
```

No candidate or checker repair, inconclusive solver result, randomness or timeout
occurred in these runs. General correctness requires the separate proof; finite
checks do not establish the theorem. The [independent review](../reviews/complete-rule/review.md) advanced without
repair. Its own three full cases and three distinct matching recoveries passed;
see its separate checks.json. Finite samples had two deletion components, while
the general recovery proof covers arbitrary component counts.
