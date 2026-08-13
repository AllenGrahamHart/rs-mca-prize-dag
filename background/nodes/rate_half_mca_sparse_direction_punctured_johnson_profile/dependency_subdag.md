# Dependency sub-DAG

```text
rate_half_mca_sparse_direction_punctured_list_payment (PROVED)
       |
rate_half_mca_sparse_direction_heavy_fiber_profile (PROVED)
       |
rate_half_mca_sparse_direction_punctured_johnson_profile (PROVED)
       |
rate_half_band_crossing_location (TARGET, evidence only)
```

The new node replaces only the ordinary-list cardinality estimate in the
existing sparse-direction profile.  It does not consume the refuted affine
incident-basis denominator.
