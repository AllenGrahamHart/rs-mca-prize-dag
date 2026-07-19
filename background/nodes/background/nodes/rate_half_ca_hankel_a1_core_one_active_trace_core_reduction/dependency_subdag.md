# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_trace_free_exclusion [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_active_trace_core_reduction [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node normalizes the sole surviving active-trace leaf. It creates no
conditional.
