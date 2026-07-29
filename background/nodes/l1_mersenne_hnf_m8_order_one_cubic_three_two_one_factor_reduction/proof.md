# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one factor reduction

Write

```text
E(W)=e_3 e(W),       e_3!=0,
a=alpha/e_3,       b=beta/e_3,       c=gamma/e_3.   (1)
```

The cubic `e-a` has the three reduced roots with color `alpha`. It is monic,
so it is exactly the monic triple-fiber factor

```text
F=e-a.                                                (2)
```

Let `G` be the complementary monic cubic. Squarefreeness and the disjoint
color fibers give `L=FG`.

At the three roots of `G`, equation (2) takes the values

```text
B=b-a=(beta-alpha)/e_3       twice,
C=c-a=(gamma-alpha)/e_3      once.                   (3)
```

Both are nonzero and `C=lambda B`, with `lambda` from (TOF1). Since `G` is
monic, the root formula for the resultant gives

```text
Res_W(G(W),X-F(W))=(X-B)^2(X-lambda B).              (4)
```

Expanding (4) proves (TOF2).

Multiplying all three colors by one eighth root leaves `lambda` unchanged,
so the seven cyclic color-set representatives from the dependency suffice.
For a fixed unordered triple there are three choices for the triple color
and two choices for the double color, hence at most six role assignments and
42 packets in total. Coincident `lambda` values may merge packets but are
not needed for the bound.

The exact multiplicities are encoded by gcd degrees three, two, and one for
`L,E-alpha`, `L,E-beta`, and `L,E-gamma`; standard subresultant saturation
fixes those degrees. The remaining conic and norm-color equations are
inherited necessary conditions. All factors and resultants have degree at
most six in `W`, independent of the official exponent. QED.
