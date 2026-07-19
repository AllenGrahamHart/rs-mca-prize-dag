# Audit

- Re-derived the factorization directly from the exact norm identity.
- Checked coprimality before making any derivative-multiplicity inference.
- The verifier covers squarefree and repeated factors in `C`, exact recovery
  of `u`, and a cube divisor that fails the cofactor test.
- The router does not treat a derivative gcd bound as sufficient for an
  intermediate candidate.
