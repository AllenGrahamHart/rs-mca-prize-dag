# Audit

1. The sign in `(PG1)` is pinned to the orientation
   `b_ij+b_jk=b_ik` inherited after locator cancellation; all four toy
   triangles detect a sign mutation.
2. The Plucker identity is derived in the polynomial ring before passing to
   `F(X)` for the rank-two interpretation.
3. No division by `b_01` is needed in `(PG2)` or `(PG3)`; these are polynomial
   identities even when `b_01` has roots.
4. `R` contains only selected singleton, full, and pair-only coordinates. Its
   degree bound is the exact maximum over the six incidence rows.
5. The independent audit reconstructs the order-eight witness from codeword
   evaluations, checks `(PG1)--(PG3)`, all six minors, and rejects mutations
   of the Plucker sign and one edge coefficient.
