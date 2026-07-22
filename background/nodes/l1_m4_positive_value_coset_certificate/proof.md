# Proof - L1 m=4 positive-valuation value-coset certificate

For `nu>0`, the depressed inner polynomial has `R(0)=0`. A complete fiber
locator is the monic degree-`p` polynomial `R-beta`. Since `p` is odd, the
product of its `p` roots is `beta`. All roots lie in one multiplicative coset
`gamma K`, so every split value lies in `gamma^p K`. Ratios of the three
values therefore lie in the order-`n` subgroup `K`, proving `(VCC1)`.

For any `w in K`, `w^N` lies in `mu_4` and

```text
w^p=w^(N-1)=w^N/w.                                     (1)
```

Raise `1+u+v=0` to the `p`th power and substitute `(VCC2)`:

```text
1+epsilon/u+eta/v=0.                                   (2)
```

Using `v=-1-u` in (2) gives exactly the quadratic in `(VCC3)`.

The checked-in exact verifier works over `F_(p^2)=F_p[i]`, where
`i^2=-1`, and for each `epsilon,eta in {1,-1,i,-i}` reduces the two
`N`th-power equations modulo `q_(epsilon,eta)`. A nonzero linear remainder
is checked at its unique root; a zero remainder certifies both quadratic
roots. The independent audit uses multiplication matrices rather than the
quotient multiplication routine. Both establish the complete table
`(VCC4)`.

For a surviving `(-1,-1)` case, the quadratic is

```text
u^2+u-1=0,       v=-1-u,       uv=-1.
```

Thus the normalized values have sum zero, pairwise-product sum `-2`, and
product `-1`, proving `(VCC5)`. The other two quarter pairs and the two roots
are exactly its remaining ordered permutations. The roots are distinct and
avoid `0,1` and each other because their discriminant and all degeneracy
tests reduce to nonzero factors of one or five.

After scaling the projective triple by `s`, the outer cubic is

```text
Y^3-2s^2Y+s^3.
```

Hence `a=-2s^2`, `b=s^3`, and `a^3+8b^2=0`. This proves `(VCC6)`.
