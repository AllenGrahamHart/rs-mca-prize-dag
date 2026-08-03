# Proof

Work in the proved six-dimensional quadratic-over-cubic source algebra with
basis `1,t,t^2,b,bt,bt^2`. For `xi=0`, the residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf,
```

and for `xi=2` it is

```text
de, de, df, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 12 is `((0,5),(1,2),(3,4))`. Put `u=df`. For fixed
`sigma_c`, the first two paired equations are

```text
P_u(u) = paired(second_de,u),
P_f(f) = paired(de,sigma_c c f).
```

Let `m,s` be the missing product and squared-sum values. Put `de=m, eta=1`
for `xi=0`, and `de=-m, eta=-1` for `xi=2`. Since `d=u/f` and
`e=de f/u`, every target satisfies

```text
J(u,f) = (u^2 + eta de f^2)^2 - s f^2 u^2 = 0.
```

After clearing the source denominator, write `P_u=A u^2+B u+C` and reduce
with `u^2=alpha u+beta`. The relation `J` has a linear remainder
`L(f)u+M(f)`, and a common root forces

```text
A M(f)^2 - B L(f)M(f) + C L(f)^2 = 0.
```

This eliminant has degree eight in `f`. Reducing it modulo the quadratic
`P_f` leaves a linear remainder; its quadratic resultant gives one
target-free element of the six-dimensional source algebra. Its direct
six-by-six multiplication norm agrees with the quadratic-over-cubic tower
norm in every row.

The census collects all deployed-field roots of the norm numerator and
denominator, every inversion-guard numerator and denominator, and the base
cubic leading coefficient. It lifts their union through the base cubic, the
`b` quadratic, linear `c` recovery, product-rank cofactors, and compact
kernel. No vanishing elimination coefficient is discarded.

For every source sign and `sigma_c`, an `xi=0` row has seven norm roots,
two live norm roots, 12 candidate `r` values, 16 source points, and two
`(u,f)` candidates. Both candidates fail the final paired equation in both
`sigma_o` lanes. An `xi=2` row has seven norm roots, two live roots, 11
candidate `r` values, 18 source points, and four `(u,f)` candidates. Two
have `f=0`, violating the target nonzero guard; the other two fail the final
paired equation in both `sigma_o` lanes.

Across the sixteen rows the exact ledger has 184 candidate `r` values, 272
source points, 48 `(u,f)` candidates, 16 terminal `f=0` boundaries, and 64
nonboundary final-pair evaluations. Every final-pair value is nonzero, with
zero witnesses and zero unresolved branches.

The sixteen computed rows pay `16*2=32` raw cases. Deleting the other
positive parallel `DE` copy preserves the residual products, missing squared
sum, matching 12, and all target guards value-for-value, so the 16 `xi=1`
raw cases transport from `xi=0`. All 48 stated cases are empty. QED.
