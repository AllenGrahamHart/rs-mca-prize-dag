# Proof

Choose one representative from each positive conjugate pair and put

```text
y_u=F(zeta_256^u)F(zeta_256^-u)>0.
```

Odd-character orthogonality and autocorrelation Parseval give

```text
sum_u y_u=64*18,
sum_u (y_u-18)^2=128E=64V,
Norm(F(zeta_256))=product_u y_u,                    (1)
```

where `V=2E`.

Fix `V>0`. A positive product maximum subject to `(1)` is attained in the
interior. Lagrange multipliers show that every `y_u` is one of at most two
positive roots of one quadratic. If the lower root occurs `j` times, then

```text
a_(V,j)=18-sqrt(V(64-j)/j),
b_(V,j)=18+sqrt(Vj/(64-j)),
M_(V,j)=a_(V,j)^j b_(V,j)^(64-j).                  (2)
```

Only `a_(V,j)>0` is feasible, and the norm is at most the maximum of `(2)`.

For each fixed feasible `j`, differentiation gives

```text
d/dV log M_(V,j)
 =sqrt(j(64-j))/(2sqrt(V))*(1/b_(V,j)-1/a_(V,j))<0. (3)
```

Thus it suffices to check `V=36`, corresponding to `E=18`: every chamber
feasible at a larger variance was already feasible at 36 and is smaller by
`(3)`.

At `V=36`, feasibility is equivalent to `j=7,...,63`. The verifier encloses
each square root in `(2)` between adjacent rationals of denominator `2^192`.
Using the upper endpoint for `a` and `b` in the direction that enlarges the
product gives 57 exact rational upper bounds, all satisfying

```text
M_(36,j)<514*B_P*2^128.                            (4)
```

The closest comparison is `j=63`. Equations `(1)--(4)` contradict
`Norm=514p` with `p>=B_P 2^128` whenever `E>=18`.

For boundary discipline, the lower rational product bound at `(V,j)=(34,63)`
is strictly above `514*B_P*2^128`. The envelope therefore makes no claim at
`E=17`. QED.
