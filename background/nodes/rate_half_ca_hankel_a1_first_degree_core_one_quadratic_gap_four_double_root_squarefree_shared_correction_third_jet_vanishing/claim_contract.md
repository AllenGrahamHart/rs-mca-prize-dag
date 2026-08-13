# Claim contract

- **Claim:** symmetry, regular corank one, and simplicity of the padded root
  force the squarefree shared third-jet obstruction to vanish.
- **Dependencies:** the exact shared third-jet gate, minimum-gap squarefree
  excess roots, and the supported minimal-locator kernel description.
- **Output:** `(HSV1)--(HSV3)`; the cubic quotient extends through every
  squarefree shared root.
- **Consumer:** the squarefree double-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no nonreduced-root or global remainder exclusion.
- **Falsifier:** a symmetric corank-one local block of determinant order
  three satisfying `(5)` with `kappa_tau U_tau(x_*)!=0`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_squarefree_shared_correction_third_jet_vanishing/verify.py`
  and `verify_audit.py`.
