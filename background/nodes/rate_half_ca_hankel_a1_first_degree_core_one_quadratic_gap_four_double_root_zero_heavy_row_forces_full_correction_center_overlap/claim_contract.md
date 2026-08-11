# Claim contract

- **Claim:** on the squarefree supported-disjoint double-root locus, a zero
  heavy row forces both correction roots to be center roots.
- **Dependencies:** exact regular-quartic resultant, all-excess vertical
  factorization and transversality, heavy-row center-overlap factorization,
  and the barycentric remainder gate.
- **Output:** `(HZF3),(HZF4)`; zero rows are restricted to `S_B|J`, hence
  `j>=2`.
- **Consumer:** the separated double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of `j=2,3`, nonreduced correction, or roots
  shared by `S_B` and `g_*`.
- **Falsifier:** a separated packet with `G(t,x_*)=0` and a root of `S_B`
  outside `Lambda`, satisfying all exact dependencies.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_zero_heavy_row_forces_full_correction_center_overlap/verify.py`
  and `verify_audit.py`.
