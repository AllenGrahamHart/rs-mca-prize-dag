# Dependency sub-DAG

```text
rate_half_mca_sparse_layer_reduction [PROVED]
  --ev--> rate_half_band_closure [TARGET]

rate_half_cyclic_rotated_prefix_floor [PROVED]
  --req--> rate_half_cyclic_simple_pole_mca_floor [PROVED]
  --ev----> rate_half_band_closure [TARGET]
```

The split is exact but does not bound either safe-side term, so its edge is
evidence rather than a conditional closure premise.
