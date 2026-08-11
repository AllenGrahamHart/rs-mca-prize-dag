# `A=1` core-one quadratic gap-four two-simple marked factorization

- **status:** PROVED
- **closure:** exact square-times-cube row forms and sixth-power marked determinants
- **consumer:** `rate_half_band_crossing_location`

Retain the two-simple-root arm of the core-one scalar quadratic packet at
`u=4`. Let `x_1,x_2` be labeled as in `(QG46)`, and let `G_i(U,V)` be the
squarefree supported-slope form cutting out the distinguished divisor
`R_i`. Let `S_i(U,V)` cut out the pushforward of `P_i` in `(QG47)`. Then

```text
deg G_1=(e-3)/2,       deg S_1=1,
deg G_2=(e-9)/2,       deg S_2=3.                    (TSF1)
```

For nonzero constants `c_1,c_2 in F^x`, the two heavy-row parameter
polynomials factor exactly over the base field:

```text
Q(U,V;x_1)=c_1 G_1^2 S_1^3,
Q(U,V;x_2)=c_2 G_2^2 S_2^3.                         (TSF2)
```

Let `M_1(U,V)` be the core-one symmetric middle Hankel pencil and

```text
adj M_1=D_1qq^T,       deg D_1=e-2.                  (TSF3)
```

For every `tau in F^x`, the two rank-one marked determinants are

```text
det(M_1+tau nu(x_i)nu(x_i)^T)
 =tau c_i^2D_1G_i^4S_i^6,       i in {1,2}.          (TSF4)
```

In characteristic three, the quotient forms satisfy the exact derivative
tests

```text
d/dz (Q(z;x_i)/G_i(z)^2)=0,       i in {1,2}.        (TSF5)
```

## Scope

The factors `S_i` are outputs of the vertical divisors, not free variables.
They may share roots with `G_i` or with each other. The theorem gives
necessary factorizations and does not exclude the packet or constrain the
overlap of the two supported incidence sets.
