# Dependency sub-DAG: L1 marked common-pencil quotient-boundary router

```text
l1_marked_common_pencil_crt_fiber_bound [PROVED] --req--+
                                                       |
pma_quotient_closure_scope [PROVED] -----------req-----+
                                                       v
l1_marked_common_pencil_quotient_boundary_router [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

The second dependency supplies the exact scope guard: quotient factorization
of a locator is not source-level exact-periodic ownership.

