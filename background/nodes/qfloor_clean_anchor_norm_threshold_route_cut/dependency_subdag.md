# Dependency sub-DAG

```text
qfloor_exact [PROVED]
    --req--> qfloor_clean_anchor_norm_threshold_route_cut [PROVED]

qfloor_clean_anchor_norm_threshold_route_cut [PROVED]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The evidence edge prevents an out-of-scope qfloor invocation. It does not
discharge the unsafe payload target.
