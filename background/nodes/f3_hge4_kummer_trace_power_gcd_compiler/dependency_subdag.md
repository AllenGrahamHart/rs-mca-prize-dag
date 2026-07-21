# Dependency sub-DAG

```text
f3_hge4_kummer_midpoint_trace_power_gate [PROVED]
                         |
                        req
                         |
                         v
f3_hge4_kummer_trace_power_gcd_compiler [PROVED]
                         |
                        ev
                         |
                         v
f3_hge4_norm_gate_count [TARGET]
```

The compiler makes the endpoint candidate count exact and cheap. It does not
replace the open map from endpoint traces to primitive pencil orbits.
