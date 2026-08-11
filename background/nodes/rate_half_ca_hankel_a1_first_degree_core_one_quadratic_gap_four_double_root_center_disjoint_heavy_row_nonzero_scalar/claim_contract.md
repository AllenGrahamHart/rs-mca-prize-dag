# Claim contract

- **Claim:** on the squarefree, supported-disjoint, center-disjoint
  double-root locus, the heavy row is a nonzero scalar multiple of
  `g_*S_B^2`.
- **Dependencies:** exact regular-quartic resultant, all-excess vertical
  factorization and transversality, heavy-row center-overlap factorization,
  and the barycentric remainder gate.
- **Output:** `(HNS3),(HNS4)`; the zero extrapolated row is excluded.
- **Consumer:** the separated double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no assertion when a correction root is a center, when
  `S_B` is nonreduced, or when `S_B` shares a root with `g_*`.
- **Falsifier:** a center-disjoint packet with `G(t,x_*)=0`, together with an
  exact local resultant and fiber factorization satisfying all dependencies.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_center_disjoint_heavy_row_nonzero_scalar/verify.py`
  and `verify_audit.py`.
