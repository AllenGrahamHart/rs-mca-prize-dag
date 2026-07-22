# Claim contract

- **Claim:** on either surviving dihedral branch, the full sparse subgroup
  norm descends to the orbit resultant `(DSN4)` or `(DSN8)`, whose value
  polynomial has orbit degree at most `r=2e+1`; exact-degree split slopes are
  equivalently characterized by `(DSN9)`.
- **Scope:** the official distance-three pair-Lagrange chart.
- **Dependencies:** dihedral boundary-order router and sparse subgroup-norm
  router.
- **Consumer:** `rate_half_band_closure` and a CR-003 split perfect-power
  classifier.
- **Falsifier:** a parameter value for which the direct `mu_N` product differs
  from the descended norm, a failure of the Dickson locator identity, or a
  disagreement between the two sides of `(DSN9)`.
- **Nonclaim:** the descended resultant is not shown to violate the required
  perfect-power factorization.
