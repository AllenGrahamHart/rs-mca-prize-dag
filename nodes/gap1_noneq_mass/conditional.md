# gap1_noneq_mass conditional proof

## Predicate nodes

- `gap1_product_model`
- `tr_joint_telescope`
- `tr_perleaf_list_ident`

## Claim

The non-equivariant periodic escape stratum is bounded by `poly(n) * FM` once
the product model and TR terminal-reserve predicates are available.

## Proof

By the proved confinement and isotypic refinement machinery, a `K_M`-stable
agreement object decomposes into isotypic character pieces. The non-equivariant
case is precisely the multi-isotypic case: more than one character contributes
on the stable stratum.

The predicate `gap1_product_model` removes cross-character amplification: the
multi-isotypic mass is bounded by the per-character product along the field
tower. Therefore any possible super-polynomial contribution must come from the
terminal product of per-character sets.

The predicates `tr_joint_telescope` and `tr_perleaf_list_ident` are exactly the
terminal reserve chain. They telescope active characters to the joint
stabilizer and identify the remaining leaf with a quotient-row exact-list
instance supplied by the list lane.

Thus the terminal product is at most `poly(n) * FM`, and the whole
non-equivariant periodic stratum satisfies the GAP-1 bound conditionally on
those predicates.
