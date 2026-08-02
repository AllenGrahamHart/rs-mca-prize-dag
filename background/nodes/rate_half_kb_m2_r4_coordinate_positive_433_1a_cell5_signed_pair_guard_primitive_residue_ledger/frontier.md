# Frontier

Work factor by factor in the five fields `K[s]/(phi_j)`:

1. express `b,x0,x1` or only the needed source and colored invariants as
   polynomials in `s`;
2. compute norms of source-square, nonzero, collision, and chart denominators;
3. isolate the finite exceptional-`t` locus from those norms and the primitive
   discriminant;
4. append the residual colored `BE` cubic and unsquared sum in each field;
5. return a unit gcd/norm or an exact surviving residue factor.

Do not recompute the pair basis, radical, primitive polynomial, or factor
ledger.  The next useful computation is the invariant-coordinate map or a
colored norm in these five low-degree fields.
