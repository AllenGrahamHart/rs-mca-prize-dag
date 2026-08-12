# Claim contract

- **Claim:** after removing the `d_A` padded-heavy center factors from
  `g_*`, every unshared nonreduced collision heavy row is `g_off`, the
  double correction `S_B`, and a residual of exact degree `2+d_A` nonzero
  at the correction.
- **Dependencies:** collision barycentric split-jet gate, all-excess fiber
  factorization, regular-quartic supported-factor pin, and exact
  three-center source partition.
- **Output:** `(HQR1)--(HQR7)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no universal nonvanishing of the remainder matrix.
- **Falsifier:** a noncenter padded-heavy root missing from `G(t,x_*)`, a
  correction order other than two, or residual degree other than `2+d_A`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_heavy_row_quadratic_residual_factorization/verify.py`.
