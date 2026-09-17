# Parser totality repair

The independent [review](../../../reviews/complete-rule/review.md) found that
Python's decimal-integer digit limit rejected a malformed 5,000-digit n before
source validation. The CLI now disables that limit using the native Python
setting, preserving arbitrary-precision input semantics. It also maps excessive
JSON nesting to C6: legal source objects have fixed shallow nesting, so a parser
RecursionError cannot exclude a legal source. Recovery still fails explicitly
on invalid input. The graph construction, decoding and mathematical proof did
not change. The original candidate and full-rule evidence are retained in
rounds/048; original reviewer failures remain in their review directory.

Run from campaign root: `python3 work/evidence/parser-totality/check.py`.
This is an implementation repair within round 048, not a new research attempt.
Experience extraction: none; this runtime-specific parsing repair supplies a
regression check, not a mathematical construction finding.
