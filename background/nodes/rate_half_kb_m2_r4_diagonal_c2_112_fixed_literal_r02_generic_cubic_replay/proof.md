# Proof

Build the four literal q-slice rows and reconstruct `w=-U/V`. The resultant
of the first two rows factors, after removing named units, into two cubics and
one degree-12 polynomial. For each cubic, adjoin the two remaining essential
q-slice cores over `F_2130706433`.

Factor 0 gives a dimension-one Groebner basis of size 37. None of the 24
transported localizer factors, nor the first four powers of their product,
reduces to zero, so this computation records the surviving route without
claiming emptiness.

Factor 1 gives a dimension-one basis of size 36. Sequential multiplication
by the square-free transported named factors reduces to zero at factor 15.
Thus the complete named-open intersection with factor 1 is empty over the
base field and every extension. Since the resultant factorization is exact,
factor 0 is the only cubic branch left. QED.
