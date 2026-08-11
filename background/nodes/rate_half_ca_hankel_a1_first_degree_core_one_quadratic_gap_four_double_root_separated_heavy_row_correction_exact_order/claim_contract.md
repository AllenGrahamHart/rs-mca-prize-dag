# Claim contract

- **Claim:** at every separated correction root, the heavy row has exactly
  the order already forced by `H`; the free overlap form is a unit there.
- **Dependencies:** double-root divisor/contact normal form, heavy-quotient
  Pade syzygy, center-overlap factorization, and the barycentric remainder
  identity.
- **Output:** `(HCE3),(HCE4)`; `gcd(T_j,S_B)=1`.
- **Consumer:** the separated double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no restriction on roots of `T_j` away from `S_B`, and no
  exclusion of a nonzero passing remainder.
- **Falsifier:** a separated packet where `T_j` vanishes at a correction
  root while the inherited divisor and Pade identities hold.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_separated_heavy_row_correction_exact_order/verify.py`
  and `verify_audit.py`.
