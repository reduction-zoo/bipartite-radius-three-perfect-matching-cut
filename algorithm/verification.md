# Verification of the complete reduction rule

Candidate: [algorithm.py](algorithm.py), with [general proof](../paper/proof.md).
The parser-only repair is included in the following current checks. The prepared oracle
foundation was reused without modification or a redundant self-test run.

From the campaign root:
- `python3 work/check.py --candidate work/algorithm.py`: six prepared cases pass,
  with 28 fresh-process witness recoveries; [log](../history/campaigns/bipartite-radius-three-perfect-matching-cut/work/evidence/parser-totality/prepared-check.log) and
  [per-case evidence](candidate-evidence).
- `python3 work/verify.py --candidate work/algorithm.py`: 38 additional cases,
  35 YES and three NO, 140 target solver queries and 134 fresh-process recoveries;
  maximum target order 2628. See [log](../history/campaigns/bipartite-radius-three-perfect-matching-cut/work/evidence-full-rule.log) and
  [actual outputs and witnesses](../history/campaigns/bipartite-radius-three-perfect-matching-cut/work/evidence/full-rule).

The additional checker independently enumerates source assignments, validates
actual emitted graph encodings and center distances, and uses a separately
written exact-one crossing predicate in Z3. It imports neither the candidate
nor check.py. Cases include all subsets of four positive triples on four
variables, Fano and duplicated/reordered variants, repeated clauses, empty and
unused-variable cases, and seeded random formulas (seed 4801). The candidate's
claimed exact vertex and edge counts pass for every nonempty formula tested.
The initial valid-source suites passed. Independent review then found an
oversized-integer parse failure; the [repair](../history/campaigns/bipartite-radius-three-perfect-matching-cut/work/evidence/parser-totality/repair.md)
and [five parser regressions](../history/campaigns/bipartite-radius-three-perfect-matching-cut/work/evidence/parser-totality/check.log) pass. Both
full-rule suites also pass after that repair. The graph and recovery formulas
are unchanged. Original logs and candidate remain under rounds/048. Source enumeration is bounded
at eight variables. Up to four target witnesses per case are checked here;
these finite checks are not a universal witness proof. The general proof is
required for untested sizes and witnesses, and [independent follow-up](../history/campaigns/bipartite-radius-three-perfect-matching-cut/reviews/parser-followup/review.md) has advanced.
