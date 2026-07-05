# conditional: e22_common_tail_invariance_payload

## Predicate nodes

- `e22_tail_removed_factor_manifest_soundness`
- `e22_tail_removed_factor_manifest_payload`

## Claim

Conditional on the actual tail-removed factor manifest, the E22 common-tail
invariance payload holds.

## Proof

The proved node `e22_tail_removed_factor_manifest_soundness` says that a
manifest with one common tail `B`, dyadic local moduli `M_i>t`, the bound
`|B|<min_i M_i`, and exact identities

```text
L_{T_i\B}(X) = prod_z (X^{M_i}-z)
```

for every touched petal implies that every non-tail set `T_i\B` is invariant
under the `M_i`-th-root kernel.

The remaining predicate `e22_tail_removed_factor_manifest_payload` is exactly
the assertion that the actual E22 cofactor divisor constraints provide such a
manifest. Substituting that manifest into the proved soundness rule gives the
common tail, local moduli, tail bound, and kernel-invariant non-tail sets
required by this payload.
