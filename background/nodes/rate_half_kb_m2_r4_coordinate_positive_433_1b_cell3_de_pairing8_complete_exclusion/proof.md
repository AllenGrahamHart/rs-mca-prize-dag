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

Canonical matching 8 is `((0,3),(1,5),(2,4))`. Put `u=ef`. For a fixed
target lane, the first two paired equations are

```text
P_u(u) = paired(de,sigma_o u),
P_f(f) = paired(second_de,sigma_c c f).
```

Let `m,s` be the missing product and squared-sum values. Put
`de=m, eta=1` for `xi=0`, and `de=-m, eta=-1` for `xi=2`. Since
`e=u/f` and `d=de f/u`, every target satisfies

```text
J(u,f) = (u^2 + eta de f^2)^2 - s f^2 u^2 = 0.
```

After clearing the source denominator, write `P_u=A u^2+B u+C` and reduce
with `u^2=alpha u+beta`, where `alpha=-B/A` and `beta=-C/A`. Then
`J` has a linear remainder `L(f)u+M(f)`, and a common root forces

```text
A M(f)^2 - B L(f)M(f) + C L(f)^2 = 0.
```

This eliminant has degree eight in `f`. Reducing it modulo `P_f` leaves a
linear remainder; its quadratic resultant gives a target-free element of
the six-dimensional source algebra. Its direct six-by-six multiplication
norm agrees with the quadratic-over-cubic tower norm in every row.

The exact census collects all field roots of the norm numerator and
denominator, every inversion-guard numerator and denominator, and the
base-cubic leading coefficient. It directly lifts their union through the
base cubic, the `b` quadratic, linear `c` recovery, product-rank cofactors,
and compact kernel. No vanishing elimination coefficient is discarded as a
route boundary.

For every source sign and target lane, an `xi=0` row has eight norm roots,
three live norm roots, 13 candidate `r` values, 20 guarded source points,
and four `(u,f)` candidates. All four fail `paired(df,bf)=0`. An `xi=2`
row has seven norm roots, two live roots, 11 candidate `r` values, 18 source
points, and four `(u,f)` candidates. Two have `f=0`, violating the target
nonzero guard, and the other two fail `paired(df,bf)=0`.

Across the 32 computed rows the exact ledger has 384 candidate `r` values,
608 guarded source points, 128 `(u,f)` candidates, 32 terminal `f=0`
boundary records, and 96 nonboundary third-pair evaluations. Every
third-pair value is nonzero, with zero witnesses and zero unresolved
branches.

The 32 computed rows pay 32 raw cases. Deleting the other positive parallel
`DE` copy preserves the residual products, missing squared sum, matching 8,
and every target guard value-for-value, so the 16 `xi=1` raw cases transport
from `xi=0`. All 48 stated cases are empty. QED.
