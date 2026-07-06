# e22_minimal_scale_column_evaluation

- **status:** PROVED
- **closure:** proof

## Statement

The dyadic quotient staircase pricing column, as evaluated by
`dyadic_profile_evaluation` and with the declared duplicate subtraction or
multiplicity factor, equals the sum over the disjoint minimal-scale partition
cells from `e22_minimal_scale_partition`.

This is proved from the dyadic-chain triangular accounting identity and the
exact cross-scale overlap formulas.

## Falsifier

A minimal-scale partition cell whose contribution to the dyadic pricing
column is omitted, duplicated, or assigned the wrong multiplicity.
