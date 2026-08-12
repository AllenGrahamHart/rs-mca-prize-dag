# Claim contract

- **Claim:** every ordinary companion from collision shapes B--D has the
  norm factorization `(OCN2)`, coprimality `(OCN3)`, exact heavy-row order
  `(OCN4)`, and bounded residual gates `(OCN5)--(OCN7)`.
- **Dependencies:** factorwise four-shape classification and all-excess
  transverse actual-support fiber factorization.
- **Output:** a degree-at-most-six gate for `(2,3)` companions and a
  degree-at-most-twelve gate for `(4,6)` companions.
- **Consumer:** the unshared nonreduced collision arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no companion exclusion and no root claim for `E_Q`.
- **Falsifier:** a valid companion whose norm lacks `L_0^m`, has residual
  degree above `7m/2`, meets `U_0` after division, or lacks the forced
  heavy-row divisor `(X-x_*)^(m/2)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_ordinary_companion_norm_gate/verify.py`.
