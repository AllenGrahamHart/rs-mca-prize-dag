# Dependency sub-DAG

```text
rate_half_fixed_tail_prefix_floor [PROVED; provenance] --ev--+
                                                               \
rate_half_cyclic_rotated_prefix_floor [PROVED] -----------------+--req-->
  list_adjacency_closing [CONDITIONAL]

rate_half_cyclic_rotated_prefix_floor [PROVED] --ev-->
  rate_half_band_closure [TARGET; MCA/CA only after the list split]
```
