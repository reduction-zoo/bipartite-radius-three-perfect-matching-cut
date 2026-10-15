# Independent parser follow-up review

Date: 2026-09-15. Decision: **advance**.

The sole blocking finding in the [complete-rule review](../complete-rule/review.md)
is repaired. The current complete reduction is eligible for expert review.
This is not publication acceptance, and the earlier explicit literature-coverage
limitations remain in force.

## Correctness

I compared `work/algorithm.py` with the preserved original
`rounds/048/algorithm.py`. The only changes are the call to
`sys.set_int_max_str_digits(0)` before parsing and inclusion of `RecursionError`
in the parser exception handler. Graph construction, source validation, witness
validation and recovery are unchanged. The original proof audit, local boundary
checks, composition reasoning, target-domain proof and polynomial bit bounds are
therefore reused rather than rerun.

The integer-setting change removes the fixed decimal-digit restriction instead
of imposing a new bound on legal source integers. Arbitrary-precision parsing
remains polynomial in the input length. The exact previously failing 5,034-byte
input now exits zero and emits the prescribed C6. Oversized integer labels in
other fields are parsed and then rejected by the existing source predicate.

Mapping parser recursion failures to C6 preserves the source language: a legal
source has fixed shallow nesting (object, lists and clause lists); arbitrary
nested containers are not legal source encodings. This handler operates only at
input parsing, so it does not hide failures in graph construction or recovery.
Extraction mode re-raises parser errors and still rejects malformed premises.

My independently written `checks.py` imports no candidate or author checker.
It executes 15 fresh candidate processes and checks:

- The exact prior failure, read from the original preserved process record.
- Oversized negative n, variable label and clause label; malformed JSON; a
  1,200-level nested non-source; and a Boolean n. All seven invalid forward
  inputs emit C6 and exit zero.
- A valid empty formula on four variables and both K2 recovery witnesses.
- Two malformed recovery inputs, both rejected with nonzero exit and no output.
- The one-clause graph against the earlier independently retained actual output,
  followed by fresh recovery of two previously independently solved complementary
  witnesses and direct validation of the recovered NAE assignment.

The check passes. Original inputs, outputs and errors are retained in
`process-records.json`; the command output is in `checks.log`. No timeouts were
used. I also inspected the repair record and current author-side logs: the five
parser regressions, six prepared cases, and 38 additional cases pass; the latter
retain 134 fresh-process recoveries. These finite checks support implementation
consistency; the unchanged general proof establishes arbitrary-input and
universal-witness correctness.

## Novelty

The theorem and construction have not changed, so the primary-source assessment
and searches dated 2026-09-15 in the complete-rule review remain applicable.
No additional novelty search was needed for a parser repair. The candidate is
supported as a new same-endpoint reduction within that documented coverage;
inaccessible, unindexed, unpublished and overlooked work remain unresolved
coverage, not evidence of novelty. Round 050 now correctly locates Open Problem
2 in Section 5 of arXiv:2501.08735v1.

## Significance

The unchanged mathematical contribution remains a deterministic Karp reduction
from positive NAE-3-SAT to connected simple bipartite PMC at radius at most three,
with deterministic polynomial recovery from every valid target witness. Relative
to the radius-two tractability and radius-four hardness baselines already
checked, it addresses the fixed PMC radius boundary. This meets the campaign's
significance criterion. It establishes no corresponding result for ordinary
Matching Cut or Disconnected Perfect Matching.

No outstanding required repair was found in this follow-up. Advance to the
remaining research-write and expert-review preparation work under the existing
workflow, retaining the evidence boundaries above.
