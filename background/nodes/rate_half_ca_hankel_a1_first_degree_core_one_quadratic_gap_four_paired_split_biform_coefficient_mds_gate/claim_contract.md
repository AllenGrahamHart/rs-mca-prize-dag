# Claim contract

- **Claim:** each surviving split profile forces one explicit
  coefficient-barycentric matrix to have a full-support kernel vector.
- **Inputs:** the exact bidegrees and classified split rows from the
  extremal and strict split-biform reductions.
- **Outputs:** matrices `(CMG4)`, dimensions `(CMG7)` and `(CMG9)`, and the
  shared-denominator rational interpolation `(CMG5)`.
- **Falsifier:** a biform satisfying the input profile whose row-leading
  coefficients fail one parity check, or a parity range differing from
  `0<=l<=R-n-2`.
- **Nonclaims:** no rank lower bound, determinant nonvanishing, or boundary
  exclusion is asserted.
