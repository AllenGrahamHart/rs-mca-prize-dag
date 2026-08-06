# Dependency sub-DAG

```text
dli_wcl_newton_short_window_exclusion [PROVED] --------+
f2_weighted_kernel_collision_floor [PROVED] -----------+
                                                        v
f2_minus_branch_coupled_negacyclic_reduction [PROVED]
                                                        |
                                                        v evidence
f2_conditional_close [TARGET]
```

The node replaces the refuted bounded-class route on `p=3 mod 4`; it does
not replace the still-open mass upper bound.
