# Round 004: exclude whole forbidden boundary patterns

Status: completed; scope declared before execution.
User allocation: ten total rounds, preserving rounds 001–003.
Hypothesis: round 003 spent its budget excluding individual internal witnesses;
excluding all completions of the same bad port pattern may settle the template.
Use the fixed-center color-count experience and round 003's 64 all-equal failures.
Keep the same six complementary ports, |F|=3 and 16/18-vertex templates.
Change only the refinement rule: enumerate all 2^7 or 2^8 second-layer colorings
for each bad boundary pattern and forbid every legal extension. Up to 32
candidate graphs per template. Exact UNSAT, a checked relation, or candidate
exhaustion closes the round; no timeouts. Original Karp endpoints are unchanged.

Result: both templates are UNSAT after one candidate and one whole-boundary
exclusion each: four synthesis queries and two target-oracle queries total.
See result-1.json, result-2.json and search.log. The search completed without
repairs or timeouts. The total measured search-function time was 105.771 seconds.
Unlike round 003's budget exhaustion, this is exact solver exclusion of these
two declared templates, not a checked proof certificate or a general theorem.
Boundary-wide refinement settled the cases using fewer candidates, but consumed
more wall time than round 003's weaker refinement. No speedup claim is warranted.
Next: examine whether terminal crossing budgets can change the obstruction.
