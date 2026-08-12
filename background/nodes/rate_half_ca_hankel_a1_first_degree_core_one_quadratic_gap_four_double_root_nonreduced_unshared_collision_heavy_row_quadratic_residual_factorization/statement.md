# `A=1` nonreduced collision heavy-row quadratic residual

- **status:** PROVED
- **closure:** exact supported/correction divisor with only a quadratic residual
- **consumer:** `rate_half_band_crossing_location`

Retain an unshared nonreduced exact collision. Let `g_*` be the squarefree
degree-`e-6` supported form for the slopes at which `x_*` is padded-heavy,
and write

```text
S_B=c_S ell_tau^2,       g_*(tau)!=0.              (HQR1)
```

Then the outside split-biform row has the exact factorization

```text
G(t,x_*)=g_*(t)S_B(t)T_2(t),                      (HQR2)
```

up to one nonzero scalar, where

```text
T_2!=0,       deg T_2=2,
T_2(tau)!=0,       gcd(T_2,S_B)=1.                (HQR3)
```

Let `X`, `lambda`, `P_x`, and the value weights `b_x` be those of the
barycentric split-jet gate. Put

```text
H_NR=g_*S_B,       deg H_NR=e-4,
R_lambda(t)=sum_(x in X)b_x lambda_xP_x(t).        (HQR4)
```

Every survivor satisfies the exact quadratic-remainder gate

```text
H_NR divides R_lambda,
R_lambda/H_NR=T_2,       deg T_2=2,
(R_lambda/H_NR)(tau)!=0.                           (HQR5)
```

Equivalently, in an affine chart whose infinity misses `H_NR`, let
`B_NR` have one column per classified row,

```text
(B_NR)_x=coefficients of b_x rem_(H_NR)(P_x).      (HQR6)
```

Then `B_NR` has `e-4` coefficient rows and

```text
B_NR lambda=0.                                    (HQR7)
```

## Scope

The theorem does not show that the remainder matrix excludes the unique
weld vector. It reduces the nonreduced heavy row to three quotient
coefficients and retains the required nonvanishing at the correction.
