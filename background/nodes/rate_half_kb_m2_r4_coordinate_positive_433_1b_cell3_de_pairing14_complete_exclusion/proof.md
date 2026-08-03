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

Canonical matching 14 is `((0,5),(1,4),(2,3))`. The first two equations
are quadratics in the same variable `f`:

```text
P_b(f) = paired(second_de,bf),
P_c(f) = paired(de,sigma_c cf).
```

Write these in ascending order as `P_b=a_0+a_1 f+a_2 f^2` and
`P_c=c_0+c_1 f+c_2 f^2`. A common root forces the division-free quadratic
resultant

```text
R_f = (a_2 c_0-a_0 c_2)^2
      -(a_2 c_1-a_1 c_2)(a_1 c_0-a_0 c_1)
```

to vanish. Its direct six-by-six multiplication norm agrees with the
quadratic-over-cubic tower norm in every row.

The exact census collects all deployed-field roots of the norm numerator and
denominator, every inverse-guard numerator and denominator, and the base
cubic leading coefficient. It lifts their union through the base cubic, the
`b` quadratic, linear `c` recovery, product-rank cofactors, and compact
kernel. At each source point it intersects the exact field-root sets of
`P_b` and `P_c`; no vanishing coefficient or exceptional stratum is
discarded.

For each common nonzero `f`, put `u=ef`. If `m,s` are the missing product
and squared-sum values, put `de=m, eta=1` for `xi=0`, and `de=-m, eta=-1`
for `xi=2`. The source relation becomes the monic quartic

```text
u^4 + f^2(2 eta de-s)u^2 + de^2 f^4 = 0.
```

All of its deployed-field roots are enumerated. A zero `f` is recorded as a
`nonzero_5` target boundary; a zero `u` would be a `nonzero_4` boundary.
For every remaining root, recover `e=u/f`, `d=de/e`, and directly check
`paired(df,sigma_o ef)` in both `sigma_o` lanes, replaying all three paired
equations and the original source relation if that final cut vanishes.

For each source sign the four `(sigma_c,xi)` profiles are:

```text
(-1,0): 6 norm roots, 1 live, 8 candidate r, 6 source points,
         8 (u,f), 0 boundaries, 16 final-lane checks;
(-1,2): 8 norm roots, 3 live, 10 candidate r, 12 source points,
         0 (u,f), 2 f=0 boundaries, 0 final-lane checks;
(+1,0): 6 norm roots, 1 live, 8 candidate r, 4 source points,
         0 (u,f), 0 boundaries, 0 final-lane checks;
(+1,2): 7 norm roots, 2 live, 9 candidate r, 12 source points,
         0 (u,f), 2 f=0 boundaries, 0 final-lane checks.
```

Across all sixteen rows this is 140 candidate `r` values, 136 source points,
32 nonboundary `(u,f)` candidates, 16 `f=0` boundaries, and 64 final-pair
evaluations. Every final-pair value is nonzero, with zero witnesses and zero
unresolved branches.

The sixteen computed rows pay `16*2=32` raw cases. Deleting the other
positive parallel `DE` copy preserves the residual products, missing squared
sum, matching 14, and all target guards value-for-value, so the 16 `xi=1`
raw cases transport from `xi=0`. All 48 stated cases are empty. QED.
