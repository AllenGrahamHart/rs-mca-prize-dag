# Claim contract

- **Claim:** every unshared nonreduced nonzero-jet collision has regular
  corank two and Smith profile `[1,3]` or `[2,2]`, selected by `[z]a` in
  the local Pade remainder `b+ay`.
- **Quantifier:** odd residue characteristic.
- **Dependencies:** normalization/collision dichotomy, higher-corank
  locator router, and Pade-Bezout contact-module presentation.
- **Output:** `(CBS3)--(CBS5)`.
- **Consumer:** the nonreduced double-root arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of either residual profile, no shared-root
  assertion, and no characteristic-two assertion.
- **Falsifier:** a geometric collision of corank other than two, profile
  outside `{[1,3],[2,2]}`, or a mismatch between `[z]a` and `(CBS4)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_exact_collision_bezout_smith_router/verify.py`.
