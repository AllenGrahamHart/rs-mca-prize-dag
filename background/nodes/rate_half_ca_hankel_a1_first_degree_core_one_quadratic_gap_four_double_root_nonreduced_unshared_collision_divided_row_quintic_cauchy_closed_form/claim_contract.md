# Claim contract

- **Claim:** the divided-row quintic vector has the exact Cauchy closed form
  `(DCF4)`; all previously recorded quintic properties are automatic.
- **Dependencies:** the Pade/split-biform interpolation identity and the
  nonreduced heavy-row quadratic factorization.
- **Output:** `(DCF2)--(DCF5)`.
- **Consumer:** strategy selection in the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion or construction of a collision.
- **Falsifier:** source data satisfying `(1)` and `(DCF1)` for which `(DCF4)`
  fails for some `0<=i<=d`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_divided_row_quintic_cauchy_closed_form/verify.py`.
