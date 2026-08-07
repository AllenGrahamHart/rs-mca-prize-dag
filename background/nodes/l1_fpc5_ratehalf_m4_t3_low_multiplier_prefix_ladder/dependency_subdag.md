# Dependency sub-DAG

```text
pma_ratehalf_complement_linear_slice_reduction [PROVED] -----+
l1_fpc5_ratehalf_m4_t3_master_flat_descriptor [PROVED] ------+
                                                              v
  l1_fpc5_ratehalf_m4_t3_low_multiplier_prefix_ladder [PROVED]
       |--ev--> l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET]
       `--ev--> shared_census_kernel [TARGET, off-critical]
```
