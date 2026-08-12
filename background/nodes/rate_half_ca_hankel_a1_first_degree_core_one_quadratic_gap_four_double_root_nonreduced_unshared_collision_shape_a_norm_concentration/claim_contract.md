# Claim contract

- **Claim:** in shape A, every padding factor is concentrated at `x_*` and
  the remaining norm quotient is the degree-at-most-`e` product of the
  excess residuals.
- **Dependencies:** complete companion exclusion, all-excess fibers,
  off-line norm factorization, the three-center sums, and the heavy-row
  padding divisor.
- **Output:** one explicit polynomial `T` replacing all shape-A padding and
  excess variables in the norm.
- **Consumer:** shape A inside `rate_half_band_crossing_location`.
- **Nonclaims:** no formula for `T` and no shape-A exclusion.
- **Falsifier:** an off-line padding root away from `x_*`, total residual
  degree above `e`, or disagreement with a classified-row tangent value.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_norm_concentration/verify.py`.
