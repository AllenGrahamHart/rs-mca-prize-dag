# Dependency sub-DAG

```text
rate_half_mca_rank11_dense_locator_component_incidence_dichotomy [PROVED]
rate_half_mca_rank11_dense_root_highspan_saturation              [PROVED]
rate_half_mca_rank11_rank9_residual_petal_capacity_cut           [PROVED]
rate_half_mca_weighted_split_pencil_selected_support_cap         [PROVED]
                              |
                              v
rate_half_mca_rank11_rank9_minimal_shortening_split_pencil_payment [PROVED]
                              |
                              v
rank nine survives only on 11<=K'<=15528
```

The previously proved rank-eight minimal-shortening exclusion is recovered
inside the same dimension-equality argument. The new ingredient is the
full-density weighted split-pencil payment for rank nine.
