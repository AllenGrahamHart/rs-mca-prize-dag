# Proof

The parent theorem leaves forty zero-dimensional localized ideals, one for
each root-sign row of ten matching cells.  FGLM converts each certified
degrevlex standard basis to a reduced lexicographic basis without changing
the quotient algebra or zero set.

The generated bases all have exactly five members and the displayed shape
`(KBP1BRF-1)`.  Therefore the projection to the `b` coordinate is injective
on geometric points and its image is exactly the root set of `g`.  A point
is rational over the deployed field if and only if its `b` coordinate is a
linear factor root: the other four coordinates are then polynomial values
in that root.

Exact modular factorization gives `(KBP1BRF-2)`.  Thirty-two rows have no
linear factor and hence no rational point.  Each of the other eight has two
distinct linear factors and therefore exactly two rational points.  The
certificate evaluates the four shape polynomials at those roots and records
all sixteen coordinate tuples.

The independent verifier rebuilds each product and full common Vieta matrix
directly from its cell, root signs, and recorded coordinates.  Gaussian
elimination gives ranks four and seven, respectively.  Direct multiplication
also gives `zH=1`, so none of the reconstructed points lies on a stripped
guard.  This proves both exhaustiveness and admissibility at the common
localized level. QED.
