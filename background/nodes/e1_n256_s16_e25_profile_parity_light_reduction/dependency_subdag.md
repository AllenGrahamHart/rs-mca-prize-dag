# Dependency sub-DAG

```text
e1_n256_s16_e26_endpoint_exclusion (PROVED) --------+
e1_n256_s16_sparse_l1_variance_exclusion (PROVED) --+
e1_n256_s16_signed_chord_collision_gate (PROVED) ---+--> E25 profile/parity/
e1_n256_s16_e27_profile_parity_light_reduction -----+    light reduction
collision_norm_criterion (PROVED) ------------------+
```

The reduction supplies an exhaustive finite router. It excludes no actual
vector and is consumed by the E25 nine-profile exclusion.
