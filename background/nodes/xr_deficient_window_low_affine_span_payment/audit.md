# Audit

## Formula audit

The punctured code has length `n-e`, dimension `k-ell`, and agreement
`k+d`, so its redundancy and excess are exactly
`R+ell-e` and `d+ell`. The affine compiler is applied to the affine hull,
not assumed to contain only selected parameters.

## Maximization audit

- Smaller `e` enlarges every factor.
- The smallest allowed `e` is `2(h-d)` only in the live local branch.
- The discrete `d` comparison uses `ell+j<=R-2h`; this is checked uniformly,
  not sampled at endpoints.
- Feasibility at `ell=1` produces exactly
  `d_0=ceil((2h+2)/3)`.
- The target budget increases with `e`; the proof compares against its
  uniform minimum at `e=4`, not against the larger same-corner budget.

## Residual risk

The first unpaid dimensions are small enough that generalized-weight or
active-block refinements may still pay them, but `(LA1)` alone does not.
