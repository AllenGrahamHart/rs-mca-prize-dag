# `A=1` exceptional quotient clean-fiber `W_vee` interpolation normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_first_jet_transversality`,
  `rate_half_ca_hankel_a1_core_one_two_sided_complement_weld`

Put

```text
d=deg P_cl=T-1,       deg_t W_vee<=T=d+1,
deg_Y W_vee<=r-1.                                      (QWI1)
```

For each clean slope `gamma`, let `S_gamma` be the `r` roots of
`F(gamma,Y)`. There is one unique polynomial `w_gamma(Y)` of degree at most
`r-1` satisfying

```text
w_gamma(y)=
 -P_cl'(gamma)E(gamma)y^N_sq
  /(F_t(gamma,y)U(gamma,y))       for y in S_gamma.   (QWI2)
```

Every corrected square has

```text
W_vee(gamma,Y)=w_gamma(Y).                            (QWI3)
```

Interpolate the coefficient of each `Y^j` in the `d` polynomials
`w_gamma` by its unique parameter polynomial of degree less than `d`; call
the resulting biform `W_0(t,Y)`. Then there are unique polynomials
`A_W(Y),B_W(Y)` of degree at most `r-1` such that

```text
W_vee(t,Y)=W_0(t,Y)+P_cl(t)(t A_W(Y)+B_W(Y)).         (QWI4)
```

Thus the clean-fiber part of the high-distance endpoint determines
`W_vee` modulo `P_cl`. Only the two univariate correction polynomials
`A_W,B_W` remain.
