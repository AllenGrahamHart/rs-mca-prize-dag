# Audit - L1 Pade-remainder Jacobian dichotomy

## Checked axes

1. Locator variations have degree below `a`; monicity is fixed.
2. The quotient and remainder are both varied in the differential identity.
3. Reduction modulo `L` determines the unique degree-below-`a` remainder.
4. Multiplication by `Q` is invertible exactly on `gcd(L,Q)=1`.
5. Full remainder rank `a` is projected to, not confused with, Pade rank `w`.
6. The Jacobian conclusion is local smooth codimension, not global
   irreducibility.
7. Rank failure implies tangency; tangency is not asserted to imply failure.
8. Exactness uses the separate complement guard `gcd(Q,Omega/L)=1`.
9. The tangent gcd roots lie in the agreement support.
10. The sharpness witness is exact and has projected rank strictly below `w`.

## Route effect

The all-cofactor Pade target now has no primitive rank-collapse branch.
Potential excess on exact shells separates into a canonical tangent resultant
owner and global concentration of split points on a smooth codimension-`w`
section.  This aligns directly with upstream's tangent/common-factor versus
primitive-Q bookkeeping.
