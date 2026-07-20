# Dependency sub-DAG

```text
dli_wcl_ell4_weight9_quartic_divisor_descent [PROVED] --+
dli_wcl_odd_next_boundary_square_divisor_descent [PROVED] --+
dli_wcl_ell1_weight6_even_norm_divisor_descent [PROVED] --+
  --> dli_wcl_fixed_divisor_straight_line_lift [PROVED]
      --ev--> dli_wcl_slot_1_5_emptiness [TARGET]
      --ev--> dli_wcl_slot_1_6_emptiness [TARGET]
      --ev--> dli_wcl_slot_2_7_emptiness [TARGET]
      --ev--> dli_wcl_slot_4_9_emptiness [TARGET]
          --req--> dli_wcl_zone_coverage [CONDITIONAL]
```

The lift changes the exact certificate representation. The four red leaves
still require computed integer identities and official bad-characteristic
exclusions.
