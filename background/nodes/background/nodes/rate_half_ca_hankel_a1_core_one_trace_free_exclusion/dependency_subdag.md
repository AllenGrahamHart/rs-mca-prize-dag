# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_trace_free_exclusion [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node closes the trace-free leaf. The active-trace leaf remains open and
no conditional is introduced.
