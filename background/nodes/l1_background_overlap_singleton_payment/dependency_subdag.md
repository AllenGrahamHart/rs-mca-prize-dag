# Dependency sub-DAG: L1 background-overlap singleton payment

```text
l1_fixed_support_codeword_quotient_bound [PROVED] ---req----+
l1_bounded_retained_core_payment [PROVED] ----------req----+
pma_petal_pattern_root_pinning_ledger [PROVED] -----req----+
                                                               v
l1_background_overlap_singleton_payment [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
