# Claim contract

- **Claim:** the four-root complement of the supported padded-heavy row
  forces factorwise supported-column slack and sharpens the exact factor
  trichotomy; the `d_A=1` branch has only profile I.
- **Dependencies:** nonreduced exact quadratic heavy-row residual and exact
  factor-degree trichotomy.
- **Output:** `(URB4)--(URB9)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of the remaining large-odd factor.
- **Falsifier:** a factor exceeding its supported-fiber root capacity, a
  heavy-row supported-root deficit above four, or a feasible `d_A=1`
  profile II/III satisfying all degree inequalities.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_factor_profile_unsupported_root_budget/verify.py`.
