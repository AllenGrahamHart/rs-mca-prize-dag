# Dependency sub-DAG

```text
rate_half_mca_rank11_component_ninesubset_target_router          [PROVED]
rate_half_mca_rank11_component_ninesubset_weighted_concentrator [PROVED]
rate_half_mca_rank11_rank9_weighted_component_cap               [PROVED]
                         |
                         v
rate_half_mca_rank11_rank9_residual_petal_capacity_cut          [PROVED]
                         |
                         v
rate_half_mca_rank11_rank9_exact_petal_partition_capacity_cut   [PROVED]
                         |
                         v
rank nine survives only on 10<=K'<=15528
```

The child changes only the optimization of the already proved disjoint
petal charge. It introduces no conditional premise.
