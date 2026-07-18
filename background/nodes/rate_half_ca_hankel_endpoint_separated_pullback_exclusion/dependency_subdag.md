# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]
  --req--> rate_half_ca_hankel_endpoint_separated_pullback_exclusion [PROVED]

rate_half_ca_hankel_endpoint_separated_pullback_exclusion [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The node excludes the separated nonlinear-cover route.  It does not promote
the critical target.
