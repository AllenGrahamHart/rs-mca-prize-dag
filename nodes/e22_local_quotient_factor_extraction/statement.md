# e22_local_quotient_factor_extraction

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For E22 mixed/full-petal challengers satisfying the petal-locator divisibility
constraints

```text
L_{T_i}(X) | H_i(X),
H_i(X) = U(X)L_{Z\C}(X) - a_i L_{C\Z}(X),
```

there is one exceptional tail `B`, with size below the minimum local modulus,
such that after deleting `B` each touched-petal cofactor contributes only
quotient-fiber locator factors

```text
X^{M_i} - z
```

with dyadic `M_i > t`.

Equivalently, all non-tail roots forced by the E22 cofactor divisors come
from explicit local quotient factors.

This is reduced to:

- `e22_cofactor_common_tail_quotient_structure`, which remains to construct
  the common tail, prove its bound, choose dyadic local moduli, and show the
  non-tail roots are full quotient fibers; and
- `e22_tail_removed_quotient_factor_passthrough`, which proves that once that
  structure is known, the factors `X^{M_i}-z` pass through the divisor
  relation formally.

## Falsifier

A mixed/full-petal divisor pattern where, after every possible bounded common
tail is removed, some forced non-tail roots do not arise from quotient factors
`X^{M_i}-z`.
