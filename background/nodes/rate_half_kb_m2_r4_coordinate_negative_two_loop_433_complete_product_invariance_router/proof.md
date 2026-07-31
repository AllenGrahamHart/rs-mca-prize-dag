# Proof

Before choosing representatives, the three singleton edge signs give

```text
{u bD,v cE,w DE,DF,-DF,EF,-EF},       u,v,w in {+/-1}. (1)
```

Replace `D` by `uD` and `E` by `vE`.  The two antipodal product pairs are
unchanged as multisets, while the first two signs become positive and the
third becomes `tau=wuv`.  This proves `(KB43R-1)`.  Replacing `F` by `-F`
simultaneously swaps the two members of both doubled pairs, so either sign
of an `DF` or `EF` `xi` record has the representative in `(KB43R-2)`.
No other product types occur by the complete-edge skeleton theorem.

The outside-product compiler forces the value at `xi`.  Cross-multiplying
its protected denominator gives the last equation in `(KB43R-3)`.  The
other three equations are the exact common-`K` classifier.  This proves
that every complete packet enters one of the 20 indexed cells.

The product involution has homogeneous matrix

```text
J=[ Alpha  Beta ]
  [ Gamma -Alpha],       J^2=(Alpha^2+Gamma Beta) I. (2)
```

Its determinant is nonzero by `(KB43O-4)`.  If the six residual values are
three involution orbits, their root divisor is invariant under `J`.
Pullback of its binary equation is exactly `(KB43R-5)`, hence it differs
from `R` by a nonzero scalar.  This proves necessity of `(KB43R-6)`.

Conversely, proportional binary forms have the same root multiset.  Thus
`J` permutes the six roots of `R`.  Squarefreeness is product distinctness,
and coprimality with `(KB43R-7)` says no root is fixed by `J`.  An involution
without fixed roots on a six-element set has exactly three two-cycles.
Those are precisely the remaining three rows of the paired-product gate.

A binary sextic has seven coefficients.  Projective proportionality of two
nonzero seven-vectors is rank at most one, equivalently the 21 pairwise
`2 x 2` minors.  The independent choices are two common cells, two values
of `tau`, and five `xi` edge types, proving `(KB43R-8)`.

Finally, `M` is an affine coordinate in the independently normalized
source quotient `W`, whereas `D,E,F` are endpoint-root coordinates in `T`.
The common-five statement identifies label indices, not affine values
across these two projective charts.  Hence no equality between
`D,E,F` and powers of `M` is used or available. QED.
