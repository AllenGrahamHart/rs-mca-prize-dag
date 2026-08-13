# Claim contract

- **Claim:** no bidegree-`(2,3)` ordinary companion exists on the official
  first residual row; shapes B and D are empty.
- **Dependencies:** the proved coincidence router and the already audited
  Corvaja--Zannier positive-characteristic gcd theorem.
- **Output:** the collision shape list is reduced from A--D to A/C.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of shape A or C, no `(4,6)` companion
  exclusion, and no extension-field result.
- **Falsifier:** an official `(2,3)` companion whose coincidence component
  violates the gcd bounds, or a translated-subtorus component compatible
  with the stated `S_3/C_3` action.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_ordinary_quadratic_companion_torus_gcd_exclusion/verify.py`.
