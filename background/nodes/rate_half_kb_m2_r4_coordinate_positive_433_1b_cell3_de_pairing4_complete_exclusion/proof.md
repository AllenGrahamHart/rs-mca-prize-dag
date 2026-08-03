# Proof

Work in the proved six-dimensional quadratic-over-cubic source algebra with
basis `1,t,t^2,b,bt,bt^2`.  For `xi=0`, the residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf,
```

and for `xi=2` it is

```text
de, de, df, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 4 is `((0,2),(1,4),(3,5))`.  Put `u=df`.
The first two paired-resultant equations are therefore a quadratic
`P_u(u)` and a quadratic `P_f(f)`; neither depends on the target lane.
Let `m,s` be the missing product and squared-sum values.  Put
`de=m, eta=1` for `xi=0`, and `de=-m, eta=-1` for `xi=2`.
Since `d=u/f` and `e=de f/u`, every target must satisfy

```text
J(u,f) = (u^2 + eta de f^2)^2 - s f^2 u^2 = 0.
```

After clearing the source denominator, write
`P_u=A u^2+B u+C` and reduce with
`u^2=alpha u+beta`, where `alpha=-B/A`, `beta=-C/A`.
Then `J` has a linear remainder `L(f)u+M(f)), and a common root forces

```text
A M(f)^2 - B L(f)M(f) + C L(f)^2 = 0.
```

This eliminant has degree eight in `f`.  Reducing it modulo the quadratic
`P_f` leaves a linear remainder; its quadratic resultant gives one
target-free element of the six-dimensional source algebra.  Its direct
six-by-six multiplication norm agrees with the quadratic-over-cubic tower
norm in every row.

The exact census collects all field roots of the norm numerator and
denominator, all inversion-guard numerators and denominators, and the
base-cubic leading coefficient.  It directly lifts their union through the
base cubic, the `b` quadratic, linear `c` recovery, product-rank
cofactors, and compact kernel.  No vanishing elimination coefficient is
discarded as a route boundary.

For each source sign, the `xi=0` row has 14 candidate `r` values, 20
guarded source points, and no `(u,f)` candidate.  The `xi=2` row has 15
candidate `r` values and 36 guarded source points.  It retains six
`(u,f)` candidates: two have `f=0`, violating the target nonzero guard,
and the other four fail the third paired equation in each of the four target
lanes.  Thus the exact ledger has 64 nonboundary third-pair evaluations, all
nonzero, and zero witnesses or unresolved branches.

The eight computed source rows therefore pay `8*4=32` raw cases.  Deleting
the other positive parallel `DE` copy preserves the residual products,
missing squared sum, matching 4, and all target guards value-for-value, so
the 16 `xi=1` raw cases transport from `xi=0`.  All 48 stated cases are
empty. QED.
