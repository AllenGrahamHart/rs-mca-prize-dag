# Proof

The normal-form identity is

```text
m(P+Q-PQG)=d^2XP'R,       PQR=X^m-1.                (1)
```

Put `c=h+e`. Since `h>e`, the first `e+1` coefficients below the leading
term of `PQ` are the same as those of `P^2`; the constant shift `dP` begins
too low to contribute. Polynomial division at infinity in `PQR=X^m-1`
therefore gives

```text
R=X^c-2aX^(c-1)+(3a^2-2b)X^(c-2)+... .             (2)
```

The first three coefficients of `XP'R` are consequently

```text
h,
-(h+1)a,
(h+2)(a^2-b).                                      (3)
```

Write `G=g_eX^e+g_(e-1)X^(e-1)+...`. The terms `P+Q` in `(1)` also begin
below the first `e+1` comparison degrees. Comparing the leading coefficient
in `(1)` gives

```text
g_e=-d^2h/m.                                       (4)
```

The next coefficient gives

```text
g_(e-1)=d^2(3h+1)a/m.                              (5)
```

For `e>=2`, the third gives

```text
g_(e-2)=d^2(3h+2)(b-2a^2)/m.                       (6)
```

When `e=1`, `m=3h+1`, so `(4)--(5)` are exactly `(BTP1)`. When `e=2`,
`m=3h+2`, so `(4)--(6)` are `(BTP2)`.

The separator has a factor `X`, hence `H(0)=0`. Equivalently, evaluate

```text
P+Q-PQG=(d^2/m)XP'R
```

at zero to get `p_0+q_0=p_0q_0G(0)`. Substitution from `(BTP1)` or `(BTP2)`
proves `(BTP3)--(BTP4)`.

The constant term of a monic locator whose roots lie in `mu_m` is a signed
product of those roots. Since `m` is even, the sign also lies in `mu_m`, so
`p_0,q_0 in mu_m`. In the `e=1` case, `m=3h+1` gives `gcd(h,m)=1`. Scaling
all roots by `lambda in mu_m` sends a locator to

```text
lambda^h P(X/lambda),
```

so there is a unique `lambda` making `p_0=1`. Then `q_0=x`, `d=x-1`, and
`(BTP3)` rearranges to `(BTP5)`. QED.
