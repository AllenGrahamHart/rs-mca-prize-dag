# `A=1` shape-A primitive source-pencil three-center fibers

- **status:** PROVED
- **closure:** the parameter-linear source numerator defines a primitive
  domain map with three exact center fibers
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A and homogenize the source numerator as

```text
B_src(t,X) in S_1(t) tensor S_(R-1)(X),
R=|U_0|=(9e-7)/2.                                (PSP1)
```

Its two parameter coefficients are independent. Let `H(X)` be their
homogeneous gcd, put `h=deg H`, and write

```text
B_src(t,X)=H(X) B_prim(t,X).                     (PSP2)
```

Then `B_prim` is a basepoint-free pencil of domain degree

```text
D=R-1-h,                                         (PSP3)
```

and defines a morphism

```text
phi:P^1_X -> P^1_t,       deg phi=D,             (PSP4)
```

by `B_prim(phi(X),X)=0`. The fixed factor obeys

```text
gcd(H,L_U0)=1,       H(x_*)!=0,       0<=h<=d-2. (PSP5)
```

For each center, the Pade quotient factors further as

```text
C_gamma=H Cbar_gamma,
B_prim(gamma,X)=L_Mgamma(X)Cbar_gamma(X).         (PSP6)
```

The three projective residual degrees are exact:

```text
deg Cbar_alpha=deg Cbar_beta=d-1-h,
deg Cbar_(gamma_0)=d-2-h.                        (PSP7)
```

On the classified domain the fibers are exactly the source classes:

```text
phi^(-1)(gamma) intersect U_0=M_gamma            (PSP8)
```

as sets. Also

```text
phi(x_*)!=gamma_0.                               (PSP9)
```

The three residuals are pairwise coprime, and before primitive
normalization their pairwise gcd is exactly the fixed factor:

```text
gcd(C_gamma,C_delta)=H       (gamma!=delta),
gcd(Cbar_gamma,Cbar_delta)=1.                    (PSP10)
```

Finally, if `(u_alpha,u_beta,u_theta)` is the unique projective relation
among evaluations of parameter-linear forms at the three centers, then
every coefficient is nonzero and

```text
u_alpha L_Malpha Cbar_alpha
 +u_beta L_Mbeta Cbar_beta
 +u_theta L_Mtheta Cbar_theta=0.                 (PSP11)
```

## Scope

This theorem does not determine the fixed degree `h`, the ramification of
`phi`, or the off-grid roots of the three residual fibers. Those are now
the exact primitive source-pencil frontier.
