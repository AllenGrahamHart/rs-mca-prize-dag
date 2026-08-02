# Audit

The campaign rejected several implementation and proof hazards before this
packet was posed:

1. A first Singular-to-SymPy parser mishandled exponent-free variables; its
   reconstruction check failed and the output was discarded.
2. A first coefficient extractor selected only `t^0` terms; again the exact
   reconstruction check failed before any claim.
3. `48` is nonsquare in the deployed field, so the conic has no rational point
   at infinity.  The proof uses the exact affine point `(1,66846712)` instead.
4. Singular factorization and rational-function coefficient fields impose a
   `2^29` characteristic ceiling.  Those presentations are retired.
5. A FLINT `is_zero` method was initially treated as a property.  Every zero
   and exact-division check was corrected to a method call before the sealed
   plane result was produced.
6. Broad lex, direct-family, and target-free bases reached bounded timeouts.
   None is interpreted as unit, nonunit, emptiness, or survival.

Mutation controls alter the discriminant reconstruction, square-free cover,
kernel opposition, and timeout status; each mutation must fail verification.
