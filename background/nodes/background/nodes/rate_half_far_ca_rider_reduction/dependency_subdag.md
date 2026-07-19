# Dependency sub-DAG

```text
rate_half_mca_sparse_layer_reduction [PROVED]
  --ev--> rate_half_band_closure [TARGET]

rate_half_far_ca_rider_reduction [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The two reductions expose the sparse and far-pair halves independently. The
rider theorem leaves the deficient pair-list count open.
