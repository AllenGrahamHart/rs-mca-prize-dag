# dependency sub-DAG: e22_lower_scale_intersection_formula_payload

Edges are directed from dependency to consumer.

```text
e22_cross_scale_support_canonical_form [PROVED]
    -> e22_lower_scale_intersection_formula_payload [PROVED]

e22_residual_profile_generating_function [PROVED]
    -> e22_lower_scale_intersection_formula_payload [PROVED]

dyadic_profile_evaluation [PROVED]
    -> e22_lower_scale_intersection_formula_payload [PROVED]

e22_lower_scale_intersection_formula_payload [PROVED]
    -> e22_lower_scale_intersection_profile_counts [CONDITIONAL]
    -> e22_residual_minimality_multiplicity_filter [CONDITIONAL]
```

This node supplies the actual lower-scale intersection formulas consumed by
the proved weighted-bijection soundness rule.
