# Proof

The deployed common saturation gives dimension one and basis size 23.  Exact
elimination was run in four variable orders.  In order `(c,r,b,t)`, the
projected lex basis has size seven.  Its first polynomial is the 25-term
bidegree-`(4,4)` eliminant `P`.  The coefficients of `b^4,b^3,b^2,b,1` show
that `P` is palindromic.  Dividing by `b^2` and substituting
`x=b+b^{-1}` reconstructs the recorded quadratic `Q(x,t)` exactly.

The quadratic discriminant factors as `(KBC3-1)`.  Removing the square

```text
(t+16711679)^2(t-16711679)^4
```

leaves a conic.  Direct substitution verifies its point
`(1,66846712)`.  Lines through that point give the sealed rational functions
`t(s),Y(s),x(s)`.  Substitution verifies `Q(x(s),t(s))=0`.  The remaining
quadratic `b^2-x(s)b+1` has discriminant `x(s)^2-4`.  Its denominator factors
as

```text
1593843777 (s+66846724)^2
 (s^3-200540148s^2-8388527s+1035993540)^2,
```

while its numerator is the nonzero scalar `1728845849` times `(KBC3-3)`.
The factorization packet gives multiplicity one to five linear factors and
one irreducible cubic.  Thus the numerator is square-free of degree eight.
In odd characteristic, the smooth projective normalization of
`y^2=R_8(s)` has genus `(8-2)/2=3`.  The transformations have rational
inverses away from their printed denominators, proving the claimed
birational model on the open chart.

For the kernel statement, reduce the eight primitive common coefficients by
the seven-element lex basis.  Exact reduction gives `b11=-b10`.  The two lex
equations linear in `r,c` give rational functions with a common denominator
scale of `t`-degree 48.  FLINT arithmetic over the deployed field clears this
scale.  The eight cleared polynomials have a common `t`-factor of degree 12,
which is divided exactly.

Write the plane eliminant as

```text
P(b,t)=A_4(t)b^4+A_3(t)b^3+...+A_0(t).
```

For each coefficient `K`, repeated pseudo-division replaces its leading
`L(t)b^m` by

```text
A_4(t)K-L(t)b^(m-4)P.
```

Each step lowers the `b`-degree.  Sixteen common powers of `A_4` align all
eight reductions.  Their second common factor, of `t`-degree 84, divides
exactly.  The resulting coefficient shapes are bounded by `(3,22)`, and the
exact `B_1` opposition remains.  This proves `(KBC3-4)` and the compact kernel
model on the stated open chart.

Finally, FLINT compiles the four necessary target-free family equations and
pseudo-reduces them by `P`.  The subsequent Singular computation times out;
the packet records only the exact equations and their shapes.  No emptiness
claim is inferred.  QED.
