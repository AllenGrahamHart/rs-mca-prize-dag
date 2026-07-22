# Dependency sub-DAG

```text
distance_three_pair_lagrange_normal_form [PROVED] --------+
distance_three_external_split_design_saturation [PROVED] -+--req--> cleared_lift_quartic_router [PROVED]
calibrated_conic_kernel_lift_normal_form [PROVED] ---------+                    |
                                                                               +--ev--> rate_half_band_closure [UNPROVED]
```

The node introduces no conditional premise. It replaces an unconstrained
kernel-lift family by an exact degree-four residual-factor problem.
