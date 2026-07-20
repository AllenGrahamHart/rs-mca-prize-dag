# Dependency sub-DAG: L1 bounded retained-core payment

```text
l1_polarized_petal_entropy_ledger [PROVED] --------req----+
pma_petal_pattern_root_pinning_ledger [PROVED] ----req----+
pma_saturated_mixed_support_kernel [PROVED] -------req----+
                                                               v
l1_bounded_retained_core_payment [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
