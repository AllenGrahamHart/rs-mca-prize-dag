# proof: e22_residual_minimality_multiplicity_filter

The proved node `e22_lower_scale_filter_inclusion_exclusion` expresses the
minimality condition

```text
|B_{M'}(R)| >= M'        for every dyadic M'<M_i
```

as the finite inclusion-exclusion complement of the smaller-scale
admissibility events.

The proved node `e22_lower_scale_intersection_profile_counts` gives the exact
`dyadic_profile_evaluation`-weighted count of every intersection appearing in
that inclusion-exclusion formula. Substituting these counts into the finite
identity gives exactly the weighted residual profiles whose selected minimal
scale is `M_i`.

Thus the raw residual-profile generating function has been filtered by both
lower-scale nonadmissibility and the declared multiplicity convention. The
result is the exact overlap count `O_{i,j}`.
