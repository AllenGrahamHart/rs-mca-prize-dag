## Round-29 row-size scope flag (2026-08-10, coordinator-applied: k_extremal)

ROW-SIZE SCOPE (k_extremal 2026-08-10, E7 pattern — FLAGGED, not
resolved): the claim line quantifies over every admissible rate-1/2
row; the supplied lower bracket (RHL-LB, a_L >= k+2^34) is proved
only at n = 2^41, k = 2^40 and is VACUOUS below k = 2^35 (at rate
1/2, [k+2^34, 3n/4] = [k+2^34, 1.5k] is empty unless k >= 2^35 —
exact integer check, coordinator-replayed). Under the descriptor
family (background/nodes/descriptor/proof.md:3-8: k <= 2^40 is an
upper CAP, so the rate-1/2 family is n = 2^s, k = 2^(s-1),
s = 1..41), rows with s <= 35 have no bracket at all and rows with
36 <= s <= 40 have an unproved one. Claim quantifier strictly
exceeds machinery quantifier — the round-28 tiling failure's
pattern, one axis over. Candidate reduction poses (incl. the
elementary POSE 1 list-side triviality corridor, exact reach
s <= 7 above per-s q-thresholds) at
notes/pilots_20260810/k_extremal/DRAFT_SCOPE_FLAGS.md.
