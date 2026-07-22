# Dependency sub-DAG: L1 partial-pullback Johnson router

```text
l1_general_pullback_interleaving_descent [PROVED] -----req----+
l1_tame_fixed_petal_refinement_census [PROVED] --------req----+
                                                               v
l1_partial_pullback_johnson_router [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

This is the positive-gate payment for incomplete and partially agreed
pullbacks. It introduces no conditional premise.
