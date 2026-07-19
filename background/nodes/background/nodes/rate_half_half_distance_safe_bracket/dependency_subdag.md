# Dependency sub-DAG

```text
mca_from_ca_reduction [PROVED; published CA import tracked]
  --req--> rate_half_half_distance_safe_bracket [PROVED]

rate_half_half_distance_safe_bracket [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The edge to the target is evidence because the bracket narrows the search but
does not prove the adjacent crossing.
