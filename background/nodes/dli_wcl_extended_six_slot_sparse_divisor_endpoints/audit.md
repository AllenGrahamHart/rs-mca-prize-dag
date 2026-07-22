# Audit

1. The signed roots have order `M=2N`; the squared-root divisor uses `N`,
   avoiding the common factor-of-two order error.
2. Newton identities kill exactly the top `ell` coefficients of the locator's
   parity part in characteristic zero or characteristic greater than `w`.
3. Odd weight uses the unique product-one dilation because
   `gcd(w,M)=1`; even weight makes no unsupported product normalization.
4. Divisibility by squarefree `Y^N-1` makes reconstruction denominators
   nonzero and excludes repeated squares, hence antipodal pairs.
5. The recurrence starts at `s=floor(log2(w-1))`, substitutes `V_m=1`, and
   counts only the remaining quotient and intermediate-remainder variables.
6. Characteristic-zero emptiness is proved for the full displayed divisor
   schemes, not inferred from finite samples.
7. The raw affine counts are lower bounds on a blind route, not claims about
   the number of moment-vanishing relations.
8. The theorem creates six finite certificate endpoints but computes no
   integer certificate and closes no target.

