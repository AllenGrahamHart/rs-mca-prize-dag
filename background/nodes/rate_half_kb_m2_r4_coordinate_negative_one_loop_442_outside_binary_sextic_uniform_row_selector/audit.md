# Audit

1. The norm is a determinant of multiplication by the coefficient minor,
   so nonvanishing proves that the minor is a unit, not merely nonzero at one
   quotient point.
2. The primary verifier checks the representative sign row; the audit
   verifier independently rebuilds the other three quotient rows.
3. Coefficient rows and columns are zero-indexed and both equal `(0,1,2)`.
4. The rank-three conclusion is imported from the characteristic-independent
   eigenvalue compiler; the unit-minor calculation is deployed-field exact.
