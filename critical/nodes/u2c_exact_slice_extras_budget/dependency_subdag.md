# Dependency sub-DAG

```text
x4_locator_prefix_consumer_scope [PROVED] --------ev--> u2c_exact_slice_extras_budget [TARGET]
x4_exact_slice_f2_guard_route_cut [PROVED] --ev--> u2c_exact_slice_extras_budget [TARGET]
x4_fixed_slice_pfree_fullcube_route_cut [PROVED] --ev--> u2c_exact_slice_extras_budget [TARGET]
x4_exactlist_bucket_currency_ownership [PROVED] --ev--> u2c_exact_slice_extras_budget [TARGET]
b2b_near_tail_bound [PROVED] --------------------ev--> u2c_exact_slice_extras_budget [TARGET]

u2c_exact_slice_extras_budget [TARGET] --req--> x4_exactlist_staircase_split [CONDITIONAL]

u2c_giant_tnull_dichotomy [historical t-null route] --ev--> u2c_exact_slice_extras_budget
f2_conditional_close [TARGET, guarded (C) depth] ----ev--> u2c_exact_slice_extras_budget
```

This target owns the structured moment/null pullback column only. The guarded
F2 and historical t-null targets are retained as possible inputs to a future
strip-aware exchange-compression and expansion proof, not as consumer
substitutes. The primitive prefix residue is owned separately by
`x4_primitive_star_u1_coverage` and `u1_x4_direct_column_budget`.
