# Proof

Choose one element from each conjugate pair of primitive `256`th roots and
put

```text
y_u=F(zeta^u)F(zeta^-u)>0.                           (2)
```

There are 64 such values. Odd-character orthogonality and the definition of
the autocorrelation variance give

```text
sum_u y_u=64*18,
sum_u (y_u-18)^2=64V,
R=product_u y_u.                                    (3)
```

## Sharp moment envelope

Fix a positive variance `V`. On the compact closure of the locus in (3), a
boundary point has zero product. Hence a positive maximum of `R` is attained
in the interior. Lagrange multipliers at an interior extremum give

```text
1/y=lambda+2 nu (y-18).
```

Every `y_u` is therefore one of at most two positive roots of one quadratic.
If the lower root occurs `j` times, where `1<=j<=63`, the two moment equations
in (3) force

```text
a_(V,j)=18-sqrt(V(64-j)/j),
b_(V,j)=18+sqrt(Vj/(64-j)),                          (4)
M_(V,j)=a_(V,j)^j b_(V,j)^(64-j).
```

Values of `j` for which `a_(V,j)<=0` are infeasible. Consequently

```text
R<=max_(1<=j<=63, a_(V,j)>0) M_(V,j).               (5)
```

This argument uses only positivity and the two exact moments. In particular,
it does not assume that every extremizing real tuple is a cyclotomic tuple.

## Exact prize comparison

Let

```text
B_P=317494674775468773183020924238786383963,
p_min=B_P 2^128.
```

The committed verifier treats every even `V` from 14 through 34 and every
feasible `j`. Each square root in (4) is enclosed between adjacent rationals
with denominator `2^192`. Subtracting the lower square-root endpoint in the
first factor and adding the upper endpoint in the second gives a rigorous
rational upper bound for `M_(V,j)`. All 649 feasible comparisons prove

```text
M_(V,j)<1024 p_min.                                  (6)
```

The closest comparison is `(V,j)=(14,63)`. Since a cofactor-`m` collision has
`R=mp` with `p>=p_min`, (5)-(6) contradict both `m=1024` and `m=1028`.

The parent theorem already restricts both classes to positive even
`V<=34` and excludes `V=2`; this leaves exactly (1). For boundary discipline,
the same interval engine uses lower endpoints at `(V,j)=(12,63)` and proves
`M_(12,63)>1024 p_min`. The envelope therefore makes no claim below 14.
