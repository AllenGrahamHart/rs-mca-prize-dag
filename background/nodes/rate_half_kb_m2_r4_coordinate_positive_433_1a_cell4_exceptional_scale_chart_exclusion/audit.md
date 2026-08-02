# Audit

1. Each scale factorization is reconstructed exactly in FLINT.
2. Linear roots are extracted only from degree-one factors.  Every other
   factor is an irreducible cubic in the finite-field factorization.
3. The root ledger is the union across all six scales; multiplicities affect
   scale order but not the zero set.
4. Guard exclusion is checked in the original common localization and does
   not rely on the compact plane equations being valid at a scale zero.
5. The claim is base-field only; no extension-field emptiness is asserted.

Mutation controls remove a root, alter a factor degree, and alter the guard
evaluation; each must fail verification.
