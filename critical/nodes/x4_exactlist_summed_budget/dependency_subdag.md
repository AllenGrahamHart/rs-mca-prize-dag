# Dependency sub-DAG

```text
u2c_exact_slice_extras_budget [TARGET] -----------+
x4_primitive_star_u1_coverage [TARGET] -----------+
u1_x4_direct_column_budget [CONDITIONAL] ---------+--inputs--> x4_exactlist_summed_budget [TARGET]
x4_exactlist_bucket_currency_ownership [PROVED] --ev-------+
ww_qa22_currency_separation [PROVED] -------------ev-------+

x4_exactlist_summed_budget [TARGET] --req--> x4_exactlist_staircase_split [CONDITIONAL]
```

The graph uses direct requirements only at the final `x4` assembly. The
component nodes remain independently attackable leaves.
