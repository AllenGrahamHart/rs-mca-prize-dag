# Proof

For a monic cubic, the constant coefficient is the negative product of its
roots. The adapter's equal-constant decoration therefore gives

```text
RUV=SXY=RS.                                          (1)
```

Its `lambda X` difference says the `X^2` coefficients agree, which is the
equal-sum identity in `(UTN2)`.

Since `gcd(3,n)=1`, the map `h -> h^3` permutes `H`, so `q` in `(UTN3)`
exists uniquely. Divide `(1)` by `q^3` to get

```text
ruv=sxy=1.                                          (2)
```

On the other hand `R=q r` and `S=q s`, so `q^3=RS=q^2rs`. Cancellation
gives `q=rs`. Dividing the equal-sum identity by `q` gives the common trace
`sigma`, proving `(UTN4)`.

Conversely, start from the normalized data in the statement and put
`q=rs`. Scaling both triples by `q` preserves their equal sums. Their
products become `q^3`, while the product of the distinguished scaled roots
is

```text
(qr)(qs)=q^2rs=q^3.                                 (3)
```

Thus the two monic cubics have equal `X^2` and constant coefficients and
differ only in the `X` coefficient. If that coefficient also agreed, the
cubics and their root multisets would be equal, contradicting reduced
disjointness. Their difference is therefore a nonzero multiple of `X`, and
the adapter's converse reconstructs the decorated primitive shift pair.
The two constructions are inverse because the cube root and the scale in
`(3)` are unique.

The original representation attached to `B` has roots `qx,qy`. Using
`xy=1/s`, `x+y=sigma-s`, and `q=rs`, its shifted product is

```text
(1-qx)(1-qy)
 =1-q(sigma-s)+q^2/s
 =1-rs sigma+rs^2+r^2s
 =1+rs(r+s-sigma).                                  (4)
```

The representation attached to `A` gives the same expression from
`uv=1/r` and `u+v=sigma-r`. Replacing `v` by `(ru)^(-1)` and `y` by
`(sx)^(-1)` gives the two factorizations in `(UTN5)`.

Finally, sum and product determine each residual unordered pair. The pair
`{u,v}` has sum `sigma-r` and product `r^(-1)`, and `{x,y}` has sum
`sigma-s` and product `s^(-1)`, proving `(UTN6)`. The forced scaling preserves
the signed-coordinate distinctness. Adding the retained-target predicates and
one ordered quotient representation gives exactly `(UTN7)--(UTN8)` and no
extra multiplicity. QED.
