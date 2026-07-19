# proof: e22_overlap_residual_profile_formula

The proved node `e22_residual_profile_generating_function` gives the exact
product generating function for canonical scale-`M_i` data satisfying
`|B_i|<M_i` and the raw larger-scale residual inequality

```text
|B_i| + M_i*r_{i,j}(S_i) < M_j.
```

The proved node `e22_residual_minimality_multiplicity_filter` applies exactly
the two filters not present in the raw generating function:

```text
|B_{M'}(R)| >= M'        for every dyadic M'<M_i,
```

and the declared `dyadic_profile_evaluation` multiplicity convention.

After these filters, the surviving objects are precisely the
minimal-scale-`M_i` supports that are also raw-admissible at `M_j`. Therefore
the resulting formula is the exact cross-scale residual-profile formula for
`O_{i,j}`.
