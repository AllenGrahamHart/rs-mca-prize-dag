# Proof

Exact lex conversion in the order `(c,r,b,t)` gives seven polynomials.  The
first is the recorded 21-term bidegree-`(4,4)` eliminant.  Its coefficients of
`b^4,b^3,b^2,b,1` show that it is palindromic.  Dividing by `b^2`, setting
`x=b+b^{-1}`, and reconstructing verifies the quotient quadratic exactly.
Its discriminant factors as `(KBC4-1)`.

Remove the square `(t-16711679)(t+16711679)^2`.  Direct substitution verifies
the point `(1,66846712)` on the remaining conic.  A line of slope `s` through
that point gives the sealed rational functions `t(s),Y(s),x(s)`.  Substitution
verifies both the conic and quotient equations.  The discriminant of
`b^2-x(s)b+1` has numerator `(KBC4-2)` and a denominator which factors as four
distinct linear squares.  The numerator factorization gives one linear
factor, the square `(s+4)^2`, and one irreducible cubic.  After removing the
square, the branch polynomial is square-free of degree four.  In odd
characteristic, the normalization of `y^2=R_4(s)` has genus one.

For the kernel, reduce the eight primitive common coefficients by the same
seven-element lex basis.  Exact reduction gives `b11=-b10`.  The basis has one
equation linear in `r` and one equation linear in `c` after substituting `r`.
FLINT substitutes these rational functions, clears the common denominator of
`t`-degree 45, and divides the exact common projective factor of degree 20.

Write the leading coefficient of `P` in `b` as `(t^2+1)^2`.  Repeated
pseudo-division lowers every kernel coefficient to `b`-degree at most three.
Nine aligned leading-coefficient powers suffice.  Their projected common
factor has `t`-degree 49 and divides all eight aligned polynomials exactly.
The normalized coefficients then have `t`-degree at most eighteen and retain
`b11=-b10`, proving `(KBC4-3)`.

Finally, FLINT compiles and pseudo-reduces the four necessary target-free
family equations.  Their shapes and hashes are sealed.  The subsequent
Singular standard basis times out at the stated bound, so no emptiness or
survival conclusion is inferred.  QED.
