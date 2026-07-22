# Proof

At a clean selected root, `(QJT4)` gives the value in `(QWI2)`, and every
denominator there is nonzero. The `r` roots in `S_gamma` are distinct. Since
`deg_Y W_vee<=r-1`, Lagrange interpolation gives one unique `w_gamma`, and
the first-jet theorem proves `(QWI3)`.

The clean-slope locator `P_cl` is squarefree of degree `d`. For each
`0<=j<r`, interpolate the coefficient `[Y^j]w_gamma` over its `d` roots by
the unique polynomial of parameter degree less than `d`. This defines
`W_0` with

```text
deg_t W_0<d,       deg_Y W_0<=r-1.                   (1)
```

Every coefficient in `W_vee-W_0` vanishes at every root of `P_cl`, so it is
divisible by `P_cl`. The inherited bound
`deg_t W_vee<=T=d+1` makes the coefficientwise quotient affine in `t`.
Collecting its linear and constant coefficients across powers of `Y` gives
`A_W,B_W`, each of degree at most `r-1`, and proves `(QWI4)`. Polynomial
division by monic `P_cl` also proves uniqueness. QED.
