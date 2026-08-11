# Proof

Use the integral curve and point `P_*` from the Picard pin, and pass to the
normalization. Let

```text
D_G=div(G),       D_H=div(H),
K=min(D_G,D_H),
Z_+=D_G-K,        P_-=D_H-K.                          (1)
```

Put `p=deg P_-`. The pole-ideal bound gives

```text
0<=p<=O<=1.                                           (2)
```

The support of `K` is exactly the distinct grid incidence set. Since
`deg D_H=T rho` and the number of distinct incidences is `T rho-O`,

```text
deg K=T rho-p,
deg K-(T rho-O)=O-p.                                  (3)
```

Thus the total common-divisor multiplicity in excess of one per distinct
incidence is exactly `O-p<=1-p`.

Let `d<=1` and `F` be the clearing form in the Picard pin. If `d=1`, write
`x_F` for its unique domain root and `E_F` for the full degree-`e` fibre. If
`d=0`, omit this term. The pole divisor `P_-` is contained in `E_F` whenever
`p=1`. Pulling back `(FCP5)` and taking divisors gives

```text
3P_*+Z_+ + d E_F-P_-=pi_X^* div(A_d).                 (4)
```

The right side is a sum of complete `X`-fibres. Also

```text
D_G=sum_(x in D) E_x,
Z_+=sum_(x in D)(E_x-K_x),                            (5)
```

where `K_x` is the part of `K` over `x`.

Put `x_*=pi_X(P_*)`. First suppose either `d=0` or `d=1` with
`x_*!=x_F`. On the fibre over `x_*`, equation `(4)` has no clearing-fibre
term. If `x_*` is not in `D`, its left side has degree three, which is not a
multiple of `e>3`. If `x_*` is in `D`, the fibre part is

```text
E_(x_*)-K_(x_*)+3P_*.
```

For it to be a complete multiple of `E_(x_*)`, degree comparison forces one
copy and `deg K_(x_*)=3`; equality of divisors then forces

```text
K_(x_*)=3P_*.                                        (6)
```

This one distinct incidence contributes at least two units of excess
multiplicity, contradicting `(3)`. Hence necessarily

```text
d=1,       x_*=x_F.                                  (7)
```

Write this common coordinate as `x_0`. If `x_0` is not in `D`, the fibre
part in `(4)` has degree

```text
e-p+3,
```

which is neither `e` nor `2e` for `e>3` and `p in {0,1}`. Thus `x_0 in D`.
The fibre part is now

```text
2E_(x_0)-K_(x_0)-P_-+3P_*.                           (8)
```

If `k=deg K_(x_0)`, its degree is `2e-k-p+3`. The only possible complete
fibre multiple is two copies, forcing

```text
k=3-p,
K_(x_0)+P_-=3P_*.                                    (9)
```

All divisors in the second equality are effective of degree three, so they
are supported at `P_*`. The common divisor therefore has multiplicity
`3-p` at one distinct incidence and contributes at least

```text
(3-p)-1=2-p                                           (10)
```

units of excess multiplicity. But `(3)` allows at most `1-p`. This final
contradiction excludes `(FDE1)`. Combined with the slope-slack exclusion, no
strict `A=3` failure remains. QED.
