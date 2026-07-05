# dependency sub-DAG: e22_weighted_intersection_certificate_soundness

Edges are directed from dependency to consumer.

```text
e22_residual_profile_generating_function [PROVED]
    -> e22_weighted_intersection_certificate_soundness [PROVED]
    -> e22_lower_scale_intersection_profile_counts [CONDITIONAL]

e22_minimal_scale_partition [PROVED]
    -> e22_weighted_intersection_certificate_soundness [PROVED]

dyadic_profile_evaluation [PROVED]
    -> e22_weighted_intersection_certificate_soundness [PROVED]
```

This node proves only the weighted-bijection soundness of an intersection
formula certificate. It does not provide the formulas.
