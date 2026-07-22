# Dependency sub-DAG: L1 general first-layout domination

```text
l1_core_defect_reduction [PROVED]
    --req--> l1_general_first_layout_domination [PROVED]
                  |--ev--> l1_mixed_residual_intersection_pin [PROVED]
                  |--ev--> l1_mixed_petal_amplification [TARGET]
                  `--ev--> petal_mixed_amplification [TARGET]
```

The new node proves the base-polynomial form directly and generalizes the
structural part of `pma_sigma_one_first_layout_domination`. Its evidence edges
remove a composition mechanism but do not pay the one-layout residual.
