# `A=1` core-one exceptional-only full reciprocal complement

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization`

Put

```text
s=D_0-r,       n_X=D_0-1,
A_vee(t,Y)=Y^s A_1(t,1/Y),
R_X(Y)=Y^n_X P_X(1/Y).                              (FRC1)
```

The infinity coefficient gives `A_vee(t,0)=P_cl j_inf`, so define

```text
U(t,Y)=(A_vee(t,Y)-P_cl j_inf)/Y,
deg_Y U<=D_0-r-1.                                   (FRC2)
```

With the reciprocal polynomials `F,L` from `(RRD2)--(RRD3)`, the complete
corrected complement descends to the exact polynomial identity

```text
F U+P_cl L=R_X.                                     (FRC3)
```

It has the exact resultant consequence

```text
Res_Y(F,R_X)=c_X P_cl^r E^(r-1).                    (FRC4)
```

The constant coefficient of `(FRC3)` is `(RBN2)`. At every clean slope
`gamma`, it specializes to

```text
F(gamma;Y)U(gamma;Y)=R_X(Y),                        (FRC5)
```

so the complete reciprocal quotient is prescribed there. Thus future
classification should solve one coefficientwise divisibility condition
`P_cl | (R_X-FU)` and set `L=(R_X-FU)/P_cl`, rather than allocate all lower
coefficients of `L` independently.

This is a necessary reduction, not a converse reconstruction theorem. A
candidate `F,U,L` must still satisfy `E | (YL-j_infF)` to recover `G`, the
unit and second complement identities, the Hankel chain, and all splitting
conditions.
