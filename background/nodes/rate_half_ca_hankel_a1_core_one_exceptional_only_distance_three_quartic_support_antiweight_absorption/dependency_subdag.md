# Dependency sub-DAG

```text
quartic_internal_slice_lambda_cube_kernel [PROVED] --+
                                                       +--req--> quartic_support_antiweight_absorption [PROVED]
quartic_support_degree_two_three_subgroup_reduction ---+                         |
  [PROVED]                                                                        +--ev--> rate_half_band_closure [UNPROVED]
```

The support-only antiweight fence is preserved. It is absorbed only for an
exact design carrying the internal-slice quartics and distinct slopes.
