# `A=1` shape-A padded-center Pade transversality

- **status:** PROVED
- **closure:** the unique padded center is the sole simple center contact
  of the locator and Pade numerator
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A and let `gamma_0` be the large-class center. With the
center quotient from the coprimality theorem,

```text
Qbar(gamma_0,X)
 =chi_0(X-x_*)L_rest,0(X),
P_F(gamma_0,X)
 =chi_0(X-x_*)C_0(X).                            (PCT1)
```

Then

```text
C_0(x_*)!=0,
B_src(gamma_0,x_*)!=0.                           (PCT2)
```

The two projective curves `Qbar=0` and `P_F=0` meet at
`(gamma_0,x_*)` with local intersection multiplicity exactly one. In
particular, they are smooth and transverse there, and there is no other
common point over `gamma_0`.

At either small center `gamma`, the specialized polynomials
`Qbar(gamma,X)` and `P_F(gamma,X)` are coprime.

## Scope

This is a locator/Padé contact theorem, not a Shape-A exclusion. It pins
the source-numerator pencil away from `gamma_0` at the outside point
`x_*`, but does not identify the parameter at which
`B_src(t,x_*)` vanishes.
