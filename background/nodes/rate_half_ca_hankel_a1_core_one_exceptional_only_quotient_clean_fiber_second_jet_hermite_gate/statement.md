# `A=1` exceptional quotient clean-fiber second-jet Hermite gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_w_interpolation_normal_form`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_unit_bezout_remainder_gate`

Fix a clean selected incidence `(gamma,y)`. Let `y(t)` be its local root of
`F(t,y(t))=0`, and put dots for total parameter derivatives at `t=gamma`.
Besides the proved nonzero first velocity, one has

```text
ddot y=-(F_tt+2F_tY dot y+F_YY dot y^2)/F_Y.         (QSJ1)
```

All derivatives on the right are evaluated at `(gamma,y)`. The reversed
first-complement identity gives the exact second-jet formula

```text
2R_X'(y)dot y dot W
 =P_cl'' E y^N_sq
  +2P_cl'(E' y^N_sq+E N_sq y^(N_sq-1)dot y)
  -(R_X''(y)dot y^2+R_X'(y)ddot y)W_vee(gamma,y),   (QSJ2)

dot W=W_vee,t(gamma,y)+W_vee,Y(gamma,y)dot y.       (QSJ3)
```

Every denominator needed to recover `dot W` is nonzero. The first-jet
interpolation theorem already gives the whole polynomial
`w_gamma(Y)=W_vee(gamma,Y)`, so `(QSJ2)--(QSJ3)` determine
`W_vee,t(gamma,y)` at all `r` selected roots. Interpolate these values by the
unique polynomial `j_gamma(Y)` of degree at most `r-1` and define

```text
D_gamma(Y)=(j_gamma(Y)-W_0,t(gamma,Y))/P_cl'(gamma). (QSJ4)
```

Then every corrected square satisfies

```text
D_gamma=gamma A_W+B_W                              (QSJ5)
```

at every clean slope. Hence any two distinct clean slopes `alpha,beta`
reconstruct the corrections independently:

```text
A_W=(D_beta-D_alpha)/(beta-alpha),
B_W=(beta D_alpha-alpha D_beta)/(beta-alpha).        (QSJ6)
```

All remaining `D_gamma` must obey `(QSJ5)`, and the pair in `(QSJ6)` must
equal the pair reconstructed by the unit-remainder stream. Failure of either
comparison is an exact endpoint rejection certificate. This theorem does
not assert that either endpoint profile fails the comparisons.
