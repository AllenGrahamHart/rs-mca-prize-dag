# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node refines one exhaustive leaf of the trace router. It creates no
conditional and leaves the active-trace leaf unchanged.
