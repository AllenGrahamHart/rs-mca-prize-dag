# Proof

Use the proved six-dimensional source algebra with basis
`1,t,t^2,b,bt,bt^2`. Canonical matching 13 is
`((0,5),(1,3),(2,4))`. Put `u=ef`. For each target lane the first two
paired equations are

```text
P_u(u) = paired(second_de,sigma_o u),
P_f(f) = paired(de,sigma_c c f).
```

If `m,s` are the missing product and squared-sum values, put `de=m, eta=1`
for `xi=0`, and `de=-m, eta=-1` for `xi=2`. Since `e=u/f` and
`d=de f/u`, every target satisfies

```text
J(u,f) = (u^2 + eta de f^2)^2 - s f^2 u^2 = 0.
```

Reduce `J` modulo the quadratic `P_u`, take its degree-eight eliminant in
`f`, reduce that modulo `P_f`, and take the remaining quadratic resultant.
The resulting target-free element has matching direct six-by-six and
quadratic-over-cubic tower norms in every row.

The census lifts every norm and inverse-guard root through the base cubic,
`b` quadratic, linear `c` map, product-rank cofactors, and compact kernel.
No vanishing elimination coefficient is discarded. Each finite `(u,f)`
candidate is replayed against the source relation and the final equation
`paired(df,bf)`.

Every `xi=0` row has seven norm roots, two live roots, 12 candidate `r`
values, 16 source points, two `(u,f)` candidates, no boundary, and two
nonzero final checks. Every `xi=2` row has seven norm roots, two live roots,
11 candidate `r` values, 18 source points, four `(u,f)` candidates, two
`f=0` boundaries, and two nonzero final checks.

Across 32 rows this is 368 candidate `r` values, 544 source points, 96
`(u,f)` candidates, 32 `f=0` boundaries, and 64 nonboundary final-pair
evaluations. Every final value is nonzero, with zero witnesses and zero
unresolved branches.

The 32 computed rows pay 32 raw cases. Deleting the other positive parallel
`DE` copy preserves the residual products, missing squared sum, matching 13,
and all target guards value-for-value, so the 16 `xi=1` cases transport from
`xi=0`. All 48 stated cases are empty. QED.
