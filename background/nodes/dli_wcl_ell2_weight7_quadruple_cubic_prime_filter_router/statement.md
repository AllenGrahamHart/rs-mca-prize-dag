# WCL `(2,7)` quadruple-cubic prime-filter router

- **status:** PROVED
- **closure:** proof
- **dependency:** `dli_wcl_ell2_weight3_ambient_exclusion`
- **consumer:** `dli_wcl_slot_2_7_emptiness`

Let `zeta` have order `N=1024`. From a reduced signed weight-seven double
relation, select four terms and scale one of them to `1`. Write the selected
quadruple as `Q={1,x,y,z}` and put

```text
u=e_1(Q),       A=e_2(Q),       B=e_3(Q),
d=product_(t in T)t,            W=uA-B-d,                (QCR1)
```

where `T` is the complementary triple. At an official supporting prime,
`u!=0`: otherwise the complementary reduced triple has sum zero, contrary
to the paid order-1024 weight-three ambient exclusion.

If the complementary roots are multiplied by `u`, their elementary
symmetric functions are

```text
sigma_1=-u^2,       theta_1=uW,       pi_1=u^3d.         (QCR2)
```

Define by repeated doubling

```text
sigma_(2m)=sigma_m^2-2theta_m,
theta_(2m)=theta_m^2-2pi_m sigma_m,
pi_(2m)=pi_m^2.                                      (QCR3)
```

Then the complementary cubic has all three roots in `mu_1024` exactly when

```text
F=sigma_1024-3u^1024=0,
G=theta_1024-3u^2048=0.                              (QCR4)
```

The zero branch `F=G=0` cannot occur identically in characteristic zero.

## Exact prime filter

Represent `F,G,u` by polynomials modulo
`Phi_1024(X)=X^512+1`, and let

```text
g_0=gcd(|Norm(F)|,|Norm(G)|),       U=|Norm(u)|.       (QCR5)
```

Every supporting characteristic divides `g_0`. For every prime `p|g_0`,
compute over `F_p[X]`

```text
H_p=gcd(Phi_1024,F,G),
H_p^*=H_p/gcd(H_p,u).                                 (QCR6)
```

There is a common embedding with `F=G=0` and `u!=0` exactly when
`deg H_p^*>0`. If `p` does not divide `U`, then `gcd(H_p,u)=1`; if `p`
divides both `g_0` and `U`, the quotient is load-bearing because rational
norms do not remember whether the same split embedding zeros all three
elements. Thus the complete sound filter is:

1. factor `g_0` and apply `(QCR6)` to every prime factor;
2. retain exactly the factors with `deg H_p^*>0`;
3. reconstruct the complementary cubic and check distinctness,
   disjointness, and the original two moments.

Blind removal of all `U` factors is not justified; `(QCR6)` repairs the gap
without a separate single-equation weight-four theorem.

## Exact route size

Let `W_4` be the pairs `(Q,c)` where `Q` is a legal antipodal-free
four-subset of `Z/1024` and `c` is the exponent of `d`. The affine group

```text
(a,r):(Q,c) -> (aQ+r, ac+3r),       a odd,             (QCR7)
```

owns the normalized presentations. Exact Burnside enumeration gives

```text
|W_4 / AGL|=94,652,815.                                (QCR8)
```

This is an exact complete router, not a feasible census: it is 233.9 times
the closed `(2,6)` orbit count. No broad run is authorized, and no official
prime or `(2,7)` relation is excluded.
