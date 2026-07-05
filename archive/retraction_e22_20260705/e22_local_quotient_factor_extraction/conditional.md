# conditional: e22_local_quotient_factor_extraction

## Predicate nodes

- `e22_cofactor_common_tail_quotient_structure`
- `e22_tail_removed_quotient_factor_passthrough`

## Claim

Conditional on the E22-specific common-tail quotient structure, the local
quotient factors `X^{M_i}-z` are extracted from the touched-petal cofactors.

## Proof

The predicate `e22_cofactor_common_tail_quotient_structure` supplies one
common exceptional tail `B`, the bound

```text
|B| < min_i M_i,
```

dyadic local moduli `M_i>t`, and the fact that every non-tail root set
`T_i\B` is a union of full fibers of `x -> x^{M_i}`.

The proved node `e22_tail_removed_quotient_factor_passthrough` applies to the
divisibility relation

```text
L_{T_i}(X) | H_i(X).
```

Since the non-tail fibers have locators `X^{M_i}-z`, removing the common tail
factor leaves precisely those quotient factors in the cofactor. Therefore the
local quotient-factor extraction statement follows.
