# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_rational_branch_exclusion [PROVED]
  --req--> rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]

rate_half_ca_hankel_endpoint_norm_factorization [PROVED]
  --req--> rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]

rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The node localizes the exact component defects and split fibers.  It does not
promote the critical target.
