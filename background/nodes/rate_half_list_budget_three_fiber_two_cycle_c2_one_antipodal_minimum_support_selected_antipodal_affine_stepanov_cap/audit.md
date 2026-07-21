# Audit

1. The affine determinant is `3`, so characteristic three is the only
   proportionality hazard; official characteristics are much larger.
2. The sparse nonvanishing proof uses the characteristic bound
   `A_0+NB_0<p`, not the stronger convenience assumption `p>=N^2` in the
   earlier F3 corollary.
3. The sparse derivative argument is valid over `F_q`: extending the prime
   field does not change monomial count, degree, or whether integers below
   `p` vanish.
4. The quadratic-field lower bound is taken from `p^2=q>=3*2^128`; using
   `p>=N^2` would incorrectly omit both quadratic chambers.
5. The exact count is at most `355106851`, not `355106852`; the Stepanov
   inequality is strict and the displayed rational quotient is nonintegral.
6. The two choices of `a` are one relabelling orbit, but the same cap would
   hold separately even without that identification.
7. The cap is about `2^28.40`; it is not small enough to justify an
   exhaustive laptop or unpriced Modal run.
