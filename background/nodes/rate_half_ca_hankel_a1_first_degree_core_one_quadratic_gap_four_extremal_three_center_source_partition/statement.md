# `A=1` quadratic extremal three-center source partition

- **status:** PROVED
- **closure:** exact three-class partition of the extremal line source
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal branch of the three-center minimum-word reduction. Put

```text
p=rho/2,
A={alpha,beta,theta},
d_A=sum_(gamma in A)r_gamma in {0,1},
U=S_alpha union S_beta,
U_0=U\{s_0}.                                        (ESP1)
```

Let `c^L(t)` be the affine codeword line through the three assigned centers
and set

```text
b(t)=f(t)-c^L(t).                                    (ESP2)
```

Then `supp(b_0,b_1)=U`. For `gamma in A`, define

```text
M_gamma={x in U_0:b(gamma)(x)=0}=U_0\S_gamma.       (ESP3)
```

The three sets are pairwise disjoint and

```text
|M_gamma|=p-1+r_gamma.                              (ESP4)
```

Consequently,

```text
d_A=1  =>  U_0=M_alpha disjoint_union M_beta
                    disjoint_union M_theta,

d_A=0  =>  U_0=M_alpha disjoint_union M_beta
                    disjoint_union M_theta disjoint_union {x_circ}.
                                                               (ESP5)
```

Let `ell_gamma(t)` be any nonzero parameter-linear form vanishing at
`gamma`. The core-contracted source form

```text
omega_x(t)=(x-s_0)v_x b(t)(x)                       (ESP6)
```

obeys, for fixed nonzero scalars `eta_x`,

```text
omega_x(t)=eta_x ell_gamma(t)       (x in M_gamma). (ESP7)
```

If the exceptional coordinate `x_circ` occurs, its nonzero source form has
no zero among `alpha,beta,theta`.

## Scope

The theorem identifies all source-root classes on the extremal center line.
It does not constrain the coordinate scalars `eta_x`, and it does not assert
that the possible fourth source root is a supported slope.
