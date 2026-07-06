# conditional: e22_overlap_residual_profile_formula

## Predicate nodes

- `e22_residual_profile_generating_function`
- `e22_residual_minimality_multiplicity_filter`

## Claim

Conditional on the lower-scale minimality and pricing-multiplicity filter, the
exact residual-profile formula for every `O_{i,j}` is known.

## Proof

The proved node `e22_residual_profile_generating_function` gives the exact
product generating function for canonical scale-`M_i` data satisfying both
`|B_i|<M_i` and the raw larger-scale residual inequality

```text
|B_i| + M_i*r_{i,j}(S_i) < M_j.
```

The remaining predicate `e22_residual_minimality_multiplicity_filter` applies
exactly the two filters not present in the raw generating function:

```text
|B_{M'}(R)| >= M'        for every dyadic M'<M_i,
```

and the declared `dyadic_profile_evaluation` multiplicity convention. After
these filters, the surviving objects are precisely the minimal-scale-`M_i`
supports counted by the cross-scale overlap `O_{i,j}`.
