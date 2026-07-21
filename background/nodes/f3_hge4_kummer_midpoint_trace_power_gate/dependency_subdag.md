# Dependency sub-DAG

```text
f3_hge4_near_third_belyi_necklace_bound [PROVED] ------req--+
                                                               +--> f3_hge4_kummer_midpoint_trace_power_gate [PROVED]
f3_hge4_near_third_kummer_midpoint_pencil [PROVED] -----req--+                  +--req--> f3_hge4_kummer_trace_power_gcd_compiler [PROVED]
                                                                                +--ev---> f3_hge4_norm_gate_count [TARGET]
```

The first dependency supplies the endpoint coefficients; the second turns
midpoint splitting into the exact `m`-th-power condition. The new node is an
evidence edge because it filters candidates without proving their count. The
gcd compiler makes the scalar count exact but does not count pencils.
