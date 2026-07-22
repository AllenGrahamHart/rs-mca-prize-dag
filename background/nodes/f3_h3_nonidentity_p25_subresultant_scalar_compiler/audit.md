# Audit

1. `G_n(T,X)=X^(n-1)F_n(T/X)` is polynomial. Its leading `X` coefficient is
   `-n`, a unit only because the coefficient ring inverts two.
2. Product multiplicity equals gcd degree because the first shifted factor
   determines the second; no unordered factor of two appears in `(PSC5)`.
3. All coefficients of every polynomial subresultant `S_0,...,S_24` are
   generators. Keeping only a convenient coefficient requires a separate
   nondefect theorem.
4. The cutoff is indices `0` through `24`: their vanishing means gcd degree
   at least 25.
5. The selector `(T-1)Y-1` is load-bearing because DSP8 excludes the
   potentially rich identity fiber.
6. The scalar support is exact, unlike the unordered cutoff-12 outer support;
   it has no `U=13,D=2` overcandidate.
7. Sparse degree-`n-1` input does not imply a small output. `S_0` is the
   degree-`(n-1)^2` global product resultant.
