# Claim contract

- **Claim:** the `4+d_A` complement of the off-line padded-heavy row forces
  factorwise supported-column slack and sharpens the exact factor
  trichotomy; the `d_A=1` branch still has only profile I.
- **Dependencies:** center-adjusted nonreduced heavy-row residual and exact
  factor-degree trichotomy.
- **Output:** `(URB4)--(URB9)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of the remaining large-odd factor.
- **Falsifier:** a factor exceeding supported-fiber root capacity, an
  off-line heavy-row deficit above `4+d_A`, or a feasible `d_A=1` profile
  II/III satisfying all degree inequalities.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_factor_profile_unsupported_root_budget/verify.py`.
