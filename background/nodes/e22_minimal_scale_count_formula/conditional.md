# conditional: e22_minimal_scale_count_formula

## Predicate nodes

- `e22_minimal_scale_partition`
- `e22_minimal_scale_column_evaluation`

## Claim

Conditional on the exact column evaluation, the dyadic quotient staircase
pricing column counts exactly the support classes satisfying the minimal-scale
tail criterion.

## Proof

The proved predicate `e22_minimal_scale_partition` partitions all selected
canonical representatives with at least one admissible dyadic scale into
disjoint cells indexed by the unique minimal admissible modulus. By
`e22_minimal_scale_tail_criterion`, those cells are exactly the supports whose
canonical tail data satisfy the tail-minimal predicate at their selected
scale.

The predicate `e22_minimal_scale_column_evaluation` now assembles the proved
triangular accounting identity with `e22_minimal_scale_overlap_counts`. It
states that the dyadic quotient staircase pricing column, including its
declared duplicate subtraction or multiplicity factor, equals the sum over
these disjoint cells. Because the cells are disjoint and exhaustive for the
selected representatives, that column counts each tail-minimal support class
exactly with the declared multiplicity and counts no non-selected duplicate
class.

This proves the minimal-scale count formula.
