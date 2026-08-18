# Dependency sub-DAG

```text
rate_half_mca_rank11_heavy_plane_low_margin_segre_ruling_router [PROVED]
  -> rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed [PROVED]
       -> rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router [PROVED]
            -> rate_half_band_crossing_location [TARGET]
```

The current node uses only the immediately preceding seed as a logical
dependency. Its support-collapsed extraction and exact certificate lift are
proved in this packet rather than imported through a common-core theorem
with a narrower range.
