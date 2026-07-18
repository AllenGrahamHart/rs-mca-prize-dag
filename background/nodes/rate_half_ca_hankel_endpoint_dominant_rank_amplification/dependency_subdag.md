# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_rational_normal_kernel_curve [PROVED]
  --req--> rate_half_ca_hankel_endpoint_dominant_rank_amplification [PROVED]

rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]
  --req--> rate_half_ca_hankel_endpoint_dominant_rank_amplification [PROVED]

rate_half_ca_hankel_endpoint_dominant_rank_amplification [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The node excludes low-separation-rank dominant components.  It does not
promote the critical target.
