# Proof

Use the fixed-moving reconstruction with `a=2`, `xi=b`, `(eta,ell)=(c,d)`,
and `w=1/c`. The residual over each of `c,d` has roots `1/b,1/d`. Removing
the finite-incidence factor `H^2` from each product condition gives the four
primitive polynomials with digests

```text
c product 5117a5676cc0bdb9    c sum b052e13bbf0f28fe
d product 70cb7c16ac2f1e3e    d sum 0ed07280609cd604.       (1)
```

Eliminating `b` within each q-root and factoring over `QQ` leaves low/high
components

```text
c: bed4496a0af11b8c, 842d5d9a084f107e,
d: 8d63799ea7b1c3fc, 39ad8e659560b1b1,                 (2)
```

of bidegrees `(3,2)` and `(16,14)`. Every other factor is one of
`c,d=0,+/-1,2,1/2`, `cd=1`, or `5cd-4c-4d+5=0`, with the multiplicities
pinned by the parent-resultant shards.

For low/low, the terminal projection is degree 12 and factors as

```text
(d-2)(2d-1)(19d-17)(d-1)^3(d+1)^3
(2d^3-19d^2+19d-14).                                  (3)
```

The two nonstandard fibers are classified directly. Modulo
`p=2130706433`, the cubic splits into one linear and one quadratic factor.
The linear branches leave `b=c=1`; the quadratic branch has four
`F_(p^6)` c-roots and only `b=0`, `b=1`, or `b=1/2`, with reciprocal,
collision, or `z=1` labels.

The low/high and high/low projections have degree 74. After their four
standard linear factors are removed, their degree-40 factors have digests
`995db6566e31698c` and `e364442d07376273`. Their modular irreducible degrees
are

```text
[1,2,2,4,4,27],             [1,1,6,32].                (4)
```

Thus only the first three factors in each list can meet `F_(p^6)`. Exact
lex bases and Frobenius gcds classify all six fibers as forbidden.

For high/high, a common point lies on the cross-product resultant. Its only
nonstandard components are `c^2d-2` and the bidegree `(11,8)` factor with
digest `9274da18c1badf2f`. Projecting the high `c` component against these
two factors modulo `p` gives degrees 44 and 282 and digests
`6970b9ab5bbc89f6`, `883a93b7debea09a`. Their complete factor censuses are
those printed in the statement. After deleting standard linear support and
degrees not dividing six, exactly three linear, five quadratic, two cubic,
and one sextic nonstandard factors remain. Each is empty or every point is
forbidden.

The primary reconstructs the source by direct matrix inversion, uses
resultants, and classifies each field fiber with explicit tuple arithmetic.
The audit reconstructs the source with `DomainMatrix.solve_den`, uses
terminal subresultants for all characteristic-zero routers and modular
subresultants for high/high, then specializes all four original equations
in an independently written residue-field engine. It computes both
`gcd(F,X^(p^6)-X)` and the base-field gcd, checks equality, splits every
linear factor, and requires a forbidden label for every `(b,c,d)`. Hence
no admissible deployed-field point remains. QED.
