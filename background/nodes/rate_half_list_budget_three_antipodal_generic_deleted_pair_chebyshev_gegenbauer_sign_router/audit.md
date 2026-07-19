# Audit

The symbol `r` is the normalized source lift, `u=r^2`, and `t=r^4` is the
deleted squared ratio. The three torsion exponents are therefore

```text
t^(4L)=1,       r^(16L)=1,       epsilon=r^(8L) in {1,-1}.
```

Confusing any two of these exponents changes the sign in `(CGR3)`.

The trace variables are `y=(r+r^(-1))/2` and
`x=(u+u^(-1))/2=2y^2-1`. Gegenbauer and Legendre polynomials are evaluated at
`x`, while source Chebyshev torsion is evaluated at `y`.

The sign split does not divide by `2y-1`, `y-1`, or `y`. Equation `(7)` is a
polynomial factorization and remains valid at every exceptional trace. This
avoids silently losing boundary points.

The router retains six sign branches. It neither claims that `s` is uniquely
determined nor promotes the bounded `M<=5` no-hit diagnostic to a theorem.
