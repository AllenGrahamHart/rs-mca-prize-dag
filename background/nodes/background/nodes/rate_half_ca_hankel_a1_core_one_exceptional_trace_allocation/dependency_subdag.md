# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_active_trace_core_reduction [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node eliminates one exceptional allocation and normalizes the remaining
active systems. It creates no conditional.
