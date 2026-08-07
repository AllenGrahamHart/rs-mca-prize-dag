# Dependency sub-DAG

```text
pma_ratehalf_complement_linear_slice_reduction [PROVED]
  |
  v
l1_fpc5_ratehalf_inverse_ratio_degree_gate [PROVED]
  |
  +--req-------> l1_fpc5_ratehalf_m4_t3_high_multiplier_pade_reduction [PROVED]
  +--evidence--> l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET]
  +--evidence--> shared_census_kernel [TARGET]
```
