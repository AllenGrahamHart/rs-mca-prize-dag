# Claim contract

- **Claim:** every squarefree double-root packet, including shared roots,
  has one nonzero correction-coprime heavy row with quotient degree at most
  one, and passage is exactly one barycentric divisibility test.
- **Dependencies:** separated cubic quotient, shared third-jet vanishing,
  source partition, center-overlap algebra, and barycentric interpolation.
- **Output:** `(HUG2)--(HUG7)`.
- **Consumer:** the squarefree double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of the constant/linear remainder survivor and
  no nonreduced or two-simple claim.
- **Falsifier:** a squarefree packet with `j>=2`, a correction root of `T_j`,
  a zero heavy row, or failure of the exact remainder equivalence.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_squarefree_unified_heavy_row_remainder_gate/verify.py`
  and `verify_audit.py`.
