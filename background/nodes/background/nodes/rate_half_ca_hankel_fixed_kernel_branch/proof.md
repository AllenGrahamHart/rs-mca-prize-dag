# Proof

Put `M_i=M_r(y_i)`. From `(HK1)`, every `v in K_0` satisfies

```text
(M_0+Z M_1)v=0
```

over `F(Z)`. The left side is a vector of polynomials of degree at most one in
`Z`, so both coefficients vanish:

```text
M_0v=M_1v=0.                                           (1)
```

Thus `K_0` is contained in the kernel of every specialization. If `K_0`
contained a member of `D_r(D)`, that split locator would lie in both endpoint
kernels by `(1)`. The common-locator equivalence `(HS2)` would make the pair
column-close. Hence column farness gives

```text
K_0 intersect D_r(D)=empty.                            (2)
```

The generic rank is `rho`, so some `rho x rho` minor `Delta(Z)` is nonzero.
Every matrix entry is affine linear in `Z`, and therefore

```text
deg Delta<=rho.                                        (3)
```

All `(rho+1) x (rho+1)` minors vanish identically, so every finite
specialization has rank at most `rho`. If `Delta(gamma)!=0`, the rank is also
at least `rho`, hence equals `rho`. Its kernel then has dimension
`r+1-rho`, the same as `K_0`; the inclusion from `(1)` is therefore equality:

```text
ker M(gamma)=K_0.                                      (4)
```

By `(2)` and `(4)`, a slope carrying a member of `D_r(D)` must be a root of
`Delta`. A nonzero degree-at-most-`rho` polynomial has at most `rho` roots in
`F`, proving `(HK2)`. The Hankel split-pencil equivalence identifies these
supported slopes with the CA-bad slopes of a column-far pair. QED.
