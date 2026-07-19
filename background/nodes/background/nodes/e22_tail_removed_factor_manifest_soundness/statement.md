# e22_tail_removed_factor_manifest_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Assume a tail-removed factor manifest supplies:

- one common tail `B`;
- dyadic local moduli `M_i>t`;
- the bound `|B| < min_i M_i`;
- for every touched petal, a finite set of quotient values `Z_i`; and
- the exact squarefree locator identity

```text
L_{T_i\B}(X) = prod_{z in Z_i} (X^{M_i} - z).
```

Then `e22_common_tail_invariance_payload` holds: each non-tail set `T_i\B`
is invariant under the `M_i`-th-root kernel of `x -> x^{M_i}`, with the
declared common tail and tail bound.

## Falsifier

A verified tail-removed quotient-factor manifest whose non-tail set is not
kernel-invariant, or whose tail/modulus data fail the common-tail payload.
