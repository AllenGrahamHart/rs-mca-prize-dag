# e22_tail_removed_factor_manifest_payload

- **status:** TARGET
- **closure:** proof

## Statement

Provide the actual E22 cofactor factorization manifest from the divisor
constraints `L_{T_i} | H_i`:

- one common tail `B`;
- dyadic local moduli `M_i>t`;
- the bound `|B| < min_i M_i`;
- for every touched petal, a quotient-value set `Z_i`; and
- an exact squarefree identity

```text
L_{T_i\B}(X) = prod_{z in Z_i} (X^{M_i} - z)
```

for the non-tail roots forced by the touched-petal cofactor divisor.

## Falsifier

A touched-petal cofactor divisor pattern for which no common bounded tail and
exact quotient-factor identity of this form exists.
