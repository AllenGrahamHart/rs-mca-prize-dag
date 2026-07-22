# Claim contract - L1 general polynomial-pullback interleaving descent

## Inputs

- a finite field `K`, a monic degree-`s` polynomial `P`, and degree cap `k`;
- a domain `D`, received word `U`, and `b` labels carrying complete
  `s`-point fibers in `D`;
- a complete-fiber agreement threshold `h`.

## Outputs

- the unique normal form `(GP1)` with exact component caps `(GP2)`;
- the fiberwise agreement equivalence `(GP3)`;
- the exact evaluation-kernel exponent `(GP4)`;
- the quotient interleaved-list bounds `(GP5)` and `(GP6)`.

## Falsifier

A failed normal-form reconstruction or uniqueness, a complete fiber violating
`(GP3)`, a wrong kernel dimension, or a list larger than the printed
kernel-times-interleaved bound.

## Nonclaims

No ordinary quotient-list estimate is asserted for arbitrary label domains;
partial fibers, residual domain points, and large `kappa` remain consumer
obligations.
