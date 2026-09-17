# Round 024: shared internal vertices for two independent equalities

## Plan
Status: completed. Action: Reconsider.
Round 023 implicates private two-terminal interfaces. Test a connected bipartite
shared gadget with sides 0..3 and 4..7, terminal pairs (0,4),(1,5), and four
internal vertices. Require both independent equalities with zero terminal budgets,
allowing all four x,y assignments. Every admissible local coloring with internal
budgets one and terminal budgets <=1 must have exactly that relation. Scope:
one full K4,4 edge template; Z3 synthesis with all 256 colorings as forbidden-state
constraints and four existential positive extensions. Connectedness is imposed
by distance ranks. End on SAT with direct exhaustive relation check or UNSAT.
The shared-center experience has no matching premises. Global scalable sharing
and radius remain open even if this finite interface succeeds.

## Evidence and diagnosis
One synthesis query returned UNSAT for the complete declared eight-vertex
shared template. This is trusted encoding-level exclusion, not a general theorem
against shared synchronization. No candidate graph was generated.
## Next action
Do not enlarge this family without a better composition principle. Investigate
structural characterizations of radius-three perfect cuts to identify which
part of the graph can actually carry independent source choices.
