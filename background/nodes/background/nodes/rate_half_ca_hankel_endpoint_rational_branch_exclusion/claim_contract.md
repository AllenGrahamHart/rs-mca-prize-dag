# Claim contract

- **Claim:** an official strict-endpoint counterexample has one unique
  defect-one irreducible component `(r,e)=(4e-1,e)` carrying at least
  `ceil((3m+1)/4)` parameter degree; every other component has `(r,e)=(4e,e)`
  and their total parameter degree is at most `floor((m-1)/4)`.
- **Scope:** the extremal endpoint `m>1`, `rho=4m-1`, `N=16m`, `T=4m+1` with
  exact omission budget `O<=m-1`.
- **Dependency:** `rate_half_ca_hankel_endpoint_norm_factorization` supplies
  the exact distinct-incidence count.  Component overlap only strengthens the
  aggregate shortfall bound.
- **Consumer:** the strict `e=m`, `A=3` branch of
  `rate_half_band_closure`.
- **Nonclaims:** the dominant nonlinear component is not excluded; no genus,
  monodromy, or split-fiber theorem for it is asserted; no `e>m` or `A=1`
  profile is covered.
- **Next exact gate:** analyze the dominant `(4e-1,e)` component using the
  Hankel/apolar coefficient chain and dyadic split fibers.  Rational
  moving-pencil assemblies and broadly fragmented component profiles are no
  longer live endpoint routes.
