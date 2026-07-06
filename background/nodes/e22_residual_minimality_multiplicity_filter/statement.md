# e22_residual_minimality_multiplicity_filter

- **status:** PROVED
- **closure:** proof

## Statement

For every dyadic pair `M_i<M_j`, apply both remaining filters to the
residual-profile generating function:

1. the lower-scale nonadmissibility constraints

```text
|B_{M'}(R)| >= M'        for every dyadic M'<M_i;
```

2. the declared duplicate-subtraction or multiplicity convention used by
   `dyadic_profile_evaluation`.

The resulting exact formula is the overlap count `O_{i,j}` for
minimal-scale-`M_i` support classes that are also raw-counted at `M_j`.

This is proved from:

- `e22_lower_scale_filter_inclusion_exclusion`, which proves the formal
  complement-of-union filter for smaller-scale admissibility events; and
- `e22_lower_scale_intersection_profile_counts`, which supplies the exact
  weighted lower-scale intersections.

## Falsifier

A support passing the residual budget but failing minimality or pricing
multiplicity, or a genuine minimal-scale support removed by the filter.
