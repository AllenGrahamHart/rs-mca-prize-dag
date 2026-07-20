# Dependency sub-DAG

```text
dli_wcl_newton_short_window_exclusion [PROVED]
  --> dli_wcl_odd_next_boundary_square_divisor_descent [PROVED]
      --> dli_wcl_slot_1_5_emptiness [TARGET]
      --> dli_wcl_slot_2_7_emptiness [TARGET]
          --> dli_wcl_zone_coverage [CONDITIONAL]
```

The proved descent enters both targets as exact evidence. Their promotion
still requires the finite bad-characteristic exclusions.
