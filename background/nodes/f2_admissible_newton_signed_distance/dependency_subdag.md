# Dependency sub-DAG

```text
dli_wcl_newton_short_window_exclusion [PROVED] --------+
                                                       |
f2_admissible_direct_sum_grs_reduction [PROVED] -------+
                                                       v
f2_admissible_newton_signed_distance [PROVED]
                                                       |
                                                       v evidence
f2_conditional_close [TARGET]
```

The first parent supplies the signed Newton exclusion.  The second supplies
the exact half-system class and the automatic inequality `p>S`.
