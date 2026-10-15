import Challenge
open BipartiteRadiusThreePerfectMatchingCut
example : legalTarget ⟨7, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]⟩ = true := by native_decide
example : perfectCut ⟨1, []⟩ [true] = false := by native_decide
