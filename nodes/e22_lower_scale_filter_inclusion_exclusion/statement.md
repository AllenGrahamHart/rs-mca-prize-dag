# e22_lower_scale_filter_inclusion_exclusion

- **status:** PROVED
- **closure:** proof

## Statement

Fix a dyadic pair `M_i<M_j` and a residual-profile universe `U_{i,j}` counted
by `e22_residual_profile_generating_function`. For each smaller dyadic scale
`M'<M_i`, let `A_{M'}` be the event that the same support is admissible at
scale `M'`.

Then the minimality condition

```text
|B_{M'}(R)| >= M'        for every M'<M_i
```

is exactly the complement of the union of the events `A_{M'}`. Thus the
weighted count of minimal-scale-`M_i` residual profiles is

```text
sum_{S subset Smaller(M_i)} (-1)^|S| W( intersection_{M' in S} A_{M'} ),
```

where the empty intersection is all of `U_{i,j}` and `W` is the declared
`dyadic_profile_evaluation` multiplicity weight.

## Falsifier

A weighted residual universe where inclusion-exclusion does not remove
exactly the objects admissible at at least one smaller dyadic scale.
