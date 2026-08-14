# Audit

Coordinator PR-review session, 2026-08-13 evening.

1. **The certificate-class wall is independently reproduced**:
   `verify_audit.py` recomputes `L(19737)` from scratch (own
   `math.comb` implementation of `Q_s` and `c_delta`) and hits the
   printed `U_low = 808527428378681053` exactly. Abel/greedy validity
   spot-checked (`Q_s` nondecreasing, `c_delta` strictly decreasing).
2. **Ledger identities exact**: `U_total = U_high + U_low + 2w` (the
   `134944` difference is the near charge); `U_total - B_*` matches;
   factor `> 2.9`; the predecessor rank-10 identity
   `total + slack = B_*` holds.
3. **Carried, not recomputed**: the optimality of `J = 19737` over all
   legal cutoffs, the high-margin tail value, the `C_s` nonuniform
   resource optimizer (`811958533186703629`), and the two fixed-pair
   terminal weights — all replayed upstream (Python normal/-O, Sage
   GF(7)/GF(11) controls, Wolfram integer replay, 6/6 mutations,
   independent math + custody reviews GREEN).
4. **Per-pair caps dominate the printed record loads**
   (`c_8 = 122639 >= 114624`, `c_4 = 245277 >= 200632`), as required
   for the terminals to be consistent.
5. **Disjointness mechanism** (outside coordinate determines the slope
   by its affine ratio) is the same argument family as the two-anchor
   coordinate-ratio injection banked in
   `v13_2_near_rational_supportwise_two_anchor_payment` — line-checked.
6. **Scope honesty**: the verdict is per the declared pair/core
   certificate class; the pre-registered escape (cross-pair same-line
   coupling or a chronology-correct dense-core owner) is recorded in
   the statement, with the exact `delta <= 4` / `200632`-slope terminal
   it must handle.
