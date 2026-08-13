# `A=1` quadratic nonreduced exact-collision Bezout/Smith router

- **status:** PROVED
- **closure:** exact corank-one/two and two-scalar Smith trichotomy
- **consumer:** `rate_half_band_crossing_location`

Retain the nonzero-jet alternative of the normalization/collision
dichotomy over odd residue characteristic. Complete at `tau`, put
`z=t-tau`, and write `y=X-x_*`. The exact double root has one monic
Weierstrass factor

```text
q(z,y)=y^2+c_1(z)y+c_0(z).                         (CBS1)
```

Reduce the Pade numerator modulo `q`:

```text
P_F(z,y)=b(z)+a(z)y mod q.                         (CBS2)
```

Then

```text
ord_z b=2,       ord_z c_0=6,       ord_z c_1>=3,
ord_z a>=0.                                           (CBS3)
```

Its complete regular corank and positive Smith profile are

```text
ord_z a=0:       corank 1,       [4],
ord_z a=1:       [1,3],
ord_z a>=2:      [2,2].                            (CBS4)
```

In particular, the collision cannot have profile `[1,1,2]` or
`[1,1,1,1]`; no regular corank-three or corank-four collision survives.
The entire exact collision is routed by the two successive coefficients

```text
lambda_0=a(0),       lambda_1=[z]a(z).             (CBS5)
```

## Scope

All three valuation ranges of `a` occur in abstract local plane-curve
fixtures with the same contact valuations. The theorem classifies but does
not exclude `[4]`, `[1,3]`, or `[2,2]`; that requires the retained global
source/split-biform geometry. Characteristic two is not covered.
