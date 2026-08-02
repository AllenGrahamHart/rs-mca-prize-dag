# Frontier

Two exact branches remain before cell `14` can close:

1. **Dense curve:** compile the outside ledger in the quotient
   `F_p[r,b]/(F)` without clearing the projective kernel scale into
   degree-45 equations.  A quotient-aware or function-field implementation
   should reduce after each multiplication.
2. **Denominator exception:** specialize the basis-four zero-dimensional
   ideal where the linear `c` coefficient vanishes, compile kernels without
   dividing by that coefficient, and run the finite outside ledger.

Do not launch the existing dense five-variable outside prototype in bulk:
one sampled ideal timed out before its initial standard basis.  The next
implementation must exploit the quadratic relation during equation
construction.
