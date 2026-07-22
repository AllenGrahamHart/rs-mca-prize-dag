# `A=1` exceptional quotient clean-fiber first-jet transversality

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_square_descent`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_two_sided_resultant_saturation`,
  `rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition`

Retain the reciprocal corrected-square identities

```text
FU+P_cl L=R_X,
L W_vee-FS=E Y^N_sq,       N_sq=n_X+r-1.             (QJT1)
```

Let `gamma` be an ordinary supported slope, so `P_cl(gamma)=0`, and let
`y` be a root of the split squarefree divisor `F(gamma,Y)` of the fixed
squarefree domain locator `R_X`. Then

```text
F_t(gamma,y) U(gamma,y)+P_cl'(gamma)L(gamma,y)=0,    (QJT2)
L(gamma,y)W_vee(gamma,y)=E(gamma)y^N_sq,            (QJT3)

F_t(gamma,y)U(gamma,y)W_vee(gamma,y)
  =-P_cl'(gamma)E(gamma)y^N_sq.                      (QJT4)
```

Every factor in `(QJT4)` is nonzero. In particular, every selected domain
root is transverse in the parameter direction. Writing `dot y` for its
local velocity gives the exact formula

```text
dot y=-F_t/F_Y
     =P_cl'(gamma)E(gamma)y^N_sq
        /(R_X'(y)W_vee(gamma,y)).                    (QJT5)
```

On the official multiplicative domain of order `M=2^41`, let `s` be the
fixed core point and `x_0` the unique zero-trace row. In reciprocal
coordinates,

```text
R_X(Y)=(1-Y^M)/((1-sY)(1-x_0Y)).                    (QJT6)
```

Here `n_X=M-2`, so `N_sq=M+r-3`. Thus `y^M=1` and

```text
dot y=-[P_cl'(gamma)E(gamma)/M]
       y^(r-2)(1-sy)(1-x_0y)/W_vee(gamma,y),         (QJT7)
```

where the denominator in the scalar is the domain order `M`, not `N_sq`.
Thus the high quotient-distance endpoint is not controlled only by its
resultant multiplicities: every clean incidence also carries the prescribed
first-jet weight `(QJT7)`, whose numerator has degree `r` in the domain
coordinate.
