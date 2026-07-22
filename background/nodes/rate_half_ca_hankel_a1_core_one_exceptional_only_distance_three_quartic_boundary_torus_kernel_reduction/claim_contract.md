# Claim contract

- **Claim:** the complete quartic boundary moment system is a homogeneous
  linear system `T theta=0`, where `T` depends only on pair-Lagrange data and
  every coordinate of the external label vector `theta` is nonzero.
- **Scope:** the official `e>=3` generic saturated distance-three chart.
- **Dependency:** quartic boundary dual-moment gate.
- **Consumer:** `rate_half_band_closure` and `CR-003-CLIFT`; early exact
  full-rank or torus-kernel exclusion before external cofactor construction.
- **Falsifier:** a valid design violating `(QTK3)--(QTK7)`, or a claimed
  exclusion whose printed matrix has a full-support kernel vector.
- **Nonclaims:** the matrix is not asserted to have full rank on every
  admissible packet. The deterministic full-rank controls are not external
  designs or official nonexistence certificates.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_torus_kernel_reduction/verify.py`
