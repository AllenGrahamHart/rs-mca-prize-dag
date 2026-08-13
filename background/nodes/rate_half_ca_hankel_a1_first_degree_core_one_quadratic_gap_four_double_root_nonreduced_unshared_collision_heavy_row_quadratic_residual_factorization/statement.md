# `A=1` nonreduced collision center-adjusted heavy-row residual

- **status:** PROVED
- **closure:** exact off-line/correction divisor with residual degree `2+d_A`
- **consumer:** `rate_half_band_crossing_location`

Retain an unshared nonreduced exact collision. Let `g_*` be the squarefree
degree-`e-6` supported form for the slopes at which `x_*` is padded-heavy.
Put

```text
J_*=gcd(Lambda,g_*),       deg J_*=d_A,
g_off=g_*/J_*,             deg g_off=e-6-d_A,
S_B=c_S ell_tau^2,         g_*(tau)!=0.            (HQR1)
```

Then the outside split-biform row has the exact factorization

```text
G(t,x_*)=g_off(t)S_B(t)T_(2+d_A)(t),              (HQR2)
```

up to one nonzero scalar, where

```text
T_(2+d_A)!=0,       deg T_(2+d_A)=2+d_A,
T_(2+d_A)(tau)!=0,  gcd(T_(2+d_A),S_B)=1.         (HQR3)
```

Let `X`, `lambda`, `P_x`, and the value weights `b_x` be those of the
barycentric split-jet gate. Put

```text
H_row=g_off S_B,       deg H_row=e-4-d_A,
R_lambda(t)=sum_(x in X)b_x lambda_xP_x(t).        (HQR4)
```

Every survivor satisfies the exact remainder gate

```text
H_row divides R_lambda,
R_lambda/H_row=T_(2+d_A),
deg T_(2+d_A)=2+d_A,
(R_lambda/H_row)(tau)!=0.                          (HQR5)
```

Equivalently, in an affine chart whose infinity misses `H_row`, let
`B_row` have one column per classified row,

```text
(B_row)_x=coefficients of b_x rem_(H_row)(P_x).    (HQR6)
```

Then `B_row` has `e-4-d_A` coefficient rows and

```text
B_row lambda=0.                                    (HQR7)
```

## Scope

For `d_A=0`, this recovers the quadratic residual and `e-4` row modulus.
For `d_A=1`, the unique padded-heavy center is removed by `J_*`; the row
modulus has degree `e-5` and the residual is cubic. The theorem does not
show that either remainder matrix excludes the unique weld vector.
