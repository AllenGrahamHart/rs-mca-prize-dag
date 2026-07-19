# Dependency sub-DAG - PMA sigma-one paired-core abundance obstruction

```text
pma_sigma_one_paired_core_normalization [PROVED]
  -> pma_sigma_one_paired_core_abundance [PROVED]

pma_sigma_one_paired_core_abundance --ev--> pma_wide_residual [REFUTED]
pma_sigma_one_paired_core_abundance --req-> petal_mixed_amplification [TARGET]
```

The node cuts an unweighted core census. It does not bound the weighted Post
sum.
