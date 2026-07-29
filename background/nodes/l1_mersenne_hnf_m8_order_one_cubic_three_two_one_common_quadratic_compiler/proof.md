# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one common-quadratic compiler

The dependency gives a monic cubic `G` on whose roots the monic cubic `F`
takes the values `B,B,lambda B`, with `B!=0` and `lambda!=1`. Exact double
multiplicity says

```text
deg gcd(G,F-B)=2.                                   (1)
```

Let the monic gcd be `Q`. Both cubics in (1) are monic, so their quotients
are monic linear polynomials. This proves (TQC1) for unique `y,z`. If
`y=z`, then `F-B=G` and `F` takes the value `B` on all three roots of `G`,
contrary to `lambda!=1`. Hence `a=y-z` is nonzero. Subtracting the two
factorizations gives `F=G+aQ+B`. At the complementary root `y` of `G`,

```text
lambda B=F(y)=B+aQ(y),                              (2)
```

which proves (TQC2). Exact gcd degree also gives `Q(y)!=0`.

Expanding `G=Q(W)(W-y)` gives (TQC3). Next use

```text
L=FG=G^2+aQG+BG.                                   (3)
```

The coefficients of `QG`, from degree five down to zero, are

```text
1,
u+g_1,
v+ug_1+g_2,
vg_1+ug_2+g_3,
vg_2+ug_3,
vg_3.                                               (4)
```

Combining (3)--(4) with the coefficients of `G^2` proves (TQC4)--(TQC5).
The official characteristics are odd, so the first two equations in (TQC4)
solve for `a,g_2`; the third then solves for `B`, proving (TQC6).

Finally (TQC3) gives

```text
Q(y)=y^2+uy+v=3y^2+2g_1y+g_2,                      (5)
```

and (2) becomes (TQC7). Therefore substitution of the known HNF
coefficients leaves only `(g_1,y,r,d)`, with the three equations (TQC5),
the residual conic, and the fixed role-color equation. Every transformation
is reversible on the listed saturations at the factor-system level, although
the packet remains only necessary for an actual Frobenius/cyclotomic/inner
lift. QED.
