# Claim contract

- **Claim:** at most one correction root and at most one padded-heavy root
  can lie among the three centers, so the center-overlap degree is at most
  two.
- **Dependencies:** extremal three-center reduction, double-root rank-loss
  interpretation, regular-quartic heavy-row factorization, separated
  heavy-quotient profile, and center-overlap factorization.
- **Output:** `(HOC3)--(HOC5)`; the `j=3` and four-scalar heavy-row cases are
  excluded.
- **Consumer:** the separated double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of `j<=2` or of a nonzero passing remainder.
- **Falsifier:** a separated extremal packet with either an endpoint center
  on `S_B` or two center roots of `g_*`, satisfying all dependencies.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_separated_center_overlap_cap_two/verify.py`
  and `verify_audit.py`.
