# Dependency sub-DAG: L1 fixed-support defect Johnson bound

```text
l1_polarized_petal_entropy_ledger [PROVED] ----------------req----+
pma_saturated_mixed_support_kernel [PROVED] ----------------req----+
pma_petal_pattern_root_pinning_ledger [PROVED] --------------req----+
                                                                      v
l1_fixed_support_defect_johnson_bound [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
