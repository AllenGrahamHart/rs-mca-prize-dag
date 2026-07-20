# Dependency sub-DAG: L1 joint-Johnson source-scale gate

```text
l1_joint_core_background_johnson_bound [PROVED] ----req----+
l1_fixed_support_defect_johnson_bound [PROVED] ------req----+
pma_official_rate_small_source_degree_sieve [PROVED] -req----+
                                                               v
l1_joint_johnson_source_scale_gate [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
