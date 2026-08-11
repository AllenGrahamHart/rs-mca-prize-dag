# Claim contract

- **Claim:** the correction quadratic misses all three assigned centers and
  only one supported padded-heavy center overlap can remain.
- **Dependencies:** exact three-center source partition, double-root padded
  rank-loss interpretation, separated heavy-row factorization, center-overlap
  factorization, and exact correction orders.
- **Output:** `(HOD1)--(HOD4)`; `j<=1` and at most two heavy-row scalar
  coefficients.
- **Consumer:** the separated double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of `j=0,1` or of a nonzero passing remainder.
- **Falsifier:** a separated packet with a correction root among the three
  centers, or with two center roots of `g_*`, satisfying all dependencies.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_separated_correction_center_disjoint_overlap_cap_one/verify.py`
  and `verify_audit.py`.
