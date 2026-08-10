# Dependency sub-DAG

```text
l1_fpc5_tpetal_hankel_grs_syndrome_shell [PROVED]
  -> l1_fpc5_grs_shell_constant_weight_shortening_cap [PROVED]
       -ev-> l1_fpc5_large_source_payment [TARGET]
```

The required parent supplies the injective MDS syndrome-shell model. The new
node uses only support complementation, incidence shortening, and the
elementary constant-weight Plotkin-Johnson inequality.
