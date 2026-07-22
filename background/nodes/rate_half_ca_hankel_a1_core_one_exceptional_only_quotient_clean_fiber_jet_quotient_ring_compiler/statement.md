# `A=1` exceptional quotient clean-fiber jet quotient-ring compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_second_jet_hermite_gate`

Fix a clean slope `gamma`, put `f=F(gamma,Y)`, and work in

```text
K_gamma=F_field[Y]/(f).
```

Write `p_1=P_cl'(gamma)`, `p_2=P_cl''(gamma)`, `e_0=E(gamma)`, and
`e_1=E'(gamma)`. Every denominator below is a unit in `K_gamma`. The value,
velocity, and acceleration classes are

```text
v=-F_t F_Y^(-1),                                    (QRC1)
a=-(F_tt+2F_tYv+F_YYv^2)F_Y^(-1),                  (QRC2)
w=-p_1e_0Y^(r-3)(F_tU)^(-1).                        (QRC3)
```

Here the official smooth-domain relation has already reduced

```text
Y^N_sq=Y^(r-3),       Y^(N_sq-1)=Y^(r-4)            (QRC4)
```

inside `K_gamma`. Define the total derivative class

```text
dot w={p_2e_0Y^(r-3)
       +2p_1(e_1Y^(r-3)+e_0N_sqY^(r-4)v)
       -(R_X''v^2+R_X'a)w}
      /(2R_X'v),                                     (QRC5)
```

and then

```text
j=dot w-w_Yv.                                        (QRC6)
```

The canonical degree-`<r` representatives are exactly

```text
w_gamma(Y)=W_vee(gamma,Y),
j_gamma(Y)=W_vee,t(gamma,Y).                         (QRC7)
```

Thus both clean-fiber interpolation inputs can be computed without listing
the `r` selected roots and without exponentiating to `N_sq`. This is an
algebraic compiler, not an official-scale complexity claim: dense
degree-`r` arithmetic is still forbidden, and an implementation at the
official parameters needs compressed locator and modular-arithmetic oracles.
