# Audit

1. The degree bound is strict: both numerator and denominator have degree
   below `r=n-s`.
2. Common zeros of `P,Q` are allowed. The matrix criterion is projective and
   does not require pointwise division by a nonzero denominator.
3. In the deficient branch, only the unique point carrying the lower clone is
   punctured; all other support points remain constrained.
4. The lower-clone coefficient must be nonzero. For the bivariate `j=m`
   block it is the leading coefficient of `L_xA_x` and is nonzero after the
   parameter normalization.
5. Replacing `h` by `h+c` preserves the criterion by replacing `Q` with
   `Q+cP`.
6. The primary verifier compares matrix rank with the rank of the polynomial
   interpolation system over many deterministic data sets. The audit checks
   explicit rational and nonrational examples in both unpunctured and
   punctured forms. The bounded Modal result has a separate deterministic
   aggregate verifier.
