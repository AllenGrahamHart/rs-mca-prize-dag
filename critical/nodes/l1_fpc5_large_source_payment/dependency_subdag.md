# Dependency sub-DAG

```text
pma_official_rate_small_source_degree_sieve [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_large_source_exact_prefilter [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_official_rate_prefilter_scale_gap [PROVED] --ev-->
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
l1_fpc5_tpetal_hankel_support_determinantal_system [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_hankel_grs_syndrome_shell [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_fixed_background_grs_shell_payment [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_shifted_johnson_grs_shell_cap [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_shifted_johnson_first_layout_payment [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_grs_shell_constant_weight_shortening_cap [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_grs_shortening_official_prefix_payment [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_large_source_payment [TARGET]
  --req--> l1_full_petal_fpc5_payment [CONDITIONAL]
```
