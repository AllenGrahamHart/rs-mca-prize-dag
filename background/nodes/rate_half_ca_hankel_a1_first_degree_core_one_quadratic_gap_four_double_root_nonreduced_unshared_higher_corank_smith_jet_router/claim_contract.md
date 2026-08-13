# Claim contract

- **Claim:** away from quotient-root collision, every unshared nonreduced
  nonzero-jet survivor has one of exactly three Smith/jet profiles `(HSR4)`;
  corank four closes.
- **Hypothesis:** regular corank `r>=2`.
- **Dependencies:** the exact nonreduced two-jet image and regular Hankel
  recurrence structure.
- **Output:** the locator factorization `(HSR2)--(HSR3)` and complete
  determinant-order-four routing `(HSR4)`.
- **Consumer:** the nonreduced double-root branch in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no derivation of higher corank, no exclusion of either
  collision factor, `[1,3]`, `[2,2]`, `[1,1,2]`, or shared nonreduced roots.
- **Falsifier:** a missing Smith partition of four, a noncollision corank-four
  nonzero jet, a `[1,3]` second jet, or a `[2,2]`/`[1,1,2]` survivor whose
  second jet vanishes.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_higher_corank_smith_jet_router/verify.py`
  and `verify_audit.py`.
