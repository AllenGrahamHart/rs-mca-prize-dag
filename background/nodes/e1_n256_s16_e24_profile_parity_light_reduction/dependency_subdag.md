# Dependency sub-DAG

```text
e1_n256_s16_e25_endpoint_exclusion (PROVED) --------+
e1_n256_s16_sparse_l1_variance_exclusion (PROVED) --+
e1_n256_s16_signed_chord_collision_gate (PROVED) ---+--> E24 profile/parity/
e1_n256_s16_e26_profile_parity_light_reduction -----+    light reduction
collision_norm_criterion (PROVED) ------------------+
```

The reduction is an exhaustive finite router.  It excludes no actual vector
and is consumed by the E24 six-profile exclusion.
