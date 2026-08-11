# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_saturation_rigidity [PROVED]
                         |
rate_half_fr_canonical_min_pair_union_bound      [PROVED]
                         |
                         v
rate_half_bivariate_deficiency_clone_kernel_reduction [PROVED]
                         |
                         v
rate_half_band_crossing_location                 [TARGET]
```

The canonical-FR node selects the useful joint support. The kernel reduction
itself uses saturation plus the apolar moment identity.
