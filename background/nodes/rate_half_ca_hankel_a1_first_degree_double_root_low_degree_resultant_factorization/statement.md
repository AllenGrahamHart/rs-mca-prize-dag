# `A=1` first-degree double-root low-degree resultant factorization

- **status:** PROVED
- **closure:** exact linear/quadratic residual factor after supported norm
- **consumer:** `rate_half_band_crossing_location`

Use homogeneous parameter coordinates `(U:V)` and the standard homogeneous
`X`-resultant. For the core-free cubic double-root branch put

```text
P_3(X)=(X-x_s)^2(X-x_d)G_L(X),       d=rho,           (LRF1)
R_3(U,V)=Res_X(Q(U,V;X),P_3(X)).                       (LRF2)
```

For each no-ordinary gap-one packet there are `c in F^x` and a nonzero
binary linear form `S_A` over `F` such that

```text
R_3=c^3 H^rho S_A^3.                                 (LRF3)
```

For the ordinary gap-one packet, let `L_0` be the supported-slope form of
the ordinary point, write `H=L_0H_0`, and let `S_AB` be the binary quadratic
whose zero divisor is the parameter pushforward of `A+B`. Then

```text
R_3=c^3 L_0^(rho-3) H_0^rho S_AB^3.                 (LRF4)
```

For the core-one quadratic double-root packet at `u=4`, put

```text
P_2(X)=(X-x_d)G_L(X),       d=rho-1,                 (LRF5)
R_2(U,V)=Res_X(Q(U,V;X),P_2(X)).                      (LRF6)
```

There are `c in F^x` and a nonzero binary quadratic `S_B` over `F` whose
zero divisor is the parameter pushforward of `B`, such that

```text
R_2=c^3 H^(rho-1) S_B^3.                             (LRF7)
```

The total degrees agree exactly:

```text
deg R_3=3(rho+3)e=rho(rho+4)+3,
deg R_2=3(rho+2)e=(rho-1)(rho+4)+6.                  (LRF8)
```

## Scope

These are necessary exact factorizations, not exclusions. The forms `S_A`,
`S_AB`, and `S_B` are outputs determined by the contact-complement divisors;
they are not free search variables. A candidate with any other supported
multiplicity or residual degree is impossible.
