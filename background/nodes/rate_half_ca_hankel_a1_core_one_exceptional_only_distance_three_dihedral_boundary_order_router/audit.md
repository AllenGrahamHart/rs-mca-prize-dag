# Audit

- The power `a^(8e+8)` in the constant-product calculation is exactly
  `a^N=1`; losing the final `+8` would invalidate the cancellation.
- The degree-14 map includes two simple boundary roots and three roots of
  multiplicity four.
- Nonconstancy is proved on the antipodal branch. A possible constant map on
  the inversion branch first gives the exact divisor symmetry `(DBO4)` and
  is then excluded by the triple gate `(DBO6)`.
- Disjointness of the simple and multiplicity-four boundary roots rules out
  the two-fixed-point orbit for `{s,x_0}` and yields the exact normal form
  `(DBO5)`.
- The factorization of `e` makes the cofactor argument exact: only cofactors
  `1` and `3` are at most 14.
- The verifier checks the arithmetic, the reciprocal derivative exponents,
  impossibility of an odd nonzero negation-stable triple, and an
  inversion-symmetric five-point divisor control over `F_17`. It then
  correctly rejects that control at the triple boundary-power gate.
