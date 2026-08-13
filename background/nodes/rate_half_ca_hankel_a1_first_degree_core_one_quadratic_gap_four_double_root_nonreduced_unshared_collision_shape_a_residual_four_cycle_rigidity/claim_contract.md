# Claim contract

- **Claim:** on shape A, the exact residual locator/biform four-cycle is
  `2B`, and `O_C(2B)` has exactly one section.
- **Dependencies:** the double-root divisor normal form, the nonreduced
  normalization valuation, the exact projective four-core and regular
  quartic identification, and factorwise Bezout saturation.
- **Currency:** Cartier intersection length on the normalized locator curve
  and global sections of its residual line bundle.
- **Output:** a rigid residual quartic, excluding the automatic
  quartic-pencil interpretation of the four-core.
- **Consumer:** the shape-A branch of `rate_half_band_crossing_location`.
- **Nonclaims:** shape-A exclusion, smoothness, a gonality theorem, or a
  second residual section.
- **Falsifier:** residual intersection away from `B`, a local order other
  than `2m_b`, a constant modification direction, or a nonconstant section
  of `O_C(2B)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_residual_four_cycle_rigidity/verify.py
  --tamper-selftest`.
