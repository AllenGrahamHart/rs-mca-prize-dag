# Dependency sub-DAG

```text
rate_half_kb_m12_diagonal_socle_route_cut [PROVED]
                         |
                         +--req--+
                                  |
rate_half_kb_degree5_decomposition_exclusion [PROVED]
                         |        |
                         +--req---+
                                  |
rate_half_kb_m12_secondary_degree5_decomposition_exclusion [PROVED]
                                  |
                                  +--ev--> rate_half_band_closure [TARGET]
```

The first dependency forces the secondary size-five block system; the second
deletes the corresponding inner-degree-five decomposition.
