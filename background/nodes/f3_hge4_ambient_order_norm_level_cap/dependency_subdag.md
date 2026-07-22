# Dependency sub-DAG

```text
f3_hge4_exact_ratio_tower_orbit_compiler -------------------+
                                                            |
f3_hge4_cyclotomic_norm_quarter_width_exclusion ------------+
                                                            v
                            f3_hge4_ambient_order_norm_level_cap
                                                            |
                                                            v (evidence)
                                      f3_hge4_norm_gate_count
```

The node reuses the nonzero primitive cyclotomic integer and its Parseval
ceiling, but keeps the official lower bound `p>n^2` when the pair is assigned
to a proper exact-ratio level `m|n`.
