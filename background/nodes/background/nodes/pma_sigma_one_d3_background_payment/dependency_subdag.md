# Dependency sub-DAG - PMA sigma-one defect-three background payment

```text
pma_source_paving_bridge [PROVED] -----------+
pma_sigma_one_low_defect_payment [PROVED] ---+--> pma_sigma_one_d3_background_payment [PROVED]
                                                                    |
                                                                    v evidence
                                                       pma_wide_residual [REFUTED]
```

This is a proved boundary payment above the existing red leaf. No conditional
decomposition is introduced below that leaf.
