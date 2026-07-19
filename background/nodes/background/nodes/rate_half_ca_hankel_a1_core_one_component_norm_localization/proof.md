# Proof

Use the component incidence notation from the localization theorem. It gives

```text
D_i=T*r_i-I_i,       C_i=D_0*e_i-I_i,                 (1)
sum_i D_i=O-E,       sum_i C_i=C-E.
```

The adjugate theorem proves that residual rank loss, hence residual root
omission, is supported only at the one projective root of `lambda`. Every
other supported slope makes the full `Qbar_gamma` squarefree and split over
`D\S`, so its component root sets are disjoint there. Thus component overlap
is also confined to the exceptional slope. Since `0<=E<=O<=1`, equation `(1)`
proves `(CNL4)` and the assertion that at most one `D_i` is nonzero.

Subtract the two deficits in `(1)`:

```text
C_i-D_i=D_0*e_i-T*r_i.                                (2)
```

Here `D_0=8e+7` and `T=4e+1`. For a residual component `r_i=2e_i`, equation
`(2)` gives `C_i-D_i=5e_i`. For the dominant component,

```text
C_*-D_*=5e_*-T
         =5(e-b)-(4e+1)
         =e-5b-1.
```

This proves `(CNL5)`. Since the official `e` is `3 modulo 5` and
`b<=floor(e/5)`, one has `e-5b-1>=2`. Every nonsaturated component row
contributes at least one to `C_i`, proving the saturation bounds; for the
dominant component,

```text
D_0-C_*>=D_0-(e-5b)=14m+5b.
```

For the norm identity, every distinct root of `Q_i(gamma;X)` in `D\S`
contributes one factor `L_gamma` to `R_i`. Hence

```text
R_i=(product_gamma L_gamma^u_(i,gamma))S_i.
```

The residual degree is

```text
deg S_i=D_0*e_i-sum_gamma u_(i,gamma)=C_i.
```

Multiplication by `J_i` proves `(CNL7)`.

At a component-saturated residual row, `Q_i(U,V;x)` has `e_i` distinct roots
in the supported set and divides the squarefree form `P`. Interpolate the
parameter coefficients of `P/Q_i(U,V;x)` over `D_sat,i` to obtain `V_i`.
Then `Q_iV_i-P` vanishes at every root of `P_sat,i`, so division gives
`(CNL8)`. Parameter degrees are immediate; division by a polynomial of degree
`D_0-b_i` leaves `X`-degree at most `r_i-1`. This completes the proof. QED.
