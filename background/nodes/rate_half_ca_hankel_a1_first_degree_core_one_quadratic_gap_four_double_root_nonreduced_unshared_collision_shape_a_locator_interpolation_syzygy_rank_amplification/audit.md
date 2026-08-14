# Audit

1. The parity range is exact: `R-d-2=n`; using `n+1` would overrun the
   dual-RS identity.
2. The second factor `L'(x)` in `(9)` comes from `H_x=G(t,x)/L'(x)`; the
   first comes from locator interpolation.
3. The selected class has `n+2` distinct points. Evaluation of all
   degree-at-most-`n` polynomials has rank `n+1`, while the independent
   `B_j` subspace has rank `r`.
4. The diagonal source weights are nonzero, but no positivity or
   noncancellation is assumed; Sylvester permits the one-dimensional rank
   loss.
5. Only one projection is used. No unsupported independence among the three
   class maps is claimed.
6. The older `(e+1)/3` floor remains true but is superseded.
7. No critical status changes.
