# Audit

- The antipodal quotient is exactly `mu_(N/2)` because squaring has kernel
  `{1,-1}` on `mu_N`.
- The factor `c^(e-1)` in `(DSN5)` comes from multiplying the two prefactors
  `X^(e-1)` in `(4)`; omitting it changes the resultant scalar.
- Constant-product fixed points cannot be silently paired with themselves.
  They appear once in `(DSN8)` and as simple factors in `(DSN7)`.
- The reverse implication in `(DSN9)` requires exact degree and a nonzero
  constant term, so the reciprocal product has degree `2r`. These hold on
  every external locator but are stated explicitly.
- The Dickson identity is a compact representation. An implementation should
  use its recurrence and exact square-root division, not materialize an
  orbit list at official size.
- The verifier checks all 97 parameter values over `F_97` at `e=2,N=24` for
  antipodal, fixed-point-free constant-product, and two-fixed-point
  constant-product controls, including multiplicity-aware split-slope
  equivalence and the guaranteed internal split slopes.
