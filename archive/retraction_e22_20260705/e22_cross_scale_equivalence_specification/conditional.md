# conditional: e22_cross_scale_equivalence_specification

## Predicate nodes

- `e22_cross_scale_support_canonical_form`
- `e22_cross_scale_pricing_multiplicity`

## Claim

Conditional on the pricing multiplicity predicate, the declared cross-scale
equivalence relation contains every equal-support representation and is
compatible with the quotient staircase pricing column.

## Proof

The proved predicate `e22_cross_scale_support_canonical_form` assigns every
support `R` a canonical set of admissible quotient moduli and, at each such
modulus, the recovered tail and selected full quotient fibers. Equal-support
representations therefore map to the same canonical support-scale object.

The predicate `e22_cross_scale_pricing_multiplicity` supplies the remaining
counting assertion: the quotient staircase pricing column counts these
canonical objects with exactly the declared multiplicity.

Thus all equal-support cross-scale representations are declared equivalent,
and the declared quotienting is compatible with the pricing column. This is
the desired cross-scale equivalence specification.
