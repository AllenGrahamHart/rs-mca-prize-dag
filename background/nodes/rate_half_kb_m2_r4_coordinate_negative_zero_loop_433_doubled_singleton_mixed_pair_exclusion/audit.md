# Audit

1. Cramer numerators and denominators are reduced with their relative
   constants preserved.  They are not monic-normalized separately.
2. The common square factor is checked to be exactly
   `X_den(y^2-1)` before it is removed.
3. All base-field roots of the projected eliminants are reconstructed and
   replayed in the original four determinants and full guard.
4. Lost linear-`c`, product-solve, and singular-q branches are eliminated
   independently in every sign row.
5. The `F_29/F_41` scanner tests the original ranks directly and is used
   only as route reconnaissance, not as the deployed proof.
6. Four separate verifier processes keep each exact replay within the local
   RAM and 60-second policy.
