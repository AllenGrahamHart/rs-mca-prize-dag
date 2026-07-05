# dependency sub-DAG: e22_minimal_scale_overlap_counts

Edges are directed from dependency to consumer.

```text
e22_minimal_scale_partition [PROVED]
    -> e22_minimal_scale_overlap_counts [PROVED]
    -> e22_minimal_scale_column_evaluation [PROVED]

dyadic_profile_evaluation [PROVED]
    -> e22_lower_scale_intersection_profile_counts [PROVED]
    -> e22_residual_minimality_multiplicity_filter [PROVED]
    -> e22_overlap_residual_profile_formula [PROVED]
    -> e22_minimal_scale_overlap_counts [PROVED]

e22_cross_scale_support_canonical_form [PROVED]
    -> e22_overlap_nested_fiber_residual_identity [PROVED]
    -> e22_residual_profile_generating_function [PROVED]
    -> e22_lower_scale_filter_inclusion_exclusion [PROVED]
    -> e22_residual_minimality_multiplicity_filter [PROVED]
    -> e22_overlap_residual_profile_formula [PROVED]
    -> e22_minimal_scale_overlap_counts [PROVED]
```

The weighted lower-scale intersections needed by the proved triangular
accounting identity are now supplied by proved nodes.
