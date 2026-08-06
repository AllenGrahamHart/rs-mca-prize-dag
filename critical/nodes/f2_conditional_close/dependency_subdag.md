# Dependency sub-DAG

```text
proved empty/edge/dictionary/contraction/tails/struct inputs --ev--> f2_conditional_close [TARGET]

f2_admissible_direct_sum_grs_reduction [PROVED] --ev---------+
f2_growing_order_myerson [TARGET, legacy scope] --ev---------+--> f2_conditional_close [TARGET]
f2_all_admissible_o1_mass_bound [REFUTED] --ev route alarm---+

f2_conditional_close [TARGET] --req--> u2c_giant_tnull_dichotomy [CONDITIONAL]
```

The former Myerson requirement is deliberately absent. Its statement may
still support matching sectors, but Round 17 proves it cannot serve as the
sole all-admissible-row premise.
