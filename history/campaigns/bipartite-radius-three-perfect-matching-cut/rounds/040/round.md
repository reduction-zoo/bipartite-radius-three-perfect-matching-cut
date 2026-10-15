# Round 040: planted perfect-cut graphs challenge the binary-choice observation

## Plan
Status: completed. Action: Investigate.
Round 034's unconditioned sample contained only 23 feasible graphs. Generate
600 guaranteed-PMC bipartite graphs: orders 12,14,16, densities .25,.5,.75,1,
50 graphs per order/density, seed 4001. Plant a balanced cut and a crossing
perfect matching containing (0,n/2), then sample only monochromatic additional
edges. Validate the planted witness before structural filtering. For connected
graphs with center eccentricity <=3, enumerate every balanced coloring with
that fixed center edge, recording mate diversity. End after 600 graphs and
close the forty-round allocation. This diagnoses a sampling bias; no general
binary-choice theorem will be inferred from a finite sample.

## Evidence and diagnosis
600 planted-PMC graphs; 463 connected, 284 with the required center eccentricity.
All planted witnesses were validated. Exhaustive fixed-center checks on eligible
graphs examined 431640 balanced colorings; solution counts were one or two and
maximum mate diversity two. The generator removes the mostly-NO bias of round
034, but its topology and finite sizes remain a coverage limitation. This does
not prove the binary-choice conjecture or settle radius-three PMC.

## Allocation assessment: rounds 021–040

Twenty new rounds completed in the same conversation. No construction reached
both fixed campaign endpoints. There were two focused literature rounds (025,
035), six Web queries total, and 1751 research solver queries. Direct enumeration,
graph-distance checks and planted-witness validation are reported separately in
their rounds. A closing audit added 28 solver queries on five saved synthesized
graphs: all positive extensions and five forbidden patterns/witnesses checked.
See ../../work/evidence/additional-rounds/audit.log. It does not certify UNSAT or
constitute independent review. No preparation rerun, timeouts or failed executions
occurred in this allocation. Full wall time and token usage were not measured.

The two established construction mechanisms remained the main focus: whole-graph
synchronization (021–024), and shared-center variable/clause construction
(026–032,037–039). Structural and spectral probes are diagnostic work, not extra
independent reduction routes. The variable encoding changed substantially: a
non-leaf mate supports complementary third-layer ports and robust second-layer
occurrences. Their independent composition now has finite checks and an author-side
argument. The exact NAE and exact-one clauses remain absent. The source-to-exact-one
bridge in round 039 is supporting logic, not an original graph reduction.

Useful feedback prevented further private synchronizer expansion (023), exposed
the limitation of leaf-center choices (026), and ruled out spectral sufficiency
(036) and specified edge-only augmentation (037–038). Larger sampling did not
turn the mate-choice observation into proof. The skill's optional actions were
used, but prior experience, this discussion and different search scopes prevent
a causal comparison with earlier allocations. No numerical success-rate gain
or improved discovery rate is claimed.

## Next action

Stop with all forty rounds used. Short-term prospects remain low (uncalibrated):
the missing clause or a different complete encoding is still the bottleneck.
An independently supported structural characterization or a concrete clause
mechanism addressing the recorded budget constraints would justify renewed work.
Do not extend the current templates merely to fill another allocation. No full
candidate, independent review, manuscript or production integration exists.
