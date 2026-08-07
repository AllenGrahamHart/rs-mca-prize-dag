# Dependency sub-DAG

```text
pma_three_petal_mu_basis_reduction [PROVED] -------------------+
pma_ratehalf_complement_linear_slice_reduction [PROVED] -------+
                                                                 v
  l1_fpc5_ratehalf_m4_t3_master_flat_descriptor [PROVED]
       |--ev--> l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET]
       `--ev--> shared_census_kernel [TARGET, off-critical]
```
