# Claim contract

- **Claim:** the direct Pade restriction is the canonical residual section,
  while raw parameter and row derivatives fail the mandatory base divisor.
- **Dependencies:** residual four-cycle rigidity, the exact Pade syzygy and
  contact normalization, and one pure split fiber with simple roots in both
  coordinates.
- **Currency:** sections of `O_C(G)(-D_mand)=O_C(2B)` on the normalized
  locator curve.
- **Output:** a route fence for the four natural second-section candidates.
- **Consumer:** the shape-A branch of `rate_half_band_crossing_location`.
- **Nonclaims:** exclusion of every source combination or shape-A closure.
- **Falsifier:** an independent normalized `P_F` section, or vanishing of
  either raw derivative along the complete mandatory divisor.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_natural_residual_section_route_fence/verify.py
  --tamper-selftest`.
