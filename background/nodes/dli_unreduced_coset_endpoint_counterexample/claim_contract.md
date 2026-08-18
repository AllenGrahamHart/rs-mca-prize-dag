# Claim contract

## Inputs

- The challenge row bounds `n=2^41`, `t=2^33`, `q<2^256`, and `n | q-1`.
- The primitive/quotient ownership split printed by
  `x4_exactlist_staircase_split/REDUCTION_PACKET.md`.

## Output

An exact admissible prime and a family of more than `2^127` central
`t`-null quotient-periodic subsets whose unreduced normalized mass exceeds
`2^126`.

## Nonclaims

- No primitive `t`-null subset is exhibited.
- No reduced DLI, C1, C2, WCL, LIST, or MCA endpoint is proved or refuted.
- The result does not rely on a probable-prime test; primality follows from
  the printed Proth certificate.
