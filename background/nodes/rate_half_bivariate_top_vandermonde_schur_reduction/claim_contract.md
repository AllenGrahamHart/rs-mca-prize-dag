# Claim contract

- **Claim:** the top parameter-coefficient slice pays exactly `4m+1` matrix
  columns, reducing full rank to the Schur matrix `(TVS4)`.
- **Dependency:** `rate_half_bivariate_deficiency_clone_kernel_reduction`.
- **Inputs:** the domain points, coordinate linear factors, incidence root
  products, and deficiency clone columns.
- **Output:** `(TVS2)--(TVS6)`.
- **Consumer:** the bad-pattern rank attack on
  `rate_half_band_crossing_location`.
- **Nonclaims:** no lower bound for `rank(S_W)`, no canonical pivot set, and
  no endpoint closure.
- **Falsifier:** failure of the top-column coefficient rule, a zero printed
  Vandermonde determinant under `(TVS1)`, or a rank mismatch in `(TVS4)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_bivariate_top_vandermonde_schur_reduction/verify.py`
  and `verify_audit.py`.
