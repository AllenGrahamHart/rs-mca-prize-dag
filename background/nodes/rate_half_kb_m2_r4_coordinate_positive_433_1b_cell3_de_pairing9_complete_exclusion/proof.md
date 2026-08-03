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

Canonical matching 9 is `((0,4),(1,2),(3,5))`. Put `u=df`. The first two
paired equations are

```text
P_u(u) = paired(second_de,u),
P_f(f) = paired(de,b f).
```

Neither depends on the target lane. Let `m,s` be the missing product and
squared-sum values. Put `de=m, eta=1` for `xi=0`, and
`de=-m, eta=-1` for `xi=2`. Since `d=u/f` and `e=de f/u`, every target
satisfies

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

For every source sign, an `xi=0` row has ten norm roots, five live norm
roots, 15 candidate `r` values, 18 guarded source points, and four `(u,f)`
candidates. All four fail `paired(sigma_o ef,sigma_c cf)=0` in every target
lane. An `xi=2` row has eleven norm roots, six live roots, 15 candidate `r`
values, 36 source points, and six `(u,f)` candidates. Two have `f=0`,
violating the target nonzero guard, and the other four fail the final paired
equation in every target lane.

Across the eight source rows the exact ledger has 120 candidate `r` values,
216 guarded source points, 40 `(u,f)` candidates, eight terminal `f=0`
boundary records, and 128 nonboundary final-pair evaluations. Every
final-pair value is nonzero, with zero witnesses and zero unresolved
branches.

The eight computed source rows pay `8*4=32` raw cases. Deleting the other
positive parallel `DE` copy preserves the residual products, missing
squared sum, matching 9, and every target guard value-for-value, so the 16
`xi=1` raw cases transport from `xi=0`. All 48 stated cases are empty.
QED.
