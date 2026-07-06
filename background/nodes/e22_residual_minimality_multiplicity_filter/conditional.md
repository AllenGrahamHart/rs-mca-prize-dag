# conditional: e22_residual_minimality_multiplicity_filter

## Predicate nodes

- `e22_lower_scale_filter_inclusion_exclusion`
- `e22_lower_scale_intersection_profile_counts`
- `e22_lower_scale_intersection_formula_payload`

## Claim

Conditional on the exact lower-scale intersection-profile counts, the
minimality and multiplicity filter for the E22 residual profiles is known.

## Proof

The proved node `e22_lower_scale_filter_inclusion_exclusion` expresses the
condition

```text
|B_{M'}(R)| >= M'        for every dyadic M'<M_i
```

as the finite inclusion-exclusion complement of the smaller-scale
admissibility events. The predicate
`e22_lower_scale_intersection_profile_counts` is now a conditional assembly
from weighted-intersection soundness and
`e22_lower_scale_intersection_formula_payload`. That payload supplies the
exact weighted count of every intersection appearing in that formula, using
the same `dyadic_profile_evaluation` multiplicity convention as the quotient
staircase column.

Substituting those intersection counts into the inclusion-exclusion identity
gives exactly the weighted count of residual profiles whose selected minimal
scale is `M_i`. This is the desired filter.
