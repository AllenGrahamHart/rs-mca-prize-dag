# Dependency sub-DAG

```text
mca_from_ca_reduction [PROVED]
  --req--> rate_half_unique_decoding_ca_mca_scope_fence [PROVED]
              --ev--> rate_half_band_crossing_location [TARGET]
```

The incoming theorem supplies the exact half-distance hypothesis. The new
node specializes that gate to the live rate-half agreement interval. Its
outgoing edge is evidence because eliminating one proposed transfer route
does not bound the far-CA numerator.
