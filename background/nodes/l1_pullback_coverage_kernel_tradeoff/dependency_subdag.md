# Dependency sub-DAG: L1 pullback coverage/kernel tradeoff

```text
l1_general_pullback_interleaving_descent [PROVED] ---req---+
l1_partial_pullback_johnson_router [PROVED] ---------req---+
                                                           v
l1_pullback_coverage_kernel_tradeoff [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

The node composes the earlier router and exports its sharpened automatic-
kernel corollary directly to the live consumers.
