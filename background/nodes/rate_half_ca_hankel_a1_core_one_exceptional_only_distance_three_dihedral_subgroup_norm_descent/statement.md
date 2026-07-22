# `A=1` distance-three dihedral subgroup-norm descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_boundary_order_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_sparse_subgroup_norm_router`

Write

```text
B(X)=X^3-sigma_1 X^2+sigma_2 X-sigma_3,
R_D(z)=Res_X(X^N-1,Q(z;X)).                          (DSN1)
```

The pair-Lagrange coefficients define the orbit polynomial

```text
J(z;U)=sum_i (lambda_i/xi_i)L_i(z) E(U)/(U-u_i).     (DSN2)
```

It has `U`-degree at most `e-1`.

## Antipodal branch

If `A(X)=E(X^2)`, put

```text
P(z;U)=Phi(z)E(U)-z(sigma_1 U+sigma_3)J(z;U),
S(z;U)=z(U+sigma_2)J(z;U),
V_-(z;U)=P(z;U)^2-U S(z;U)^2.                       (DSN3)
```

Then `deg_U V_-<=2e+1=r` and

```text
R_D(z)=Res_U(U^(N/2)-1,V_-(z;U)).                   (DSN4)
```

## Constant-product branch

If `A(X)=X^eE(X+c/X)`, define

```text
K_c(U)=cU^2-2c^2-(sigma_1 c+sigma_3)U+2sigma_2 c,
L_c(U)=product_(t in T)(c+t^2-tU),

V_c(z;U)=c^(e-1)[c Phi(z)^2E(U)^2
                 +z Phi(z)E(U)J(z;U)K_c(U)
                 +z^2J(z;U)^2L_c(U)].              (DSN5)
```

Again `deg_U V_c<=r`. Let

```text
Fix_c={w in mu_N:w^2=c},
Omega_c(U)=product_(nonfixed orbits {x,c/x})
             (U-(x+c/x)).                           (DSN6)
```

The fixed-point set has size zero or two. If `D_j(U,c)` denotes the Dickson
polynomial defined by

```text
D_0=2,       D_1=U,       D_j=U D_(j-1)-c D_(j-2),
```

then the quotient locator is recovered without orbit enumeration:

```text
D_N(U,c)-2=
 [product_(w in Fix_c)(U-2w)] Omega_c(U)^2.          (DSN7)
```

Finally,

```text
R_D(z)=
 [product_(w in Fix_c)Q(z;w)] Res_U(Omega_c,V_c).   (DSN8)
```

At any parameter `z` for which `Q(z;X)` has exact degree `r` and nonzero
constant term, the corresponding identity also gives the exact split-slope
equivalence

```text
Q(z;X) splits over mu_N
 iff V_-(z;U) splits over mu_(N/2)                  (antipodal),
 iff V_c(z;U) splits over the roots of
        [product_(w in Fix_c)(U-2w)]Omega_c(U)       (constant product).
                                                               (DSN9)
```

Here splitting allows multiplicity. Thus external slopes and their root
blocks can be reconstructed in orbit coordinates.

Thus the sparse subgroup norm on either dihedral branch descends from an
`N`-point norm in `X` to an orbit norm with at most `N/2` nonfixed factors
and a degree-at-most-`r` value polynomial. Combined with the sparse norm
router, `(DSN4)` or `(DSN8)` is the norm input to the exact split
perfect-power test. This descent does not prove that test fails.
