# dependency sub-DAG: e22_residual_minimality_multiplicity_filter

Edges are directed from dependency to consumer.

```text
e22_minimal_scale_partition [PROVED]
    -> e22_weighted_intersection_certificate_soundness [PROVED]
    -> e22_lower_scale_intersection_profile_counts [PROVED]
    -> e22_residual_minimality_multiplicity_filter [PROVED]
    -> e22_overlap_residual_profile_formula [PROVED]

dyadic_profile_evaluation [PROVED]
    -> e22_weighted_intersection_certificate_soundness [PROVED]

e22_residual_profile_generating_function [PROVED]
    -> e22_lower_scale_filter_inclusion_exclusion [PROVED]
    -> e22_residual_minimality_multiplicity_filter [PROVED]

e22_residual_profile_generating_function [PROVED]
    -> e22_weighted_intersection_certificate_soundness [PROVED]

e22_lower_scale_intersection_formula_payload [PROVED]
    -> e22_lower_scale_intersection_profile_counts [PROVED]
```

The exact weighted intersections needed by the proved inclusion-exclusion
filter are now supplied by `e22_lower_scale_intersection_profile_counts`.
