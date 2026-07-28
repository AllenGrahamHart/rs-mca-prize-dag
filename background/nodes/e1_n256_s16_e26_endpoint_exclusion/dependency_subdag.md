# Dependency sub-DAG

```text
e1_n256_s16_e26_profile_parity_light_reduction (PROVED) --+
e1_n256_s16_e26_six_two_odd_profile_exclusion (PROVED) ----+--> E26 endpoint
e1_n256_s16_e26_four_six_odd_profile_exclusion (PROVED) ---+    exclusion (PROVED)
```

The endpoint node is only the exhaustive synthesis. All computation remains
in its exclusion dependencies. It supplies evidence to
`e1_official_prime_exception_control` and
`unsafe_crossing_family_instantiation`.
