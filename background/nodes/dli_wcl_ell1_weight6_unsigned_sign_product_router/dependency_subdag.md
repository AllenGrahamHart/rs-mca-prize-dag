# Dependency sub-DAG

```text
dli_wcl_ell1_weight6_even_norm_divisor_descent [PROVED] --ev--+
                                                               |
dli_wcl_ell1_weight6_unsigned_sign_product_router [PROVED] --ev-+
                                                               v
                              dli_wcl_slot_1_6_emptiness [TARGET]
                                        --> dli_wcl_zone_coverage [CONDITIONAL]
```

The two suppliers are independent views of the same slot. The norm-divisor
descent compresses by coefficient geometry; this router aggregates sign
lifts before norm arithmetic. Neither is a requirement because neither
excludes the compatible finite characteristics.
