# gap1_noneq_mass conditional proof

## Predicate nodes

- `gap1_product_model`

## Claim

The non-equivariant periodic escape stratum is bounded by `poly(n) * FM` once
the product-model predicate is available.

## Proof

By the proved confinement and isotypic refinement machinery, a `K_M`-stable
agreement object decomposes into isotypic character pieces. The non-equivariant
case is precisely the multi-isotypic case: more than one character contributes
on the stable stratum.

The predicate `gap1_product_model` packages the already-banked tower product
mechanism together with the terminal-reserve reduction: cross-character
amplification is removed, active characters telescope to the joint stabilizer,
and the remaining leaf is identified with the quotient-row exact-list supply.
Those internal ingredients are tracked as evidence/support for
`gap1_product_model`, not as separate logical predicates of this parent.

Thus the terminal product is at most `poly(n) * FM`, and the whole
non-equivariant periodic stratum satisfies the GAP-1 bound conditionally on
`gap1_product_model`.
