# Dependency sub-DAG

```text
l1_fpc5_tpetal_hankel_support_determinantal_system [PROVED]
  --req--> l1_fpc5_tpetal_hankel_grs_syndrome_shell [PROVED]
    --ev--> l1_fpc5_large_source_payment [TARGET]
```

The incoming node supplies the exact support amplitudes, recurrence
equations, and primitive nonvanishing criterion. The upstream syndrome-shell
theorem identifies the resulting weighted moment fiber with a GRS coset.
