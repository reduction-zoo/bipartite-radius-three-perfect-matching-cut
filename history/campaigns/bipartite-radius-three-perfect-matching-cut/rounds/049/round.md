# Round 049: general interface and composition proof

## Plan
Status: completed. Action: Investigate.
Use the selector and occurrence findings. Prove the selector boundary relation
for arbitrary external attachments only at center, mate and high ports, then
prove binary wire behavior with the forced center edge. Compose with the signed
exact-one bridge, establish both directions and normalization for every witness,
and count vertices, edges and encoding costs. No new finite graph search or
solver calls: this is a general proof strategy. Preserve the old fixed-center
lemma in its originating round before replacing the current work/proof.md;
update its incoming evidence link. Time/token usage unavailable.

## Evidence and diagnosis
The author-side proof in work/proof.md establishes the robust selector relation,
forces the center edge, proves binary variable consistency under attachments,
and composes both maps. The output counts are 4+8n+160m vertices and
3+14n+304m edges for m>0, with explicit polynomial bit bounds. Degenerate and
malformed inputs are covered. The earlier lemma and its incoming links were
preserved. No new solver queries or algorithm changes.
Experience extraction: updated selector and occurrence entries with the general
arguments and exact attachment premises; independent review remains pending.

## Next action
Check primary literature and run independent verification before review.
