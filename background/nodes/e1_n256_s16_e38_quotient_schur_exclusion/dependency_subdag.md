# Dependency sub-DAG

```text
e1_n256_s16_sparse_l1_variance_exclusion [PROVED] --------+
e1_n256_s16_autocorrelation_subfield_exclusion [PROVED] --+--req-->
collision_norm_criterion [PROVED] ------------------------+
    e1_n256_s16_e38_quotient_schur_exclusion [PROVED]

e1_n256_s16_e38_quotient_schur_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This closes the variance-76 slice of the profile-`(3,4,0)` branch. The lower
positive even variances remain downstream work.
