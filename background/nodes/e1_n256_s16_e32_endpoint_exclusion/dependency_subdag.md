# Dependency sub-DAG

```text
e1_n256_s16_e32_profile_parity_diameter_reduction (PROVED)
       |                 |                    |
       v                 v                    v
profile-(0,8)        profile-(3,5,1)      profile-(4,7)
exclusion            exclusion             exact-norm exclusion
       |                 |                    |
       +-----------------+--------------------+
                         v
e1_n256_s16_e32_endpoint_exclusion (PROVED)
                         |
                         +-- ev --> e1_official_prime_exception_control
                         +-- ev --> unsafe_crossing_family_instantiation
```

The endpoint is a finite synthesis node. Lower variance and other swap-profile
branches remain outside this sub-DAG.
