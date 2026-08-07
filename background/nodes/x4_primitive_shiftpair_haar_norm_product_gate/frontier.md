# Frontier

For every consumed row and residual `(e,d)` cell:

1. set `T=e-d-1`;
2. enumerate only the possible zero/nonzero fold patterns, with scale zero
   active;
3. delete every pattern failing `(HP-3)` using the row characteristic and
   exact Frobenius orbit counts;
4. seek a structural classification of the surviving zero-fold patterns or
   a first-owner-compatible count of the fully active residue.

Do not replace a zero higher fold by a norm factor without a separate
divisibility theorem.
