# Dependency sub-DAG: L1 joint Plotkin-boundary payment

```text
l1_joint_core_background_johnson_bound [PROVED] ----req----+
l1_joint_johnson_source_scale_gate [PROVED] ---------req----+
pma_petal_pattern_root_pinning_ledger [PROVED] -------req----+
                                                               v
l1_joint_plotkin_boundary_payment [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
