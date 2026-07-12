# Proof

Fix a nonzero parameter `t`.  The involution

```text
(a,b) -> (b,a)
```

acts on the `P(t)` ordered product representations.  Its fixed points are
exactly the `D(t)` representations `(a,a)` with `a^2=t`.  Therefore the number
of ordered pairs of product representations which are neither equal nor
swaps is

```text
P(t)(P(t)-1) - (P(t)-D(t))
  = P(t)(P(t)-2)+D(t).                         (1)
```

Since the field has odd characteristic, `D(t)` is at most two.  More
importantly, the swap involution shows that `P(t)` and `D(t)` have the same
parity.  For every nonnegative integer `m` and every feasible fixed-point
count `d` (`0 <= d <= 2`, `d <= m`, and `d = m mod 2`),

```text
136(m-35)_+ <= m(m-2)+d.                       (2)
```

For `m <= 35` this is immediate.  For `m >= 36`, subtracting the left side
from the right side gives

```text
(m-68)(m-70)+d.
```

This is nonnegative except possibly at `m=69`; there parity forces `d >= 1`,
giving equality.  Equality also occurs at `(m,d)=(68,0)` and `(70,0)`.
Multiplying (2) by `R(t)` and summing over `t != 1` proves
`136X_35 <= S_ns`.  Thus `S_ns <= 68n^2` implies `X_35 <= n^2/2`.

There is also an exact lower-dimensional description of the remaining
incidences.  Given two product representations and one quotient
representation of the same `t`, write

```text
(a,b), (a',b'), (c,d),
ab=a'b'=d/c=t.
```

All entries lie in `A`, hence are nonzero.  Set `lambda=a'/a`.  Then

```text
a'=lambda*a,  b'=b/lambda,  d=a*b*c.
```

The representations are equal exactly when `lambda=1`, and they are swaps
exactly when `lambda=b/a`.  Conversely these formulas recover a unique
incidence from every quadruple `(lambda,a,b,c)` satisfying

```text
lambda != 1,
lambda != b/a,
ab != 1,
a, lambda*a, b, b/lambda, c, a*b*c in A.       (3)
```

Hence `S_ns` is precisely the four-variable six-membership incidence count
(3).  This removes the universal swap contribution from the older factorial
moment without changing the critical claim.

