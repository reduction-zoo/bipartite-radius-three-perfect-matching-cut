# Round 002: additional third-layer auxiliaries

Record reconstructed from the executed scripts and logs on 2026-09-14.
The original search was finite; its round budget was not established prospectively.

Hypothesis: third-layer auxiliary vertices can absorb changes in the number of
zero-colored ports while preserving a fixed shared crossing center edge.
Change from round 001: allow one or two non-port vertices in the third layer.
Scope: (first-layer auxiliaries, third-layer auxiliaries) equal to (0,1), (1,1),
(2,1), (0,2), (1,2); five templates of orders ten through fourteen. End when
these templates are exhausted or the exact NAE relation is realized.

Result: five synthesis queries returned UNSAT; zero candidate graphs or complete
rules. Stage reached: Propose. No whole-rule source instances or recovery calls
were applicable. No command retry or implementation repair is recorded for this
experiment. Per-round elapsed time and token usage are unavailable.

Commands from this directory: `python3 center_search.py` and
`python3 obstruction_check.py`. Evidence: [synthesis script](center_search.py),
[results](center-search.json), [synthesis log](center-search.log),
[structural check](obstruction_check.py), [check log](obstruction-check.log).
The structural check covered 33 feasible center/mate choices and 34 colorings,
including nine leaf-mate colorings, on atlas graphs through order seven.

New mathematical information: the [general lemma](../001/fixed-center-proof.md) fixes
the third-layer zero count. It explains round 001 but does not exclude all
expanded interfaces. Round 002 excludes only the five stated templates.

Decision: stop discovery on this topic for now. No supported replacement
interface has been identified; expanding size alone is not a justified third
round. Resume only with a concrete mechanism that uses the count constraint.
The mathematical question remains open within the recorded literature coverage.

## Experience consolidation

After round closure, the fixed center-edge lemma was recorded as
[shared experience](../../../../research/experience/fixed-center-edge-color-count.md).
It remains an author-side proof awaiting independent review. This is retrospective
consolidation, not a new round, a prior retrieved input, or measured transfer.
No subsequent use has yet been observed.
