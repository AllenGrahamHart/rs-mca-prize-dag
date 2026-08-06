# Dependency sub-DAG

```text
xr_radius_arithmetic [PROVED] ---------------------req--+
                                                         +--> x4_exact_slice_f2_guard_route_cut [PROVED]
f2_consumer_guard_depth_reconciliation [PROVED] --req--+

x4_exact_slice_f2_guard_route_cut --ev--> u2c_exact_slice_extras_budget [TARGET]
x4_exact_slice_f2_guard_route_cut --ev--> u2c_giant_tnull_dichotomy [TARGET, background]
```

The first input fixes the exact corridor depth. The second fixes the generated-
field guard and prevents fixed-depth ambient invariance from being used to
recalibrate that depth.
