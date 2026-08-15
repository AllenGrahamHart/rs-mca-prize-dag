# Proof

Fix a globally heavy owner of weight `s`, and put `d=P-s`.  Every clean
line through it uses at least `d` selected light mass.  Distinct such lines
use disjoint light owner points, so there are at most `ell/d` of them.
For one line, convexity of the selected partition gives charge at most

```text
C(s,2)+C(d,2)+rP.
```

The owner's total contribution is therefore at most

```text
ell [C(s,2)+C(P-s,2)+rP]/(P-s)
  =ell phi(s).                                      (1)
```

The heavy weights satisfy `a<=s_i<=b` and sum to at most `S-ell`.
Moreover

```text
phi(s)=C0/(P-s)-s,
phi'(s)=C0/(P-s)^2-1>0,
phi''(s)=2C0/(P-s)^3>0.                            (2)
```

The first inequality follows from `P-s<=floor(P/2)` and
`C0>=C(P,2)`.  Thus, for a fixed owner count and heavy-mass budget, an
exchange toward the endpoints cannot lower the objective.  Iterating the
exchange leaves as many weights `b` as possible, at most one residual
weight, and all remaining weights `a`.  This proves the finite maximum in
the statement and hence the clean cap.

For exact evaluation, fix the owner count `t` and the number `u` of weights
equal to `b`.  On one residual-weight interval, write the light mass as
`x`.  The residual denominator has the form `x+D`, and the objective is

```text
F(x)=x (x+A+C0/(x+D)).                              (3)
```

Its second derivative is

```text
F''(x)=2-2C0 D/(x+D)^3.                             (4)
```

If `D<=0`, the segment is convex.  If `D>0`, (4) changes sign at most once;
the concave part has a monotone derivative and the convex part is maximized
at an endpoint.  Exact rational bisection therefore reduces each segment
to its endpoints and, when present, the single derivative crossing.  The
primary verifier checks 271 segments and at most 558 exact candidates for
each of the thirteen core offsets.  Every maximum has `t=u=8`; adding the
unchanged balanced and collision terms gives the printed chart maximum.
