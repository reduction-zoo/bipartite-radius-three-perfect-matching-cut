# Round 001: third-layer ports without auxiliary vertices

Record reconstructed from the executed scripts and logs on 2026-09-14.
This scope was used in the experiment but was not recorded in this format
before execution. No prospective budget is claimed for the earlier run.

Hypothesis: a fixed shared crossing center edge can support the complete NAE
relation on three third-layer ports using only first- and second-layer auxiliaries.
Scope: four templates, with zero through three first-layer auxiliaries, orders
8, 10, 12 and 14. Every permitted optional edge is represented in Z3. End when
the finite list is exhausted or a graph with exactly the required relation is found.

Result: four synthesis queries returned UNSAT; zero candidate graphs or complete
reduction algorithms were produced. Stage reached: Propose. No source-instance
or recovery tests were applicable. No command retry or implementation repair is
recorded for this experiment. Per-round elapsed time and token usage are unavailable.

Command from this directory: `python3 center_search.py`. Evidence:
[script](center_search.py), [results](center-search.json), [log](center-search.log).

Initial feedback suggested adding third-layer auxiliary vertices; round 002
changed that premise and tested a new family. The later
[fixed center-edge lemma](../001/fixed-center-proof.md) explains the original failure at
all sizes: the required NAE assignments have different third-layer zero counts.
This explanation was developed after the experiments, not known at round entry.
Decision: reject this interface and test the expanded family in round 002.
