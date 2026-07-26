# Audit

The upstream proof was reconstructed from the statement rather than copied.
The audit checks the two load-bearing points:

1. the common-zero bound is `z<=K-s`, not merely `z<K`;
2. the ratio step is the exact nonnegative identity `(3)`, so no asymptotic
   or field-size hypothesis is hidden.

The generalized-weight count uses independent normal bases. It does not
count arbitrary hyperplane tuples, and each independent basis has at most
one affine intersection point. The focused verifier checks the binomial
identity and the ratio identity over a bounded parameter census. The audit
verifier exhausts all affine flats in a small RS code.
