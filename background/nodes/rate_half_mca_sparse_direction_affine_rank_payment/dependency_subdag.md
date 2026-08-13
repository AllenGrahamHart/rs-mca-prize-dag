# Dependency sub-DAG

```text
codeword-direction gauge rank router [PROVED] ----+
full-code sparse-direction payment [PROVED] ------+--> rank-refined sparse payment [PROVED]
                                                             |
                                                             +--ev--> rate_half_band_crossing_location
```

The first supplier gives the transformed affine rank.  The second supplies
the witness-to-punctured-list injection, refined here to the actual rank.
