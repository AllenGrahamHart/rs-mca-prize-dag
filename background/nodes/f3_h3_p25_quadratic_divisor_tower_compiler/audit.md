# Audit

1. Both scalar selectors are required. `T=0` makes the second torsion element
   identically one; `T=1` is outside DSP8.
2. `XZ=1 mod Q` is load-bearing. Without it, `(X-T)/X` is undefined and a
   root at zero can enter.
3. No separate discriminant selector is needed: `(1-X)^n-1` is squarefree
   at `p=1 mod n`, so any monic divisor `Q` is squarefree.
4. The degree is exactly 25, not at most 25. A fiber with more records permits
   selection of any 25 distinct first coordinates.
5. Quotient polynomials are part of the certificate but not counted as
   product representations. Omitting them turns congruence into an
   unevaluable assertion.
6. Characteristic-zero emptiness gives only a finite bad-characteristic outer
   set from a checked integer certificate. It does not say every divisor of
   that certificate supports a fiber.
7. Four thousand quadratic variables can still be computationally
   prohibitive. The size reduction is not a cost estimate.
