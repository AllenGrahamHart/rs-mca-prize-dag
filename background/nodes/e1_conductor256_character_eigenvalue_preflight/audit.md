# Audit

## Arithmetic seams

- Machin's formula is evaluated with an alternating-series remainder.
- Trigonometric arguments remain in `[0,pi/2]`; monotonic endpoint evaluation
  and explicit Taylor remainders are valid there.
- Logarithm range reduction puts every argument in `[1,2)`, where the atanh
  parameter is in `[0,1/3)`.
- Decimal negation uses `copy_negate()`. Unary Decimal minus obeys the ambient
  context and previously exposed a 28-digit rounding hazard during verifier
  construction.
- Every nontrivial spectral rectangle excludes zero; conjugate frequencies
  and the real `j=32` frequency are checked.
- The DFT uses squared-modulus logs and therefore retains the factor two from
  the router.
- The prize floor uses the strict inequalities `p>2^255` and `mu>=1`.
- The dynamic program counts 64-coordinate zero-sum vectors, not 63
  unconstrained coordinates.

## Scope ruling

The universal ellipsoid is an enclosing filter.  Showing that it contains
the family `(CEP5)` rejects only an enumeration that generates that filter
before consuming sparse algebra.  It neither proves those units arise from
collision pairs nor refutes the desired 367-orbit theorem.

## Compute ruling

The verifier uses under one second of tiny local arithmetic and no Modal
credit.  The projected ambient searches are not authorized.  A successor
must expose an algebraic sparse-first state space and conservatively price it
before execution.
