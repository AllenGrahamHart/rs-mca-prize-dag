# Dependency sub-DAG

```text
l1_general_first_layout_domination [PROVED] ----------------ev----+
pma_two_full_petal_linear_slice_reduction [PROVED] ---------ev----+
l1_fpc5_m4_t2_official_codimension_sieve [PROVED] ----------ev----+
l1_fpc5_ratehalf_m4_t2_codimtwo_guarded_slice [PROVED] -----ev----+
l1_fpc5_ratehalf_m4_t2_sharp_cell_nonemptiness [PROVED] ----ev----+
l1_fpc5_ratehalf_m4_t2_sharp_projective_flat_descriptor
  [PROVED] --------------------------------------------------ev----+
l1_fpc5_ratehalf_m4_t2_sharp_gcd_triviality [PROVED] -------ev----+
l1_fpc5_ratehalf_m4_t2_sharp_dyadic_quotient_absence
  [PROVED] --------------------------------------------------ev----+
l1_fpc5_ratehalf_m4_t2_sharp_six_value_rational_map
  [PROVED] --------------------------------------------------ev----+
l1_fpc5_ratehalf_m4_t2_sharp_fixed_agreement_shortening
  [PROVED] --------------------------------------------------ev----+
l1_fpc5_ratehalf_m4_t2_uniform_guarded_codimension
  [PROVED] --------------------------------------------------ev----+
l1_fpc5_ratehalf_m4_t2_joint_support_distance
  [PROVED] --------------------------------------------------ev----+
l1_fpc5_ratehalf_m4_t2_distance_only_no_go
  [PROVED] --------------------------------------------------ev----+
                                                                    v
  l1_fpc5_ratehalf_m4_t2_payment [TARGET]
    --req--> l1_fpc5_m4_t2_payment [CONDITIONAL]
```
