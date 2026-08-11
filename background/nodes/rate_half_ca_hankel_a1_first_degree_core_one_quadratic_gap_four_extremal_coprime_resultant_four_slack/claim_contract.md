# Claim contract

- **Claim:** the nonzero extremal parameter resultant has only
  `4+r_bad` residual degrees after every mandatory classified-row,
  exceptional-row, and selected-padding factor is removed.
- **Inputs:** paired curve coprimality and transversality, the extremal row
  factorizations, the zero-excess padded fibers, and the exact `a/r/b`
  slack ledger.
- **Outputs:** `(CRS3)--(CRS8)` and a single small residual polynomial
  carrying all unclassified intersections and excess multiplicities.
- **Quantifiers:** both extremal `d_A` profiles on the official row.
- **Falsifier:** a missing mandatory resultant factor, a zero resultant, or
  residual degree greater than `4+r_bad`.
