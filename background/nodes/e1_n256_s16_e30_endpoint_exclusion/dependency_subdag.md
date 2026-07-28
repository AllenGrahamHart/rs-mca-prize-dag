# Dependency sub-DAG

```text
e1_n256_s16_e30_profile_parity_light_reduction (PROVED) ---+
e1_n256_s16_e30_three_profile_quotient_exclusion (PROVED) -+
e1_n256_s16_e30_two_odd_profile_exclusion (PROVED) --------+
e1_n256_s16_e30_profile_422_exclusion (PROVED) ------------+--> E30 endpoint
e1_n256_s16_e30_profile_541_exclusion (PROVED) ------------+    exclusion (PROVED)
e1_n256_s16_e30_profile_66_exclusion (PROVED) -------------+
```

The endpoint node is only the exhaustive synthesis. All computation remains
in its exclusion dependencies. It supplies evidence to
`e1_official_prime_exception_control` and
`unsafe_crossing_family_instantiation`.
