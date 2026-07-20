# Dependency sub-DAG: L1 background-quotient Johnson bound

```text
l1_background_overlap_singleton_payment [PROVED] ----req----+
l1_fixed_support_codeword_quotient_bound [PROVED] ----req----+
pma_petal_pattern_root_pinning_ledger [PROVED] -------req----+
                                                                v
l1_background_quotient_johnson_bound [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
