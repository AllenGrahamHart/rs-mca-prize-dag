# Dependency sub-DAG

```text
mca_quadratic_prize_rows [PROVED]
  --req--> rate_half_quadratic_exact_range [PROVED]
             --ev--> rate_half_band_closure [TARGET]

rate_half_mca_sparse_layer_reduction [PROVED]
  --req--> rate_half_quadratic_exact_range [PROVED]

rate_half_sparse_pinning_rigidity [PROVED]
  --req--> rate_half_quadratic_exact_range [PROVED]
```

The quadratic dependency proves the exact range and bracket. The sparse
dependencies identify the first post-cutoff candidate as CA-only. The new
node does not satisfy the target's all-fields adjacent-certificate contract.
