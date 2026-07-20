# Dependency sub-DAG

```text
dli_wcl_newton_short_window_exclusion [PROVED]
  --> dli_wcl_ell4_weight9_quartic_divisor_descent [PROVED]
  --> dli_wcl_slot_4_9_emptiness [TARGET]
  --> dli_wcl_zone_coverage [CONDITIONAL]
```

The first edge is required. The descent is an exact evidence edge into the
open slot; promotion requires the missing bad-characteristic certificate.
