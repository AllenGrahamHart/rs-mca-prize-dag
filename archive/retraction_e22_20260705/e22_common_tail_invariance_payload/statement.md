# e22_common_tail_invariance_payload

- **status:** CONDITIONAL
- **closure:** proof

## Statement

From the E22 cofactor divisor constraints, provide the actual common-tail
invariance certificate:

- one common tail `B`;
- dyadic local moduli `M_i>t`;
- the bound `|B| < min_i M_i`;
- kernel invariance of every `T_i \ B` under the `M_i`-th-root kernel.

This is reduced to:

- `e22_tail_removed_factor_manifest_soundness`, the proved rule that an exact
  tail-removed quotient-factor manifest gives the required kernel-invariant
  non-tail sets; and
- `e22_tail_removed_factor_manifest_payload`, the remaining actual E22
  cofactor factorization manifest.

## Falsifier

A cofactor divisor pattern for which no bounded common tail and admissible
dyadic local kernel-invariance package exists.
