# Dependency sub-DAG: L1 joint core/background Johnson bound

```text
l1_fixed_support_defect_johnson_bound [PROVED] ----------req----+
l1_background_quotient_johnson_bound [PROVED] -----------req----+
l1_cross_quotient_split_descent_obstruction [PROVED] ----req----+
pma_petal_pattern_root_pinning_ledger [PROVED] -----------req----+
                                                                  v
l1_joint_core_background_johnson_bound [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
