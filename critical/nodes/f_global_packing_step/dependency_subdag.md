# Dependency sub-DAG

```text
f_spread_moment_count [PROVED] -----------ev--+
f_spread_descent_dichotomy [PROVED] ------ev--+
f_descent_termination [PROVED] -----------ev--+--> f_global_packing_step [TARGET]
f_scale_recursion [PROVED] ---------------ev--+
f_prize_consumer_flat_scope [TARGET] --------ev-+

f_global_packing_step [TARGET]
  --req--> f_dim_induction [CONDITIONAL]
```

The inputs identify all local terms. They do not prove the absolute-exponent
sum, which is the content of this leaf.
