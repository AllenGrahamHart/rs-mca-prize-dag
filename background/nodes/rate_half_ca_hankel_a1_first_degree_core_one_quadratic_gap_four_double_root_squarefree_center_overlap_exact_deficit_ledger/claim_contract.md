# Claim contract

- **Claim:** the squarefree heavy-row center-overlap degree is exactly the
  already classified deficit bit `d_A`, so the two surviving remainder
  profiles are constant for `d_A=0` and at most affine for `d_A=1`.
- **Dependencies:** the extremal three-center source partition and the
  unified squarefree heavy-row remainder theorem.
- **Output:** `(HED2),(HED3)`.
- **Consumer:** the squarefree double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of either passing remainder and no assertion
  that the `d_A=1` quotient has exact degree one.
- **Falsifier:** a correction center not counted by `r_gamma`, a center
  factor of `g_*` not counted by `r_gamma`, or `j!=d_A`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_squarefree_center_overlap_exact_deficit_ledger/verify.py`
  and `verify_audit.py`.
