# Dependency sub-DAG

```text
cleared_lift_quartic_router [PROVED] ------+
sparse_subgroup_norm_router [PROVED] ------+--req--> quartic_boundary_crt_reconstruction [PROVED]
                                                        |
                                                        +--ev--> rate_half_band_closure [UNPROVED]
```

The node adds no conditional premise. It converts the boundary part of the
quartic weld into an exact low-degree CRT gate and certificate.
