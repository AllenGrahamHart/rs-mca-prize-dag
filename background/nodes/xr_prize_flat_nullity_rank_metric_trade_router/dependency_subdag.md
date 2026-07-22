# Dependency sub-DAG

```text
xr_prize_flat_nullity_maxwell_trade_space_compiler [PROVED]
                              |
                              v
xr_prize_flat_nullity_rank_metric_trade_router [PROVED]
                              |
                              v
             xr_highcore_collision_count [TARGET]
```

The parent supplies the exact core union and a lower bound on trade-space
dimension. This node compresses the two universal slope checks and applies a
rank-metric row-deletion argument.
