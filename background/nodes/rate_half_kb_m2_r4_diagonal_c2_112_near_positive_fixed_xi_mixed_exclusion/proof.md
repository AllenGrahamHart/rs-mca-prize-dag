# Proof

Use the positive fixed-moving reconstruction supplied by the parent nodes.
At a root `r` of `q=(T-c)(T-d)`, divide

```text
U(r,W)^2-W V(r,W)^2
```

by the forced `(W-w)^2`, and write the residual as
`A_r W^2+B_r W+C_r`. The mixed allocation `(KBNMX-1)` is equivalent, for
both `r=c,d`, to

```text
C_r-A_r/(2d)=0,
B_r+(1/2+1/d)A_r=0.                              (1)
```

The direct checker verifies the exact reconstruction determinant and both
forced roots before forming `(1)`. After removing the finite-chart factor
`H^2` from each product equation, all four equations are primitive
quadratics in `b`. Their `(deg_b,deg_c,deg_d)` values are

```text
product: (2,6,5),       sum: (2,10,7)             (2)
```

at both roots.

Eliminate `b` between the product and sum equations over the `c`-fiber. Its
resultant is a product of explicit forbidden factors and one irreducible
residual curve `R` of bidegree `(8,6)`. The corresponding `d`-fiber
resultant has the same `R`. A simultaneous solution must therefore lie on
`R` after the forbidden components are removed.

Next eliminate `b` between the two product equations. Apart from
`2d-1`, `c-d`, `c-1`, `cd-1`, and the excluded `z=1` factor, this resultant
has exactly two factors of bidegrees `(2,1)` and `(6,5)`. Eliminate `b`
between the two sum equations. Apart from `c-d`, `c-1`, `cd-1`, the `z=1`
factor, and the finite-chart boundary `H`, it has exactly three factors of
bidegrees `(1,1)`, `(4,3)`, and `(10,8)`.

A retained solution lies on `R`, one of the two product factors, and one of
the three sum factors. Eliminate `c` between `R` and each product factor and
multiply the two univariate certificates, obtaining degree 96. Do the same
for the three sum factors, obtaining degree 186. Their squarefree gcd is
exactly `(KBNMX-2)`. Each root is forbidden, so no finite characteristic-zero
solution is admissible.

The primary clears denominators and repeats the univariate gcd modulo the
deployed characteristic. The independent audit obtains the source
coefficients with `DomainMatrix.solve_den`, verifies the fraction-free matrix
identity, and instead eliminates `d`. Its degree-96 and degree-186
projections have squarefree gcd

```text
(c-2)(c-1)(2c-1),
```

also in characteristic `2130706433`. Resultants are used only in their
necessary direction, so no leading specialization is discarded. Every
remaining projected root is forbidden. QED.
