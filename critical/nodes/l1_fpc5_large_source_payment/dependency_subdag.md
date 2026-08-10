# Dependency sub-DAG

```text
pma_official_rate_small_source_degree_sieve [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_large_source_exact_prefilter [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_saturated_slice_dimension [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_anchor_coordinate [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_anchor_pade_chart [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_joint_anchor_owner [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_joint_owner_packing [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_joint_owner_split_pencil [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_joint_owner_ambient_mds_census [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_owner_free_cauchy_divisor_chart [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_cauchy_hankel_kernel [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_fixed_background_hankel_codimension [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_large_source_payment [TARGET]
  --req--> l1_full_petal_fpc5_payment [CONDITIONAL]
```
