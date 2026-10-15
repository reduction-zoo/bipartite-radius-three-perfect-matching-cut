# Candidate verification

The unchanged `algorithm.py` passed the prepared suite: 8 source cases,
20 independently obtained target witness recoveries. See
[prepared-check.json](../rounds/001/prepared-check.json). The arithmetic-encoding
run was interrupted and is not a pass; the native-cardinality rerun is the completed
run. The encoding change and repeated self-test are documented in preparation.

A separately implemented `verify.py` imports neither the candidate nor prepared
checker. It brute-forces source witnesses, validates actual target structure,
uses native Z3 cardinality constraints, recounts witnesses directly, and tests
both returned colors and their complements through actual extractor subprocesses.
All 18 instances passed (14 YES and 4 NO),
with 56 recoveries. Largest additional output: 3628
vertices and 8331 edges. See
[verification.json](../rounds/001/verification.json).

The additional family is all connected bipartite atlas graphs through five
vertices, four explicit six-vertex graphs, and three explicit radius-four trees.
Counts are executed cases, not mutually disjoint graph families. No source
randomness or timeout was used. No algorithm repair was needed.

Reproduce from repository root:

```sh
python3 campaigns/bipartite-radius-three-matching-cut/work/check.py --candidate campaigns/bipartite-radius-three-matching-cut/work/algorithm.py
python3 campaigns/bipartite-radius-three-matching-cut/work/verify.py --candidate campaigns/bipartite-radius-three-matching-cut/work/algorithm.py
```

Finite tests do not establish correctness for all inputs. `proof.md` supplies
separate general arguments, including nontriviality, the source encoding,
universal recovery and radius. The [independent review](../reviews/complete-rule/review.md) advanced with no
required repair. Its separate checks and coverage are recorded there; the
reviewer imported none of the author implementations. Human review is pending.
