# Proof

Push the tensor ideal sequence used in the multiplication reduction along
`pi`. Both ambient line bundles have negative parameter degree, so their
zeroth direct images vanish. Since `pi|_C` is finite, its higher direct image
vanishes. The resulting exact sequence identifies the kernel of the relative
multiplication map with

```text
pi_*O_C(N,-T).
```

The Picard pin `O_C(N,-T)=O_C(P_*)` proves `(KED1)`.

Next push the untwisted ideal sequence

```text
0 -> O(-rho,-m) -> O -> O_C -> 0.                   (1)
```

For `m>1`, the first term has zero direct image and

```text
R^1 pi_*O(-rho,-m)=O(-rho)^(m-1).
```

Thus

```text
0 -> O -> pi_*O_C -> O(-rho)^(m-1) -> 0.            (2)
```

The extension splits because

```text
Ext^1(O(-rho),O)=H^1(P^1,O(rho))=0.
```

This proves `(KED2)`.

The effective degree-one divisor `P_*` is Cartier by the line-bundle
identity. Hence

```text
0 -> O_C -> O_C(P_*) -> k_(P_*) -> 0.               (3)
```

is exact. Finite pushforward is exact and sends the final term to
`k_(x_0)`. Combining `(3)` with `(KED1)--(KED2)` proves `(KED3)`.

A locally free positive elementary modification of

```text
E=O direct_sum O(-rho)^(m-1)
```

at one point is represented by a nonzero vector in the fibre `E|_(x_0)`, up
to automorphisms of `E`. If its projection to the negative block is zero,
the modification raises the `O` summand and gives `(KED4a)`. If that
projection is nonzero, a constant automorphism of the equal negative
summands sends it to the first coordinate. Maps
`O(-rho)->O` have arbitrary prescribed value at `x_0`, so the remaining
`O`-component can be removed. The modification then raises one negative
summand and gives `(KED4b)`. These are distinct and exhaust all nonzero
vectors, proving the dichotomy.

Since `rho=4m-1>=7`, all displayed negative summands have no sections.
Equations `(KED5)` follow.

Finally, in `(KED4a)` the Picard identity gives
`h^0(C,O_C(P_*))=2`. A degree-one line bundle with two independent sections
has no base point: a common degree-one fixed divisor would leave a
degree-zero line bundle with two sections. The resulting morphism to `P^1`
has degree one. It is finite and birational, and the normality of `P^1`
forces the integral source to be `P^1`. QED.
