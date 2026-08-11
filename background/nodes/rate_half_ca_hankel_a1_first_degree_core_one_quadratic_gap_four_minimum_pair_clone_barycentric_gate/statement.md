# `A=1` quadratic gap-four minimum-pair clone-barycentric gate

- **status:** PROVED
- **closure:** exact clone fibres and endpoint errors at pair union `rho+2`
- **consumer:** `rate_half_band_crossing_location`

Retain either quadratic `u=4` root pattern and distinct supported slopes
`alpha,beta` satisfying

```text
|S_alpha union S_beta|=rho+2.                       (QCB1)
```

Put `X=S_beta\S_alpha`, so `|X|=r_alpha+2`. There is a
nonzero degree-`e` parameter form `P_(alpha,beta)` and nonzero scalars
`lambda_x` such that

```text
Qbar(U,V;x)=lambda_x P_(alpha,beta)(U,V)   (x in X). (QCB2)
```

Every `x in X` is a saturated light row. Consequently
`P_(alpha,beta)` is squarefree and its roots are the same `e` supported
locator slopes for every member of `X`.

Let

```text
L_X(T)=product_(x in X)(T-x),                        (QCB3)
```

and let `v_x` be the nonzero RS dual multiplier. Up to one common nonzero
scalar `kappa`, the unique error at `beta` obeys

```text
(f_beta-c_beta)(x)
 =kappa/((x-s_0)v_x lambda_x L_X'(x))       (x in X). (QCB4)
```

The reverse orientation gives the analogous clone class of size
`r_beta+2` on `S_alpha\S_beta` and the analogous formula for the error at
`alpha`.

## Scope

The theorem classifies the sharp pair-union boundary. It does not prove that
such a pair exists, exclude its clone fibres, or constrain pairs with larger
union.
