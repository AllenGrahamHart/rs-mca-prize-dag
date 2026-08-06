# Dependency sub-DAG

```text
f3_h1_singleton_injectivity [PROVED] ----------------+
f3_h2_stratum_theorem [PROVED] ----------------------+
f3_h3_direct_floor_conditional_close [CONDITIONAL] --+--> u1_x4_direct_column_budget [CONDITIONAL]
f3_hge4_aggregate_budget [CONDITIONAL] --------------+

x4_primitive_star_u1_coverage [TARGET] --------------+
u1_x4_direct_column_budget [CONDITIONAL] ------------+--> x4_exactlist_staircase_split [CONDITIONAL]
```

The first block proves only the F-4 minimal-record budget.  The coverage node
is a separate requirement of the exact-list consumer and supplies the
general-record-to-ledger bridge if such a bridge is true.
