# Dependency sub-DAG

```text
mca_full_agreement_endpoint [PROVED]
  --ev--> rate_half_band_closure [TARGET]

rate_half_cyclic_simple_pole_mca_floor [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

Together these nodes give the two endpoints of the live rate-half agreement
interval; neither locates the interior adjacent crossing.
