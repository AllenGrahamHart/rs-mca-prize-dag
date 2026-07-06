# proof: e22_minimal_scale_count_formula

The proved node `e22_minimal_scale_partition` partitions all selected
canonical representatives with at least one admissible dyadic scale into
disjoint cells indexed by their unique minimal admissible modulus.

By `e22_minimal_scale_tail_criterion`, these cells are exactly the supports
whose canonical tail data satisfy the tail-minimal predicate at their
selected scale.

The proved node `e22_minimal_scale_column_evaluation` states that the dyadic
quotient staircase pricing column, including its declared duplicate
subtraction or multiplicity factor, equals the sum over these disjoint cells.
Because the cells are disjoint and exhaustive for the selected
representatives, the column counts each tail-minimal support class exactly
with the declared multiplicity and counts no non-selected duplicate class.
