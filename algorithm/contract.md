# Executable contract

Source: a JSON object with exactly `n`, `variables` and `clauses`. The integer n is nonnegative;
each clause is a list of three distinct integer variable indices in [0,n).
Duplicates across clauses, empty formulas and unused variables are allowed.
The variables field must be the explicit list [0, ..., n-1], so the input
length is at least n, including unused variables. Integer labels are binary
encoded mathematically; JSON uses decimal integer strings.
A source witness is an n-element list of integer bits satisfying NAE in every
clause. Empty formulas admit the empty assignment when n=0.

Target: exactly `n` and `edges`, encoding a connected simple undirected graph
on [0,n), with n>=2, bipartite and radius at most three. Each edge lists two
distinct valid integer indices; unordered duplicate edges are invalid.
A target witness is an n-element list of integer bits with both colors present
and exactly one opposite neighbor at every vertex. C6 is a legal NO instance;
K2 is a legal YES instance. Boolean JSON values do not count as integer indices.

`python3 algorithm.py` reads one source object and writes the actual target.
Malformed source encodings map to C6 under the total Karp contract. With
`--extract`, it reads exactly `source` and `target_solution` and returns a source
witness. Invalid recovery premises fail explicitly. Both modes run in fresh
processes with no hidden state. Diagnostics go to stderr, execution failures
exit nonzero. No solver calls are allowed in the eventual reduction algorithms.

The test harness uses independently solved target witnesses, at most eight
models per YES target, including complements where encountered. It checks the
actual graph and the recovered source predicate. Finite checks do not prove
universal recovery. 