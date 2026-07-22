# Dependency sub-DAG: L1 full-pullback divisibility/Johnson closure

```text
l1_tame_fixed_petal_refinement_census [PROVED] --------req----+
l1_general_pullback_interleaving_descent [PROVED] -----req----+
                                                               v
l1_full_pullback_divisibility_johnson_closure [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

This closes one explicit sector and introduces no new premise.
