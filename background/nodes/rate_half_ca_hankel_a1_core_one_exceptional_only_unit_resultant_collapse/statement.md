# `A=1` core-one exceptional-only unit-resultant collapse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation`

Retain the corrected exceptional-only system and write

```text
a=[X^r]Q=E q_bar,       n_X=D_0-1,
m=deg_X W<=r-1.                                      (EUR1)
```

Use the resultant constant `c_X` from `(ERS4)`. Then the unit pair
`W,B_1` satisfies the exact low-resultant identities

```text
Res_X(Q,B_1)=c_X q_bar,                              (EUR2)

Res_X(Q,W)=c_X^(-1)
             E^(m+n_X+1) q_bar^(m+n_X).             (EUR3)
```

If `v_inf!=0`, the infinity theorem gives `m=r-1`, and `(EUR3)` becomes

```text
Res_X(Q,W)=c_X^(-1)
             E^(n_X+r) q_bar^(n_X+r-1).             (EUR4)
```

No value of `m` is imposed when `v_inf=0`; `(EUR3)` remains exact with the
actual `X`-degree of `W`.

Consequently every affine common fiber of `Q` and `B_1` lies over a root of
the single degree-`e-1` form `q_bar`. Every common fiber of `Q` and `W` lies
over `E q_bar`. These statements include multiplicity through the printed
resultants. They are necessary intersection constraints, not a proof that
`q_bar` has no roots or that the corrected square is empty.
