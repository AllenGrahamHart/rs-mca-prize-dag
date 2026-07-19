# Dependency sub-DAG - PMA sigma-one low-defect payment

```text
pma_aux_list_reduction [PROVED] --------+
pma_source_paving_bridge [PROVED] ------+--> pma_sigma_one_low_defect_payment [PROVED]
pma_sigma_one_b11_scope [PROVED] -------+                         |
                                                                  v evidence
                                                     pma_wide_residual [REFUTED]
```

The theorem is a proved source payment above the red leaf. It does not split
the remaining `d>=3` target into speculative conditionals.
