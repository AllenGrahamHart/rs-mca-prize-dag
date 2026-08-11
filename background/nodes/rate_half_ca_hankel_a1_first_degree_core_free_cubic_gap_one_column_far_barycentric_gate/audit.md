# Audit

- The joint support of the two endpoint errors is exactly their union, so
  the column-far threshold is `rho+1`, not `rho`.
- The strict `+1` means the equality case in `(TSV7)` is unavailable in the
  retained branch.
- Barycentric uniqueness is asserted only at union exactly `rho+1`, where
  the source difference has `c_alpha+1` distinct points.
- Every derivative `P'(x)` is nonzero because the domain points are distinct.
- `kappa` is nonzero by the degree of `R_alpha`; this also keeps all factors
  in `(CBG6)` nonzero.
- No sign or positivity is imposed on the field-valued weights.
