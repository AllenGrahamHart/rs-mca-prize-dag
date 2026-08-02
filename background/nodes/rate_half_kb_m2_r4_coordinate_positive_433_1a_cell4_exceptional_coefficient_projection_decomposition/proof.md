# Proof

The resultant in `(KBC4EC-1)` is homogeneous of degree four in the three
coefficient vectors `L,M,F`, hence has total degree at most four in `(s,u)`.
The recorded 15-by-15 evaluation matrix is invertible.  Therefore its fifteen
values vanish simultaneously exactly when the resultant is the zero
polynomial in `(s,u)`.  Since the plane has degree four on the guarded chart,
the product formula for resultants then forces a plane root common to `L,M,F`
over the algebraic closure.

FLINT computes all fifteen resultants, their exact common gcd, and reconstructs
the seven irreducible factors in `(KBC4EC-2)`.  The linear factors have only
the four original guard roots, the two cubic factors have no deployed roots,
and the remaining factor is the irreducible `H` with multiplicity two.

Exact division by the common gcd gives fifteen primitive bivariate
polynomials.  Singular appends them sequentially: the zero-dimensional degree
drops `528,472,472,471,471,471,470` and then remains `470`.  FGLM gives a
17-element lex basis and the degree-105 eliminant `(KBC4EC-3)`.  FLINT
reconstructs its complete factorization.  Every linear root is an original
guard zero and the cubic is irreducible, proving that the primitive residual
has no admissible base-field point.

Finally, pseudo-Euclidean division in `b`, with coefficient reduction modulo
`H` after every operation, first gives a quadratic remainder and then the
linear polynomial `(KBC4EC-4)`.  After exact removal of its common univariate
content, division of each of `P,L,M,F` by this linear polynomial has zero
remainder in the `H` quotient.  This proves the generic lift statement, with
all leading-scale exceptions retained.  QED.
