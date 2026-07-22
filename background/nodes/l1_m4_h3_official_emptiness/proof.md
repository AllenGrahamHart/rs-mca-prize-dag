# Proof - L1 official m=4, h=3 split-pencil emptiness

The Mason and Cartier suppliers put every hypothetical record in a depressed
factorization

```text
(R^3+aR+b)D=X^(4(p+1))-alpha,
a!=0,       nu=ord_0(R) in {0,1,2,3},
0<=deg H<=3-nu.                                       (1)
```

This is an exhaustive valuation split.

If `nu>0`, the tangent-radical theorem reduces all possibilities to
`(nu,deg H)=(1,2),(2,1)`. The positive tangent multiplicity exclusion proves
both impossible on every official characteristic.

It remains to take `nu=0` and split on `b`.

If `b=0`, the value-coset and Euler exclusion proves the complete branch
empty: the first two characteristics have no packet, while either remaining
packet would force characteristic five.

Suppose `b!=0`. Tangent localization excludes `deg H=1,2`. At `deg H=0`,
the projective packet chain and auxiliary-fiber exclusion remove the
universal packet and the sole exceptional largest-characteristic packet. At
`deg H=3`, the tangent multiplicity exclusion would force `p<=9`. Thus both
remaining degrees are impossible.

Every case in (1) has been exhausted, proving official `m=4,h=3` emptiness.
