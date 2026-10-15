# Independent complete-rule review

Date: 2026-09-15. Decision: **revise**.

The mathematical construction and universal recovery argument are supported. The
current executable fails the fixed totality contract on a concrete malformed
source string. This is a narrow parser repair, not a reason to replace the graph
construction or restart the campaign. Novelty is supported within the literature
coverage below; significance meets the fixed criterion. Neither judgment asserts
publication acceptance or exhaustive literature coverage.

## Correctness

### Required correction: forward parsing does not totalize every invalid string

Location: `work/algorithm.py:73–78`, especially the exception handler at line 75.
It catches `json.JSONDecodeError` only. The 5,034-byte source string consisting of
`{"n":`, 5,000 copies of the digit `1`, and `,"variables":[],"clauses":[]}` is
not a legal source because the explicit variable list does not have length n.
The executable exits with code 1, empty stdout, and:

```
ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5000 digits; use sys.set_int_max_str_digits() to increase the limit
```

It must instead emit the prescribed C6. The complete original input and process
output are record 28 (zero-based) in `process-records.json`. The runnable
`checks.py` reproduces the failure; `checks.log` retains its nonzero conclusion.
This contradicts the current statements “Malformed source encodings map to C6”
and “These cases make the forward map total” at `work/proof.md:116–120`. The
missing premise is that parsing either succeeds or raises JSONDecodeError; the
actual parser has another input-dependent failure mode.

Repair the integer parsing limit without imposing a new bound on the source
language. For example, disabling Python's decimal-integer digit limit permits
ordinary arbitrary-precision validation here. Simply interpreting every
oversized integer as invalid needs a justification relative to the unrestricted
mathematical encoding. Recheck this exact input and normal valid/invalid cases;
retain existing graph and proof evidence when unchanged. Other invalid probes,
including a 1,200-level nested non-object, did emit C6 in the tested runtime.
No deep-nesting failure is claimed.

### General proof audit

The source transformation (`proof.md:11–23`) is valid: exact-one selectors
choose a true literal, and each slack equation enforces selector <= literal.
Choosing the first true literal supplies a deterministic extension. The two OR
conditions are precisely positive NAE, with disjoint auxiliaries. Implementation
lines 27–34 produce the same signs and freshness conditions.

The selector argument (`proof.md:41–57`) proves the necessary robust relation.
If A differs from u, its three d neighbors coincide with A and the three
opposite-neighbor equations on d imply an odd number equals twice an integer.
Otherwise A forces one-hot d, which forces complementary T and F=h=1 after
normalization. Every T is already saturated. This argument uses exact internal
counts only at vertices with no external neighbors. Its relaxed counts at u,h,T
are legitimate restrictions of a full witness. It does not presuppose uh crosses.

The variable argument (`proof.md:61–74`) is also valid. After a selector forces
uh to cross, u forces a=b=0 and h forces f=1. The leaf t supplies b's crossing
edge, so every z=0 even when b is shared. Setting q=0 either gives a port two
crossing neighbors or leaves q unmatched; thus q=1. The two fixed opposite
neighbors a,q saturate each occurrence port, forcing p=v and r=w. Vertex a then
forces these two bits to differ. In the converse, f and q each also have exactly
one crossing neighbor because the two bits differ. Repeated attachments do not
consume any further budget.

Composition (`proof.md:78–95`) consequently applies to **every** full target
witness. Positive literals attach to w=1-p, negative literals to v=p, so the
selector imposes exact-one on the signed literals. Reading p relative to u then
satisfies each original NAE clause. The fresh-process implementation checks the
full graph coloring and returns exactly these normalized ports; it does not
choose or solve a source assignment. Complemented witnesses are covered. The
YES extension satisfies all shared-vertex budgets as well as each private block.
The NO implication is the contrapositive of universal recovery. Empty formulas
and their K2 recovery are correct, and C6 is a legal NO target by cut parity.

The stated layers (`proof.md:99–104`) cover every emitted edge, supply paths to
u of length at most three, and certify bipartiteness. Vertex labels are disjoint
between blocks; distinct T endpoints prevent duplicates even under repeated
clauses. Counts are 4+8n+160m vertices and 3+14n+304m edges for nonempty formulas.
There are linearly many records and logarithmic-length labels. The explicit
variables list prevents a binary-encoded n from hiding exponentially many unused
variables. Forward construction, validation and recovery are deterministic and
polynomial in encoded lengths; the stated conservative quadratic bit bounds are
reasonable once the parser issue is repaired. No oracle occurs in either map.

### Independent finite evidence

`checks.py` imports neither candidate nor existing checkers. It writes named
local graphs directly from the specification and executes the candidate only as
a subprocess. It checks:

- All 512 normalized selector assignments under the relaxed boundary contract:
  exactly three survive, with the proved one-hot and saturation relation.
- All 1,024 variable assignments pinned at u=0,h=1, relaxing u,h,b,v,w:
  exactly two survive, with complementary bits and saturated ports.
- Five injected source graphs: a single clause; seven repeated clauses plus two
  overlapping clauses on five variables; all ten triples on five variables
  (NO); and empty formulas with zero and four variables.
- Actual graph simplicity, bipartition, center distances and exact counts;
  source truth-table decisions versus independently encoded target SAT decisions.
- All eight fixed source projections for the one-clause target, and three SAT
  queries excluding **any** target witness with a monochromatic recovered source
  clause. Each bad-projection query is UNSAT. The scope is only these three
  finite graphs, not a general theorem.
- Eighteen fresh-process recoveries, including complemented witnesses; seven
  malformed-source probes, one of which fails as described above.

Original graphs and witnesses are in `full-checks.json`; local states are in
`local-states.json`; process I/O is in `process-records.json`. The first reviewer
checker run queried a model after pop without a fresh solver check. Its error is
preserved in `checker-initial-error.log`; the checker was corrected and rerun.
That was a reviewer-harness error, not candidate evidence. No timeouts were used.

I inspected the prepared and additional checking interfaces and retained their
passing logs, including the 38-case additional run and 134 recoveries. The new
checks target relaxed interfaces, projections and parsing instead of repeating
all earlier cases. Finite evidence supplements the argument above.

The shared experience entries `three-mate-choices-at-radius-three.md` and
`occurrence-ports-exhaust-crossing-budget.md` were inspected along with the
round-029 supporting argument and current proof. Their applicable claims are
restricted to these particular gadgets. The current proof supplies the
shared-center premises needed here; no unsupported transfer to arbitrary gadgets
or external attachments at private interior vertices is used.

## Novelty

Search date: 2026-09-15. Independent searches were:

- `"Perfect Matching Cut" "radius 3"`
- `"Perfect Matching Cut" "radius three"`
- `"perfect matching cut" bipartite radius 2026 2025 -site:emergentmind.com`
- `"disconnected perfect matching" "radius" 2026 -site:emergentmind.com`

Primary evidence:

1. [Lucke, arXiv:2501.08735v1](https://arxiv.org/html/2501.08735v1), Theorems
   18–19, Claims 20–21, and **Section 5**, Open Problem 2. The paper's positive
   NAE source and cube-based radius-four construction are different from the
   candidate's shared-center exact-one selectors and binary ports. Open Problem
   2 explicitly asks the bipartite radius-three PMC case. Theorem 22 concerns
   d-Cut for d>=2. Theorems 23–24 concern maximum matching-cut variants, whose
   selected cut need not saturate the whole graph; they do not imply this result.
   The [arXiv record](https://arxiv.org/abs/2501.08735) lists only v1.
2. [Lucke, Paulusma and Ries, Finding Matching Cuts in H-Free Graphs](https://link.springer.com/article/10.1007/s00453-023-01137-9),
   Theorem 21: PMC is polynomial-time solvable on graphs of radius at most two.
   This is the relevant lower-radius baseline.
3. [Dichotomies for Maximum Matching Cut](https://durham-repository.worktribe.com/OutputFile/2851394),
   Section 1 and Theorem 3 distinguish the known general-graph radius-three
   PMC hardness from the bipartite restriction. That theorem alone does not
   preserve bipartiteness. Its PMC/Disconnected Perfect Matching distinction
   also prevents importing hardness for the latter predicate.
4. [Le and Telle, The Perfect Matching Cut Problem Revisited](https://arxiv.org/abs/2107.06399),
   abstract: subcubic bipartite hardness and large girth, with no bounded-radius
   assertion. This is not a same-endpoint theorem.
5. [Lucke's publications](https://felicialucke.github.io/publications.html) lists
   2026 publications and preprints; no radius-three PMC resolution was identified.

The published TCS [record](https://www.sciencedirect.com/science/article/pii/S0304397525003676)
was found, but direct publisher access returned HTTP 403 and the
[university PDF](https://durham-repository.worktribe.com/OutputFile/4275060) could
not be fetched through the review browser. A newer relevant
[JCSS record](https://doi.org/10.1016/j.jcss.2025.103723) on induced paths/cycles
was also found through search, but its full text returned HTTP 403. These
inaccessible texts were not independently verified in full here. Round 050's
literature report was read; its attribution of the arXiv conclusion to Section
6 should be corrected to Section 5. Its theorem and open-problem identifiers are
otherwise consistent with the inspected version.

No prior same-endpoint reduction or implication was located within this coverage.
The candidate's concrete contribution is the combination of robust shared-center
selectors with binary saturated ports that places the whole construction within
three layers. The Boolean source encoding and saturation principle alone are not
novelty claims. Unindexed, unpublished, inaccessible and overlooked work remain
outside coverage; absence from search does not prove nonexistence of a result.
The evidence supports proceeding to expert novelty assessment after repair.

## Significance and disposition

The fixed task asks for a new Karp reduction to connected simple bipartite graphs
of radius at most three, with universal polynomial witness recovery. The graph
construction meets those mathematical requirements and, with the known
radius-two algorithm, would settle the corresponding PMC boundary. This is a
concrete complexity classification contribution, rather than an optimization of
an existing implementation or a partial gadget. It says nothing by itself about
Matching Cut or Disconnected Perfect Matching. NP membership follows from direct
checking of graph structure and one opposite neighbor per vertex.

**Required before advance:** repair the integer-parser totality failure, preserve
the source language, pass the targeted regression and relevant normal-input
checks, and submit the narrow changed behavior for follow-up review. Correct the
Section 5 literature locator when updating the report. The mathematical and
literature findings above can be reused if the candidate construction is unchanged.
