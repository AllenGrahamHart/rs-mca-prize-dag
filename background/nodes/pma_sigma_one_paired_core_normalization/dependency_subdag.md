# Dependency sub-DAG - PMA sigma-one paired-core normalization

```text
pma_sigma_one_b11_scope [PROVED] --req--+
                                             +--> pma_sigma_one_paired_core_normalization [PROVED]
l1_program_frontier [PROVED] --------req-----+

pma_sigma_one_paired_core_normalization --ev--> pma_wide_residual [REFUTED]
pma_sigma_one_paired_core_normalization --req-> petal_mixed_amplification [TARGET]
pma_sigma_one_paired_core_normalization --req-> pma_sigma_one_paired_core_abundance [PROVED]
```

The theorem canonicalizes the chart index. It does not bound the resulting
weighted paired-core sum.
