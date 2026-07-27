# Audit

Date: 2026-07-27.

The proof is analytic and exact. Exhaustive toy enumeration is used only to
exercise the negacyclic coefficient convention; it is not extrapolated to
`h=256`.

The variance-two branch is load-bearing. Four-singleton vectors with `V=2`
already occur at toy dimensions 8, 16, and 32, so replacing `V>0` by `V>=4`
would be false. That branch is paid by the exact primitive-power-of-two
cyclotomic product, not a floating-point estimate.

The logarithmic inequality is certified by its exact derivative factorization
and an exact rational lower bound for `exp(7/5)`. Both final field comparisons
are integer inequalities. No Modal run, resultant census, or probabilistic
claim is load-bearing.

This is a one-profile exclusion. It neither closes the full `s=2` band nor
bounds the number of collision pairs in later bands.
