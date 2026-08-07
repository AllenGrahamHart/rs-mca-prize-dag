# Dependency sub-DAG

```text
proved empty/edge/dictionary/contraction/tails/struct inputs --ev--> f2_conditional_close [TARGET]

f2_admissible_direct_sum_grs_reduction [PROVED, plus] --ev---+
f2_growing_order_myerson [TARGET, legacy scope] --ev---------+--> f2_conditional_close [TARGET]
f2_all_admissible_o1_mass_bound [REFUTED] --ev alarm---------+
f2_all_admissible_direct_sum_grs_reduction [REFUTED] --ev----+
f2_weighted_kernel_collision_floor [PROVED] --ev-------------+
f2_minus_branch_coupled_negacyclic_reduction [PROVED] --ev---+
f2_generated_field_ambient_invariance [PROVED] --ev----------+
f2_consumer_guard_depth_reconciliation [PROVED] --ev---------+

f2_conditional_close [TARGET, guarded (C) depth] --ev--> u2c_giant_tnull_dichotomy [CONDITIONAL]
u2c_exact_slice_extras_budget [TARGET] --req--> u2c_giant_tnull_dichotomy [CONDITIONAL]
```

The former Myerson requirement is deliberately absent. Its statement may
still support matching sectors, but Round 17 proves it cannot serve as the
sole all-admissible-row premise. The proved direct-sum supplier is likewise
restricted to `p=1 mod 4`; the second refuted node guards that scope.
The coupled minus-branch supplier repairs the structural model but leaves
its upper-mass terminal open. Ambient invariance is a fixed-depth object
identity. The guard/depth theorem limits the `(C)` F2 terminal to generating
types and sends `(T*)` outside F2. The proved exact-slice route cut now shows
that this is the official `x4` depth at every rate, so the alternate route is
owned explicitly by `u2c_exact_slice_extras_budget`.
