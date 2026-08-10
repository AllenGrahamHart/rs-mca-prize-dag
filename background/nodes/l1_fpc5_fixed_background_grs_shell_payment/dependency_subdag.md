# Dependency sub-DAG

```text
l1_fpc5_tpetal_fixed_background_hankel_codimension [PROVED] --req-->
  l1_fpc5_fixed_background_grs_shell_payment [PROVED]
l1_fpc5_tpetal_hankel_grs_syndrome_shell [PROVED] --req-->
  l1_fpc5_fixed_background_grs_shell_payment [PROVED]
l1_fpc5_fixed_background_grs_shell_payment [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
```

The first supplier gives the exact incidence sum over required background
sets. The second gives the per-chart singleton and MDS support cap.
