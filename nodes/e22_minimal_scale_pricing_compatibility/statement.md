# e22_minimal_scale_pricing_compatibility

- **status:** PROVED
- **closure:** proof

## Statement

The dyadic quotient staircase pricing column, as evaluated by
`dyadic_profile_evaluation`, counts the minimal-scale representatives selected
by `e22_dyadic_minimal_scale_selector` with exactly the declared multiplicity.

Equivalently, any cross-scale duplicate contribution from non-minimal
representations is either absent from the column or is removed by an explicit
declared multiplicity factor.

This is proved from the tail-minimality criterion and the exact count formula
for classes satisfying that criterion.

## Falsifier

A selected canonical representative that is omitted, duplicated, or assigned
the wrong multiplicity by the dyadic quotient staircase pricing column.
