# Dependency sub-DAG

```text
x4_exact_slice_f2_guard_route_cut [PROVED] --ev--> u2c_exact_slice_extras_budget [TARGET]

u2c_exact_slice_extras_budget [TARGET] --req--> u2c_giant_tnull_dichotomy [CONDITIONAL]

f2_conditional_close [TARGET, guarded (C) depth] --ev--> u2c_giant_tnull_dichotomy
```

The new target owns the official exact-slice obligation. The guarded F2 target
is retained as a related research lane without being treated as a proof of a
consumer statement outside its guard.
