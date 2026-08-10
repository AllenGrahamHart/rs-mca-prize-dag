# Proof: general t-petal saturated-slice dimension

The ambient pair space in `(SD2)` has dimension `2d+2`. Divisibility by the
pairwise coprime product `Lambda` imposes at most `h` linear conditions, so

```text
dim V>=2d+2-h=e+1.                                    (1)
```

Fix the saturated anchor `(F,W)` and define

```text
Phi: V -> K[X],       Phi(G,B)=(FB-GW)/Lambda.        (2)
```

For every `i`, both pairs obey the same labelled congruence modulo `L_i`, so
`L_i` divides `FB-GW`. Pairwise coprimality makes `(2)` a well-defined linear
map. Its image has degree at most

```text
2d-h=e-1,
```

and therefore lies in an `e`-dimensional polynomial space, interpreted as
the zero space when `e=0`.

If `(G,B)` lies in the kernel, then `FB=GW`. Since `gcd(F,W)=1`, one has
`F|G`. The degree bounds and `deg F=d` force `G=lambda F` for a scalar
`lambda`, after which `B=lambda W`. Conversely every scalar multiple of the
anchor is in the kernel. Thus

```text
ker Phi=K(F,W),       dim ker Phi=1.                  (3)
```

Rank-nullity gives `dim V<=e+1`, which with `(1)` proves `(SD4)`.

For `(SD5)`, suppose `(0,B)` lies in `V`. Then every `L_i` divides `B`, so
`Lambda|B`. But `deg B<=d<h`, hence `B=0`. Locator projection is injective
and is an isomorphism onto its image. The anchor makes the leading-coefficient
functional nonzero on `V_F`; setting it equal to one produces a nonempty
affine hyperplane of dimension `e`.

Finally, if `x` is simultaneously a petal root and a root of a primitive
member's locator, its labelled congruence forces the numerator to vanish at
`x`, contradicting primitivity. This proves the automatic disjointness claim
and completes the proof. QED.
