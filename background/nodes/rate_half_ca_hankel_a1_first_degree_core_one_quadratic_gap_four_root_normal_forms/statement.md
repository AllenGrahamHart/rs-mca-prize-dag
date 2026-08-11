# `A=1` core-one quadratic gap-four root normal forms

- **status:** PROVED
- **closure:** complete minimum-gap root, contact, and Picard classification
- **consumer:** `rate_half_band_crossing_location`

Retain the core-one parameter-constant first-degree profile with scalar
residual degree `a=2`. Put

```text
Delta=e-2,
u=Delta-I_H,       v=Delta-O.                        (QG41)
```

Then

```text
u+v=e+2,       u>=4.                                 (QG42)
```

At the minimum gap `u=4`, necessarily

```text
O=0,       I_0=0,       C_tot=I_H=e-6,       w=4.    (QG43)
```

Every excess root is simple and new relative to the minimal locator. The
residual quadratic has exactly one of the following two root patterns.

## Double root

The double root `x_*` is heavy, its row deficit is six, and its reduced
distinguished divisor `R_*` has degree `e-6`. There is an effective
degree-two proper vertical subdivisor `B` such that

```text
V_*=R_*+3B,
div(s_F)=R_*+2B,
O_C(rho+2,-e-1)=O_C(B).                              (QG44)
```

Moreover

```text
pi_*O_C(B)=O direct_sum O(1-d)^2 direct_sum O(-d)^(e-3),
d=rho-1,
h^0(C,O_C(B))=1.                                     (QG45)
```

The unique section in `(QG45)` is the reduced root-fibre section divided
by `s_F`.

## Two simple roots

Both roots are heavy. Up to interchanging them, their deficits and
corrections are

```text
(c_1,c_2)=((e+3)/2,(e+9)/2),
(q_1,q_2)=(3,9),       q_i=2c_i-e.                   (QG46)
```

For effective vertical divisors `P_1,P_2` of degrees one and three,

```text
V_i=2R_i+3P_i,
div(s_F)=R_1+R_2+P_1+P_2,                            (QG47)
```

and

```text
O_C(rho+3,-e-1)
 =O_C(R_1+R_2+2P_1+2P_2),
deg O_C(rho+3,-e-1)=e+2.                             (QG48)
```

## Scope

The theorem classifies but does not exclude either minimum-gap pattern. It
makes no assertion for `u>=5` or for the parameter-linear and
parameter-quadratic residual biforms.
