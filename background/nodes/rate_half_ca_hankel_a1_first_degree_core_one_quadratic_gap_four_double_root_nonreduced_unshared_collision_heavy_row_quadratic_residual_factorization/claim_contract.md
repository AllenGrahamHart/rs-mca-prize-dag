# Claim contract

- **Claim:** every unshared nonreduced collision heavy row is the supported
  padded factor `g_*`, the double correction form `S_B`, and a residual of
  degree at most two nonzero at the correction.
- **Dependencies:** collision barycentric split-jet gate, all-excess fiber
  factorization, and regular-quartic supported-factor pin.
- **Output:** `(HQR2)--(HQR7)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no universal nonvanishing of the remainder matrix.
- **Falsifier:** a padded-heavy supported root missing from `G(t,x_*)`, a
  correction order other than two, or residual degree above two.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_heavy_row_quadratic_residual_factorization/verify.py`.
