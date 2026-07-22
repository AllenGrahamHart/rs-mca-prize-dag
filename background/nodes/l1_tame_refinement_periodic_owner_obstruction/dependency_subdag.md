# Dependency sub-DAG: L1 tame-refinement periodic-owner obstruction

```text
l1_tame_fixed_petal_refinement_census [PROVED] ---req---+
pma_exact_periodic_owner [PROVED] ----------------req---+
                                                         v
l1_tame_refinement_periodic_owner_obstruction [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

The node is a compatibility fence between two proved interfaces. It changes
no consumer status.
