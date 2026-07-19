# Audit

The span identity is an equality of complete polynomials, not agreement in a
prefix. Checking only the coefficients that determine `beta,gamma` is not a
certificate.

The outer quartic must split into four distinct roots with the printed
fractional-linear matching. A span PASS without that check does not reconstruct
the two original locator relations.

The common scaling of the four subgroup roots preserves every zero and span
condition, so one deleted root may be normalized to one. Permutations are also
redundant. Any computational use must prove coverage of both reductions.

The toy divisor `E=1+z^4` with `d=24` passes the primary and secondary gaps,
but its canonical span residual has a nonzero coefficient `-z^12` after the
uniquely determined `beta=-5/8` and `gamma=205/256` are removed. Thus the span
test is strictly stronger than the two gap tests.
