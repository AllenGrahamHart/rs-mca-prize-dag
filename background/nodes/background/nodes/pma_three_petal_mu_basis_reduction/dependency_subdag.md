# Dependency sub-DAG - PMA three-petal mu-basis reduction

```text
pma_saturated_mixed_support_kernel [PROVED]
                 |
                 | req: exact-defect saturation and pairwise fiber coprimality
                 v
pma_three_petal_mu_basis_reduction [PROVED]
                 |
                 | ev: exact arbitrary-locator normal form; growing-e count open
                 v
petal_mixed_amplification [TARGET] --req--> imgfib [CONDITIONAL]

pma_full_petal_band_composition [PROVED]
                 |
                 | req: identifies the remaining M=4,t=3 full-petal strip
                 +------> pma_three_petal_mu_basis_reduction
```

The edge into `petal_mixed_amplification` is evidence, not a requirement that
closes the target. The new node classifies the contributor space but does not
count its growing root-excess split locus.
