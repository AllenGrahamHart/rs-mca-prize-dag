# Audit

1. The proof uses actual supports to obtain the minimum word and only then
   restores the padded-heavy factor; padded roots are never counted as actual
   error support.
2. Positive `r_delta` is retained. Restricting to clean fibers would lose
   `e-6-d_A` extremal slopes and the corresponding strict slopes.
3. The strict Forney identity is derived from its own minimum word, not
   imported by analogy from the extremal profile.
4. The scalar `chi_delta` is nonzero because a specialization of the
   homogeneous locator is defined only projectively and `delta` is a valid
   supported slope.
5. Agreement on `U_0` is converted to polynomial equality only after checking
   both degree bounds are strictly below `|U_0|`.
6. The theorem proves split fibers, not matrix rank or impossibility.
