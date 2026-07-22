# Dependency sub-DAG: L1 general polynomial-pullback interleaving descent

```text
list_subsqrt_interleaving_collapse [PROVED] --------req----+
                                                           v
l1_general_pullback_interleaving_descent [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

The tame map census bounds how many fixed-petal maps must use this interface,
but is not required for the algebraic descent itself. The periodic-owner
obstruction explains why this broader interface is needed.
