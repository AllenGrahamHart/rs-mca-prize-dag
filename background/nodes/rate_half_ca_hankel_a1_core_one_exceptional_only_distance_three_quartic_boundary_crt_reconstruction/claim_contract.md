# Claim contract

- **Claim:** the welded quartic `Omega` is reconstructed by one explicit CRT
  calculation on the `2e` exceptional roots. The generic degree-`<2e`
  remainder must collapse to `X`-degree at most four, and this collapse is
  equivalent to the global quartic weld within the exact active-row design.
- **Scope:** the official `e>=3` pair-Lagrange distance-three external
  design on the smooth multiplicative domain.
- **Dependencies:** cleared-lift quartic router and sparse subgroup-norm
  router.
- **Consumer:** `rate_half_band_closure` and `CR-003-CLIFT`; exact
  pre-cofactor rejection and certificate interface for the live saturated
  generic branch.
- **Falsifier:** a valid exact external design whose canonical remainder in
  `(QBC4)` has a nonzero coefficient of `X^j`, `5<=j<2e`, or disagrees with
  `(QBC9)` at a triple root.
- **Nonclaims:** no projective-line decomposition, coefficient-rank bound,
  fixed cofactor, or splitting of the quartics. Random pair-Lagrange data
  failing the degree collapse are rejection controls, not prize
  counterexamples.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_boundary_crt_reconstruction/verify.py`
