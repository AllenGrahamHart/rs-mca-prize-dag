# Proof

Fix a source-sign pair and target lane.  On the proved global quadratic
quotient, write the guarded source algebra over `F_p(r)` in the six-element
basis

```text
1, t, t^2, b, bt, bt^2,
```

where `t` satisfies the printed cubic, `b` the printed palindromic
quadratic, and `c` is recovered linearly.  The direct six-by-six
multiplication norm is checked against the quadratic-over-cubic tower norm.

For `xi=0`, the residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf.
```

For `xi=2`, it is

```text
de, de, df, sigma_o ef, bf, sigma_c cf.
```

Canonical matching 3 is `((0,2),(1,3),(4,5))`.  Put `u=df`,
`v=ef`, and let `P_u(u)`, `P_v(v)` be the first two paired-resultant
cuts.  Both are quadratic.  If `m` and `s` are the source missing product
and squared-sum values, put `de=m, eta=1` for `xi=0`, and
`de=-m, eta=-1` for `xi=2`.  Every target must satisfy

```text
H(u,v) = de (u + eta v)^2 - s u v = 0.
```

Regard `H` and `P_u` as quadratics in `u`.  For
`A u^2+B u+C` and `D u^2+E u+F), the exact identity

```text
Res_u = (AF-CD)^2 - (AE-BD)(BF-CE)
```

gives a quartic in `v`.  Reducing it modulo the quadratic `P_v` leaves
`L v+M`.  A common root therefore forces

```text
L^2 C_v - L M B_v + A_v M^2 = 0,
```

where `P_v=A_v v^2+B_v v+C_v`.  Taking the six-dimensional norm gives a
necessary univariate condition in `r`.

The exact census does not treat vanishing elimination coefficients as route
boundaries.  It collects every field root of the norm numerator and
denominator, every inversion-guard numerator and denominator, and the base
cubic leading coefficient.  It then directly lifts their union through the
base cubic, the `b` quadratic, the `c` recovery equation, the product-rank
cofactors, and the compact kernel.  At every guarded source point it solves
`P_u=P_v=0), checks `H=0), solves `f^2=uv/de`, and tests the omitted
colored pair and all target guards.

Across the `32` computed rows, the candidate-root sets have sizes 10, 11,
or 12 and lift to 14 or 18 guarded source points.  There are zero unresolved
branches and zero witnesses.  Twenty-four rows retain two `(u,v)`
candidates; their only terminal records total `32` copies of `f=0`, all
rejected by the explicit target nonzero guard.  The other eight rows have no
`(u,v)` candidate.  Thus the `xi=0` and `xi=2` rows are empty.

Deleting the other positive parallel `DE` copy preserves the residual
product list, missing squared sum, matching 3, and every target guard
value-for-value.  Hence the 16 `xi=1` raw cases transport from `xi=0`.
Together, 32 computed and 16 transported cases prove all 48 stated cases
empty. QED.
