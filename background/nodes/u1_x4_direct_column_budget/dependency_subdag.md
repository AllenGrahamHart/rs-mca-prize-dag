# Dependency sub-DAG

```text
f3_h1_singleton_injectivity [PROVED] ----------------+
f3_h2_stratum_theorem [PROVED] ----------------------+
f3_h3_direct_floor_conditional_close [CONDITIONAL] --+--> u1_x4_direct_column_budget [CONDITIONAL]
f3_hge4_aggregate_budget [CONDITIONAL] --------------+

u1_x4_direct_column_budget [CONDITIONAL] --ev--> x4_primitive_star_u1_coverage [TARGET]
x4_primitive_star_u1_coverage [TARGET] ----req--> x4_exactlist_staircase_split [CONDITIONAL]
```

The first block proves only the F-4 minimal-record budget.  It is evidence for
one route to the direct local primitive-column target.  The exact-list
consumer requires that target, not `u1` itself.
