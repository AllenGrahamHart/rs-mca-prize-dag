# Claim contract

- **Claim:** every irreducible factor of the extremal paired biform
  saturates every classified row and every clean parameter fiber, and obeys
  `3e n_j>=(3p-3+d_A)m_j`; at least one factor has the macroscopic degree
  in `(PMF4)`.
- **Dependencies:** the extremal dual-MDS split-biform construction and its
  exact classified-row root sets.
- **Output:** `(PMF3)--(PMF5)`, including two-directional factor splitting.
- **Consumer:** the extremal paired-biform route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no irreducibility theorem, no uniqueness of the large
  factor, and no exclusion of a macroscopic split factor.
- **Falsifier:** a factor with a zero row/fiber specialization, a factor
  violating `Tn_j>=Rm_j`, overlapping factor roots on a classified row, or
  a complete factorization below the bound `(PMF4)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_paired_split_biform_macroscopic_parameter_factor/verify.py`
  and `verify_audit.py`.
