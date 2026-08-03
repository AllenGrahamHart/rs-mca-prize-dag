# Proof

Fix a source-sign pair and target lane.  Work in the proved global
quadratic quotient with basis `1,t,t^2,b,bt,bt^2`.  For `xi=0`, the
residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf,
```

and for `xi=2` it is

```text
de, de, df, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 6 is `((0,3),(1,2),(4,5))`.  Put `u=ef`, `v=df`.
The first two paired-resultant cuts are the quadratics

```text
P_u(u) = paired(de,sigma_o u),
P_v(v) = paired(second_de,v).
```

Let `m,s` be the missing product and squared-sum values.  Put
`de=m, eta=1` for `xi=0`, and `de=-m, eta=-1` for `xi=2`.
Since `d=v/f`, `e=u/f`, and `f^2=uv/de`, every target satisfies

```text
H(u,v) = de (u + eta v)^2 - s u v = 0.
```

The displayed square is unchanged by interchanging `u,v`, including when
`eta=-1`.  Regard `H` and `P_u` as quadratics in `u`.  For
`A u^2+B u+C` and `D u^2+E u+F`, the identity

```text
Res_u = (AF-CD)^2 - (AE-BD)(BF-CE)
```

gives a quartic in `v`.  Reducing it modulo the quadratic `P_v` leaves a
linear remainder.  Its quadratic resultant is a necessary element of the
six-dimensional source algebra.  The direct six-by-six multiplication norm
agrees with the quadratic-over-cubic tower norm in every row.

The exact census collects every field root of the norm numerator and
denominator, all inversion-guard numerators and denominators, and the
base-cubic leading coefficient.  It directly lifts their union through the
base cubic, the `b` quadratic, linear `c` recovery, product-rank cofactors,
and compact kernel.  No vanishing elimination coefficient is discarded as
a route boundary.

The 32 rows split into four eight-row profiles according to
`(xi,sigma_o)`:

```text
(0,-1): norm roots 7, live 2, candidate r 11, source points 14,
        uv candidates 0, boundaries 0
(0,+1): norm roots 8, live 3, candidate r 12, source points 14,
        uv candidates 2, boundaries 0
(2,-1): norm roots 9, live 2, candidate r 11, source points 18,
        uv candidates 2, boundaries 2
(2,+1): norm roots 8, live 1, candidate r 10, source points 14,
        uv candidates 2, boundaries 2
```

The counts are independent of `sigma_c` and the source-sign pair.  In the
second profile each necessary `(u,v)` candidate has two field-valued `f`
lifts, and all 32 aggregate colored-pair evaluations are nonzero.  In the
last two profiles every retained lift has `f=0` and violates the target
nonzero guard.  Thus no row reaches a colored-pair solution.  Aggregating
gives 352 candidate `r` values, 480 guarded source points, 48 `(u,v)`
candidates, 32 nonzero colored-pair evaluations, 32 terminal `f=0` records,
and zero witnesses or unresolved branches.

The 32 computed rows therefore pay 32 raw cases.  Deleting the other
positive parallel `DE` copy preserves the residual products, missing
squared sum, matching 6, and every target guard value-for-value, so the 16
`xi=1` raw cases transport from `xi=0`.  All 48 stated cases are empty.
QED.
