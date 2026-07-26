# Audit

## Pair-to-gcd translation

The field has odd characteristic and every locator root is nonzero. Thus a
collision under an even quadratic is exactly one antipodal pair. Distinct
pairs have distinct squares; squarefreeness follows from divisibility by
`W^n-1` with `p` odd and `n` a power of two.

The degree-six leading coefficient of `R_s` vanishes only for
`s in {0,1,-1}`. These values are already forbidden by `s notin F_p`, so the
degree assumptions of the subresultant criterion are valid at every claimed
candidate.

## Modular specialization

The primary verifier reduces rational coefficients by numerator times the
modular inverse of the denominator and asserts every denominator is nonzero
modulo 8191. It recomputes the coefficient gcd after reduction; the
characteristic-zero factorization is not used as a proxy for the official
row.

## Independent determinant audit

The audit derives the first-subresultant coefficients as Sylvester minors.
The 160 degree bound is a raw determinant bound, so 161 evaluations prove the
interpolated polynomials exactly over `F_8191`. Its polynomial arithmetic,
determinant elimination, interpolation, and Euclidean gcd are all stdlib and
independent of SymPy.

## Nonclaims

The result closes one color degree only. No assertion is made about cubic or
higher interpolation, order one, inner lifts, or the aggregate L1 payment.
