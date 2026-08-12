# Claim contract

- **Claim:** the common divisor `g_*S_B` can be removed from every
  canonical divided-row moment, leaving one vector of forms of degree at
  most five with an exact recurrence and nonzero correction value.
- **Dependencies:** nonreduced center-adjusted heavy-row residual and Pade
  regular-factor identity.
- **Output:** `(DQQ3)--(DQQ7)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no divisibility by the full determinant factor
  `D_1=g_*S_B^2`; no exclusion of the quintic vector.
- **Falsifier:** one `F_i` not divisible by `g_*S_B`, quotient degree above
  five, a failed recurrence, a missing `J_*` cancellation, or
  `C_0(tau)=0`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_divided_row_quintic_quotient/verify.py`.
