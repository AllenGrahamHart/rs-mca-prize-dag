# Audit - L1 marked constant-shift extremal kernel normal form

## Checked axes

1. Rank at most `2m` still uses exact saturation; it is false for arbitrary
   coefficient data with a large common factor.
2. At exactly `2m` labels, every kernel-pair determinant is a scalar multiple
   of `Q`, not necessarily zero.
3. A third kernel direction is excluded both when all determinants vanish and
   when one determinant is nonzero.
4. The actual coefficient vectors must span the full two-dimensional kernel;
   a one-dimensional span would again violate the exact gcd degree.
5. The adjugate identity retains the complete `Q(P)` factor and both
   coefficient polynomials.
6. The sharp family uses a transcendental parameter only to certify that a
   nonempty Zariski-open set of saturated choices exists; finite specializations
   require the same nonzero-resultant guard.

## Remaining attack

Price determinant-`Q` matrices by an existing quotient/profile owner, prove
a bounded first-match count for them, or derive corresponding normal forms
for `T<2m`.
