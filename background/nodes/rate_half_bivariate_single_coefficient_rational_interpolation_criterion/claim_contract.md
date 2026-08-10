# Claim contract

- **Claim:** full rank of one coefficient block is equivalent to absence of
  the low-degree rational interpolation certificates `(RIC3)` or `(RIC4)`.
- **Dependency:** `rate_half_bivariate_schur_interpolation_defect_formula`.
- **Inputs:** distinct support points, scalar coefficient data `h`, and the
  optional unique lower deficiency clone.
- **Output:** the pivot-free rank criteria and official trace datum `(RIC5)`.
- **Consumer:** the residual rank route for
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of the rational certificate, no higher-deficit
  criterion, and no adjacent-crossing closure.
- **Falsifier:** a rank-deficient two-block matrix without `(RIC3)`, a
  full-rank matrix with such polynomials, or failure of the punctured
  equivalence `(RIC4)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivariate_single_coefficient_rational_interpolation_criterion/verify.py`
  and `verify_audit.py`.
