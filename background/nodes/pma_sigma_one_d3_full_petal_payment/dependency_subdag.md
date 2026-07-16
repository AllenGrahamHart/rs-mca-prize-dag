# Dependency sub-DAG - PMA sigma-one defect-three full-petal payment

```text
pma_source_paving_bridge [PROVED] -------------------+
pma_sigma_one_low_defect_payment [PROVED] -----------+-- req -->
pma_sigma_one_d3_background_payment [PROVED] --------+          \
  pma_sigma_one_d3_full_petal_payment [PROVED]
                         | ev
                         v
                pma_wide_residual [REFUTED]
```

The new theorem removes the full-petal portion of the first unpaid finite
cell. It leaves one atomic red leaf: the diffuse defect-three class, higher
defects and the general asymptotic residual remain inside
`pma_wide_residual`.

The later `pma_sigma_one_first_layout_domination` theorem removes finite chart
composition after consuming this payment once in the first layout.
