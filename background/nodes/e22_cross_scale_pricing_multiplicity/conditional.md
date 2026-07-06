# conditional: e22_cross_scale_pricing_multiplicity

## Predicate nodes

- `e22_dyadic_minimal_scale_selector`
- `e22_minimal_scale_pricing_compatibility`

## Claim

Conditional on pricing-column compatibility for the selected representatives,
the quotient staircase pricing column counts canonical cross-scale classes
with the declared multiplicity.

## Proof

The proved node `e22_dyadic_minimal_scale_selector` gives each dyadic
canonical support-scale class a unique selected representative: the minimal
admissible quotient modulus and its recovered tail/full-fiber data.

The predicate `e22_minimal_scale_pricing_compatibility` says that the exact
dyadic quotient staircase column counts precisely those selected
representatives with the declared multiplicity, or equivalently that any raw
non-minimal duplicates have been removed by the stated factor.

Therefore each canonical cross-scale class contributes exactly once, or with
exactly the declared multiplicity, to the pricing column. Quotienting by
cross-scale duplicates neither overcounts nor undercounts E22 challengers.
