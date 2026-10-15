# Testing foundation

Status: prepared. `python3 check.py --self-test` exited zero; see self-test.log.
Z3 5.1.0 supplies both decision oracles; NetworkX 3.6.1 checks graph structure
and radius. Each NAE clause forbids equality of its three Boolean variables.
Each target vertex has an integer sum of incident Boolean disagreements equal
to one. Thus feasible models are precisely the defined witnesses; direct Python
predicates recheck them. Only UNSAT means NO; unknown raises an execution error.
No numerical relaxation or wall-clock timeout is used.

Independent exhaustive enumeration cross-checked six source cases, including
an empty formula, unused variables, one clause, overlapping clauses, the Fano
plane and the Fano plane minus a line. It also cross-checked all 71 connected
bipartite atlas graphs of orders two through seven with radius at most three.
The Fano instance is NO; the other five sources are YES. The C6 check separates
perfect matching cuts from ordinary matching cuts and disconnected perfect
matchings. Four deliberately faulty executable fixtures were rejected: malformed
graph, wrong YES, wrong NO and invalid recovered assignment. Exact outputs and
witnesses are retained in self-test-evidence/. A valid executable control was
also accepted, with both K2 target witnesses passed through fresh recovery calls.

`python3 check.py --candidate algorithm.py` is ready for a complete rule. It
checks actual subprocess outputs, independently solves both endpoints, and
validates up to eight target models through fresh extraction processes. No
candidate exists yet, so there is no candidate verification claim. Larger
targets and malformed-source totalization will need candidate-specific checks.
