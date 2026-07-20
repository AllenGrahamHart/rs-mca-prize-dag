# Dependency sub-DAG: L1 background-surplus Plotkin payment

```text
l1_joint_core_background_johnson_bound [PROVED] --req----+
l1_bounded_plotkin_excess_payment [PROVED] --------req----+
pma_petal_pattern_root_pinning_ledger [PROVED] -----req----+
                                                             v
l1_background_surplus_plotkin_payment [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
