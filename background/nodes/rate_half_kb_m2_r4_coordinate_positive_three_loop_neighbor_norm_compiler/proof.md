# Proof

Fix a nonzero target `r` and set

```text
F_r(X)=H(r,X)=r^2D(X^2)+E(X^2)+rX B(X^2).          (1)
```

Its four roots, counted on the source divisor, are the four source points
whose component edge is incident to `r`.  If `t` is the other target root
at one of them, Vieta gives

```text
t=E(X^2)/(rD(X^2)).                                (2)
```

The complete-fiber leading-support condition makes every denominator in
(2) nonzero.

For a root `W` of `E`, multiply (1) at the two source lifts `X` and `-X`:

```text
F_r(X)F_r(-X)=r^2[r^2D(W)^2-WB(W)^2].              (3)
```

Taking resultants first over the two lifts and then over the two roots of
`E` gives

```text
Res_X(F_r,E(X^2))=r^4 Res_W(E,r^2D^2-WB^2).        (4)
```

The same calculation at a root of `D` gives

```text
Res_X(F_r,D(X^2))=Res_W(D,E^2-r^2WB^2).            (5)
```

The ratio of the left sides of (4) and (5), divided by `r^4`, is exactly
the product of (2) over the four roots of `F_r`.  Equations (4)--(5) prove
`(KBP3N-2)--(KBP3N-3)`.  Since `D,E` have degree two, each right-hand
resultant is the product of two affine-linear expressions in `U=r^2`, so
its `U`-degree is at most two.  The polynomial identities also retain a
source point at infinity by homogeneous specialization.

It remains to compute the target-neighbor products.  Every common loop
contributes the antipodal edge twice.  Each nonloop signed edge orbit
`(u,epsilon v)` contributes the two edges

```text
(u,epsilon v),       (-u,-epsilon v).              (6)
```

Insert the two common nonloop orbits for each placement and the seven
outside orbits

```text
a e, a' f, de,-de,df,-df,sigma ef.                 (7)
```

Every one of the twelve signed targets then has degree four.  Multiplying
the four neighbors of the positive representative gives exactly the four
tables in `(KBP3N-4)`.  Solving their colored rows gives
`(KBP3N-5)--(KBP3N-7)`.  The checker independently rebuilds all 24 edge
occurrences in each of the eight lanes and verifies every product. QED.
