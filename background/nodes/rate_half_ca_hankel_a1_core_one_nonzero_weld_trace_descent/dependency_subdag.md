# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_zero_weld_exclusion [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node gives an exhaustive active-trace/factor-descent split. Both leaves
remain open; no conditional is introduced.
