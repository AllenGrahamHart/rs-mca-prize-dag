# Dependency sub-DAG

```text
haboeck_quadratic_johnson_mca_import [PROVED] ---------req-->
rs_deep_point_list_to_ca_conversion [PROVED] ----------req-->
l1_fpc5_tpetal_hankel_grs_syndrome_shell [PROVED] -----req-->
l1_fpc5_tpetal_fixed_background_hankel_codimension
  [PROVED] --------------------------------------------req-->
l1_fpc5_large_source_exact_prefilter [PROVED] ---------req-->
  l1_fpc5_shifted_johnson_grs_shell_cap [PROVED] ------ev-->
    l1_fpc5_large_source_payment [TARGET]
```

The first four suppliers prove the parametric cap. The exact prefilter is
required only for the official `(PF6)` frontier classification.
