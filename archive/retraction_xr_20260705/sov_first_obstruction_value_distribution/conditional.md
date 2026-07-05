# conditional: sov_first_obstruction_value_distribution

## Predicate nodes

- `sov_first_obstruction_sensitivity`
- `sov_hminus1_coefficient_distribution`

## Claim

Conditional on small fibers for the `h-1` locator coefficient, the first
obstruction `O_{h-1}` has small enough fibers on anchored cores to meet the
active-core budget.

## Proof

The proved predicate `sov_first_obstruction_sensitivity` says that, after the
higher coefficients determining the forced root are fixed, changing only the
locator coefficient `[X^{h-1}]L` leaves the forced root unchanged and changes
the first obstruction by exactly the negative of that coefficient change.

Thus, on each forced-root fiber, the map from `[X^{h-1}]L` to `O_{h-1}` is a
translation by a fixed value and a sign. Translation and sign do not change
fiber sizes.

The predicate `sov_hminus1_coefficient_distribution` supplies the missing
small-fiber estimate for `[X^{h-1}]L` on anchored cores under this same
conditioning. Transporting that estimate through the affine sensitivity map
gives the identical fiber bound for `O_{h-1}`. This is the desired first-
obstruction value-distribution statement.
