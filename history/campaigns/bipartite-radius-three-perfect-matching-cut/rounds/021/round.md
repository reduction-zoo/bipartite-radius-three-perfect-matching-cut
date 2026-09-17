# Round 021: smaller synchronization without private leaves

## Plan
Status: completed. Date: 2026-09-15. Action: Reconsider.
Round 020 excludes the private K2,3 synchronizer with leaves. Search a replacement
with opposite-side terminals, zero terminal crossing budgets and one crossing at
all other vertices. To work inside a larger graph it must force equality and
zero terminal crossings even when terminals are allowed at most one internally.
Scope: all connected subgraphs of K3,3 (512 edge masks), terminals 0 and 3,
all 64 colorings each. A valid replacement must allow both equal assignments
and no other admissible boundary state. Classify terminal distances and radius.
The shared fixed-center experience does not apply: this is a general equality
interface. A local success still needs global distance checking. End after this
finite family; no timeouts or changes to campaign endpoints.

## Evidence and diagnosis
205 connected graphs, 13120 colorings, 12 labeled successful interfaces.
Some are leafless C6 with adjacent terminals. The private-leaf hypothesis was
therefore not necessary for synchronization. See result.json and check.log.
These are finite exact boundary relations, without a novelty assessment.
## Next action
Test their complete double-cover composition before choosing a larger gadget.
