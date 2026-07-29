# Audit

- The exact field is `Q(zeta_128)`, not `Q(zeta_256)` or its real subfield.
- The target is pairwise class separation, not merely class number or
  nonprincipality.
- The prime 257 splits completely because `257=1 mod 128`.
- The published source fixes the class coordinate and Galois multipliers, but
  its released software does not expose the n=64 class ledger.
- The source-derived modular orbit has been checked independently with exact
  integer arithmetic.
- No class-group computation has been replayed under the repository protocol;
  the node therefore remains `TARGET`.
