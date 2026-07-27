# Dependency sub-DAG

```text
e1_n256_s16_e36_quotient_schur_exclusion [PROVED] --+
e1_n256_s16_sparse_l1_variance_exclusion [PROVED] -+--req-->
collision_norm_criterion [PROVED] -----------------+
    e1_n256_s16_e35_quotient_schur_exclusion [PROVED]

e1_n256_s16_e35_quotient_schur_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This closes the variance-70 slice. Lower positive even variances remain open.
