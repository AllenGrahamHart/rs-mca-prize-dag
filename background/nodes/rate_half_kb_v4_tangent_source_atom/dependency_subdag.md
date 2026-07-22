# Dependency sub-DAG

```text
rate_half_mca_sparse_layer_reduction [PROVED]
  --req--> rate_half_kb_v4_tangent_source_atom [PROVED]
               --ev--> rate_half_band_closure [TARGET]
```

The required edge supplies exact translation to a support union of size at
most `n-a`. The outgoing edge is evidence because three owner cells and the
adjacent unsafe half remain unpaid.
