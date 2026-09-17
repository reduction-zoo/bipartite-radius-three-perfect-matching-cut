# Round 014: replace the private center leaf by a second access vertex

Status: completed; declared before execution.
Action: Reconsider the leaf assumption implicated by rounds 012–013. Add an
edge u-h to the binary cube; connect u to a nonempty subset of odd-parity cube
vertices and h to any subset of even-parity vertices. All old cube edges stay.
Scope: 15*16=240 graphs of order ten, all 1024 colorings each. Center and mate
colors are free; do not assume uh crosses or cube budgets stay internal. Test
full NAE projection on ports 1,2,4 with u eccentricity <=3. Keep all successful
interfaces for a composition check. This changes the access mechanism, not size.
End after the declared finite enumeration. Shared-center composition remains
unproved even if a local interface succeeds. No fixed-center lemma is applied.

Result: four of 240 graphs realize full local NAE with center eccentricity three.
All four attach u to one cube vertex and h to its antipode. The two added
vertices form a length-three path between these antipodes. All 245760 colorings
were checked, without an internal-budget premise. See result.json for witnesses.
The mate can provide a second access path, so the private-leaf restriction was
material. This is local feasibility, not novel hardness. Next test actual
composition immediately instead of expanding successful gadget sizes.
