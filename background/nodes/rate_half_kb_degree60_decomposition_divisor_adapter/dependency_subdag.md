# Dependency sub-DAG

```text
rate_half_kb_q6_u2_primitive_subdegree4_route_cut [PROVED]
                 |
                 +--req-->
rate_half_kb_degree60_decomposition_divisor_adapter [PROVED]
                 |
                 +--req-->
rate_half_kb_degree5_decomposition_exclusion [PROVED]
                 |
                 +--req-->
rate_half_kb_decomposition_source_pencil_compiler [PROVED]
                 |
                 +--ev-->
rate_half_band_closure [TARGET]
```

The adapter and degree-five node also directly require the compiler through
separate DAG edges. Every edge into the target is evidence, not a payment.
