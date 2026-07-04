# gap1_product_model conditional proof

## Predicate nodes

- `tr_joint_telescope`
- `tr_perleaf_list_ident`

## Claim

The tower product model closes once the TR terminal-reserve chain is supplied.

## Proof

The product half is already banked in the node statement: for a tower
`B = K_0 <= ... <= K_s`, each isotypic character is confined to one
intermediate-field line `alpha^r K`, and the recursion removes
cross-character amplification by bounding multi-character mass by the product
of the per-character sets.

The remaining issue is not another rank lemma; it is the terminal reserve:
the product over active characters must be bounded by `poly(n) * FM`.

The predicate `tr_joint_telescope` supplies the jointness step. Active
characters telescope to a single joint-stabilizer instance, with the
degenerate-tower correction column recorded in the node notes. Thus the product
over characters is replaced by one quotient-scale instance rather than by an
over-aggregated product carrying a `q^{M-1}` loss.

The predicate `tr_perleaf_list_ident` supplies the per-leaf count: the terminal
per-character set is the same-rate quotient-row exact-list kernel, so the list
lane's corrected quotient-row split is the needed supply.

Together these two predicates give the terminal reserve estimate. Combining
that estimate with the already-proved tower product mechanism proves the
conditional product model.
