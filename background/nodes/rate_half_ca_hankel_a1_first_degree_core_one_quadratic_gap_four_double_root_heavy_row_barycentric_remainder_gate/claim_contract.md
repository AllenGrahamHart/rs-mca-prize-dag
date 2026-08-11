# Claim contract

- **Claim:** after the connected scalar weld leaves its unique vector
  `lambda`, all augmented heavy-row coefficient-MDS equations are equivalent
  to the one divisibility test `H|R_lambda`, or to `B_H lambda=0`.
- **Dependencies:** the paired row coefficient-MDS gate, scalar-weld gate,
  connected-rank dichotomy, and separated double-root heavy-row
  center-overlap factorization.
- **Output:** `(HRB2)`--`(HRB7)`, including the exact `(m-j) x |X|`
  remainder matrix.
- **Consumer:** the separated double-root route inside
  `rate_half_band_crossing_location`.
- **Nonclaims:** no universal nonvanishing theorem, no exclusion of the
  branch, and no extension to nonreduced/shared corrections.
- **Falsifier:** an admissible coefficient-code vector whose barycentric
  extrapolation differs from evaluation at `x_*`, or an allowed heavy row
  for which `H|R_lambda` fails in either direction.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_heavy_row_barycentric_remainder_gate/verify.py`
  and the independent hard-coded audit `verify_audit.py`.
