# Proof: general t-petal anchor determinant coordinate

The dimension theorem shows that `M` is a nonempty affine space of dimension
`e`, while `K[X]_(<=e-1)` has dimension `e`. The cross-determinant quotient
in `(AC1)` is well defined and affine linear on `M`, and it sends `(F,W)` to
zero.

Suppose two points of `M` have the same `H`. Their difference `(G_0,B_0)`
lies in the kernel of the linear cross-determinant map. The kernel theorem
gives

```text
(G_0,B_0)=lambda(F,W)
```

for a scalar `lambda`. The two locator coordinates are monic of degree `d`,
so their difference has zero degree-`d` coefficient. Since `F` is monic,
this forces `lambda=0`. Thus `(AC2)` is injective. Equal affine dimensions
make it bijective.

Now assume `F` is squarefree and let `x` be one of its roots. Primitivity of
the anchor gives `W(x)!=0`. Automatic petal disjointness gives
`Lambda(x)!=0`. Evaluating

```text
FB-GW=Lambda H
```

at `x` yields

```text
-G(x)W(x)=Lambda(x)H(x).
```

Therefore `H(x)=0` if and only if `G(x)=0`. The two polynomials have exactly
the same roots on the squarefree locator `F`, proving the monic gcd identity
in `(AC3)`. Bijection shows that `H=0` occurs only at the anchor, and the
degree bound gives the overlap cap. QED.
