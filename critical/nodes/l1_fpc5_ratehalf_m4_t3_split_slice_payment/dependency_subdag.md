# Dependency sub-DAG

```text
pma_ratehalf_complement_linear_slice_reduction [PROVED] --------+
l1_general_first_layout_domination [PROVED] --------------------+
l1_fpc5_ratehalf_m4_t3_first_layout_atom_collapse [PROVED] -----+
l1_fpc5_ratehalf_m4_t3_master_flat_descriptor [PROVED] ----------+
l1_fpc5_ratehalf_m4_t3_aligned_common_pencil_emptiness [PROVED] -+
l1_fpc5_ratehalf_m4_t3_misaligned_common_pencil_emptiness [PROVED]+
l1_fpc5_ratehalf_m4_t3_low_multiplier_prefix_ladder [PROVED] ----+
l1_fpc5_ratehalf_m4_t3_high_multiplier_pade_reduction [PROVED] --+
l1_fpc5_ratehalf_inverse_ratio_degree_gate [PROVED] ------------+
l1_fpc5_ratehalf_ls6_pair_determinant_router [PROVED] ----------+
l1_fpc5_ratehalf_ls6_determinant_coordinate_chart [PROVED] -----+
l1_fpc5_ratehalf_ls6_canonical_owner_packing [PROVED] ----------+
                                                                  v
  l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET]
    --req--> l1_full_petal_fpc5_payment [CONDITIONAL]
```
