# Round 030: clause synthesis for saturated L2 occurrence terminals

## Plan
Status: completed. Action: Continue.
Three terminals are L2 occurrence vertices with zero remaining budget, as
supported by round 029. Add b private L1 anchors (color zero, budget one),
k=b+f L2 auxiliaries, and f L3 auxiliaries. Shared h has color one and zero
remaining budget. Optional edges: L2 auxiliaries to h/anchors/L3, terminals to
L3. Each internal L2 vertex must touch h or an anchor; each L3 vertex touches
L2 or a terminal. Shared u reaches these vertices within three steps using
existing variable paths. Require exact NAE on terminals, all six assignments
at the fixed shared phase. Scope: (b,f)=(1,3),(2,3), at most eight candidates
each, whole-boundary counterexample exclusion. A SAT interface must compose
with the existing wire; an UNSAT result excludes only these finite templates.

## Evidence and diagnosis
Both declared templates returned UNSAT after one candidate and one bad boundary
pattern each: six solver queries total. Saved graphs and bad patterns remain in
the two result files. Unlike early rounds, terminal budgets here match the actual
composable wire. No exact NAE clause was found in this scope.
## Next action
Reconsider the primitive relation. Test exact-one on the same terminals; a
successful primitive could be composed with a separate constant-size source
encoding, whose correctness and recovery would still need proof.
