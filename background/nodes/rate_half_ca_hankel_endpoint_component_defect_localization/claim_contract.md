# Claim contract

- **Claim:** the strict endpoint has exact componentwise row and column
  deficit sums `O-E` and `1+O-E`; if `b` is the total residual parameter
  degree, then `4b<=O-E`.  Every component splits disjointly on at least
  `3m+2` supported slopes and at least `15m` domain fibers.
- **Scope:** only `m>1`, `rho=4m-1`, `N=16m`, `T=4m+1`, with the exact
  endpoint incidence and component profile already proved.
- **Dependencies:**
  `rate_half_ca_hankel_endpoint_rational_branch_exclusion` supplies the
  component bidegrees; `rate_half_ca_hankel_endpoint_norm_factorization`
  supplies the transverse-fiber count; endpoint saturation and exceptional
  root charging supply the other two split-fiber counts.
- **Consumer:** the strict `e=m`, `A=3` branch of
  `rate_half_band_closure`.
- **Nonclaims:** no dominant nonlinear component is excluded; no monodromy,
  genus, or subgroup point theorem is asserted; the residual degree need not
  vanish when `O>=4`.
- **Next exact gate:** use the Hankel/apolar coefficient chain to classify
  the dominant `(4e_*-1,e_*)` curve under these two-direction split-fiber and
  low-defect divisor constraints.
