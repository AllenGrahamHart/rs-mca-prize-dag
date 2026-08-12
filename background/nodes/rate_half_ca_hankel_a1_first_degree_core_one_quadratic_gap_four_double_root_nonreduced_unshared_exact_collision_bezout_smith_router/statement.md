# `A=1` quadratic nonreduced exact-collision Bezout/Smith router

- **status:** PROVED
- **closure:** exact corank two and one-scalar Smith dichotomy
- **consumer:** `rate_half_band_crossing_location`

Retain the nonzero-jet alternative of the normalization/collision
dichotomy. Complete at `tau`, put `z=t-tau`, and write `y=X-x_*`. The
exact double root has one monic Weierstrass factor

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
ord_z a>=1.                                           (CBS3)
```

The regular specialized Hankel corank is exactly two. Its complete
positive Smith profile is

```text
ord_z a=1:       [1,3],
ord_z a>=2:      [2,2].                            (CBS4)
```

In particular, the collision cannot have profile `[1,1,2]` or
`[1,1,1,1]`; no regular corank-three or corank-four collision survives.
The entire exact collision is routed by the single first-order scalar

```text
lambda_1=[z]a(z).                                  (CBS5)
```

## Scope

Both values of `lambda_1` occur in abstract local plane-curve fixtures
with the same contact valuations. The theorem classifies but does not
exclude `[1,3]` or `[2,2]`; that requires the retained global
source/split-biform geometry.
