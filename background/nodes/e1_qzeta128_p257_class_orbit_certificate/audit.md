# Audit

- The exact field is `Q(zeta_128)`, not `Q(zeta_256)` or its real subfield.
- The output is pairwise class separation, but the proved 2-group reduction
  makes two named nonprincipality tests sufficient.
- The prime 257 splits completely because `257=1 mod 128`.
- The published source fixes the class coordinate and Galois multipliers, but
  the conditional proof does not rely on those unreplayed values.
- The source-derived modular orbit has been checked independently with exact
  integer arithmetic.
- Real class number one is derived from the proved conductor-256 theorem by
  extension/norm and Weber oddness; it is not assumed from the slide.
- Both explicit ideal products must be nonprincipal. The Harbater proof
  closes `q_1q_65`; the fixed-field certificate for `q_1q_63` remains open.
- The node therefore remains `CONDITIONAL` on exactly one prime.
