# Dependency sub-DAG

```text
rate_half_ca_hankel_minimal_index_budget [PROVED]
  --req--> rate_half_ca_hankel_endpoint_rational_normal_kernel_curve [PROVED]

rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]
  --req--> rate_half_ca_hankel_endpoint_rational_normal_kernel_curve [PROVED]

rate_half_ca_hankel_endpoint_rational_normal_kernel_curve [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The node exposes the exact projective geometry of the full endpoint kernel
family.  It does not promote the critical target.
