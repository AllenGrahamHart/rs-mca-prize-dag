# Proof

Fix a source-sign pair and target lane. On the proved cell-4 four-basis
tower, work over `F_p(r)` with

```text
1, t, b, bt,
```

where `t` is quadratic, `b` is quadratic over `F_p(r,t)`, and `c` is
recovered linearly. Reduced FLINT fractions retain the numerator and
denominator of every inversion guard.

For `xi=0`, the residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf.
```

For `xi=2`, it is

```text
de, de, df, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 3 is `((0,2),(1,3),(4,5))`. Put `u=df`, `v=ef`, and
let `P_u(u)`, `P_v(v)` be the first two paired-resultant cuts. Both are
quadratic. If `m` and `s` are the source missing product and squared-sum
values, set `de=m, eta=1` for `xi=0`, and `de=-m, eta=-1` for `xi=2`.
Every target satisfies

```text
H(u,v) = de (u + eta v)^2 - s u v = 0.                 (1)
```

After clearing the already-guarded missing-record denominator, regard
`H` and `P_u` as quadratics in `u`. For quadratics
`A u^2+B u+C` and `D u^2+E u+F`, the identity

```text
Res_u = (AF-CD)^2 - (AE-BD)(BF-CE)
```

gives a quartic in `v`. A division-free pseudo-remainder modulo `P_v`
leaves `L v+M`. A common root forces

```text
L^2 C_v - L M B_v + A_v M^2 = 0.                     (2)
```

The compiler multiplies (2) by `A_v` before taking the four-dimensional
tower norm, so specialization where the leading coefficient drops is
included rather than divided away.

For each of 32 computed sign/lane/omission rows, the compiler takes the
union of every field root of the norm numerator, norm denominator, and all
inversion-guard numerators and denominators. It lifts that union through the
quadratic `t` relation, quadratic `b` relation, linear `c` recovery, and the
original compact kernel. At each guarded source point it solves
`P_u=P_v=0`, checks (1), solves `f^2=uv/de`, reconstructs `d=u/f` and
`e=v/f`, and checks the third colored pair and original target guards.

The direct ledger contains 312 candidate `r` values and 272 guarded source
points. Of 816 `(u,v)` pairs, 752 fail (1). The remaining 64 produce 112
`f` rows: 96 have a nonzero colored-pair cut and 16 have `f=0`, failing the
explicit target nonzero guard. No row reaches a colored solution, witness,
or unresolved terminal. Hence `xi=0` and `xi=2` are empty.

Deleting the other positive `DE` copy leaves the ordered residual products,
missing squared sum, matching, and guards unchanged. Thus the 16 `xi=1`
cases transport value-for-value from `xi=0`. The 32 computed and 16
transported cases prove all 48 stated cases empty. QED.
