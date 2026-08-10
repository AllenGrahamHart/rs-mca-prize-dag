# Dependency sub-DAG

```text
l1_fpc5_tpetal_cauchy_hankel_kernel [PROVED]
  --req--> l1_fpc5_tpetal_fixed_background_hankel_codimension [PROVED]
    --ev--> l1_fpc5_large_source_payment [TARGET]
```

The incoming theorem supplies the CRT/Hankel dictionary. This node augments
it by the required background zeros and calculates the resulting exact
codimension and incidence ledger.
