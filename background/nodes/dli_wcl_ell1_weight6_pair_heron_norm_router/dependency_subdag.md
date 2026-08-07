# Dependency sub-DAG

```text
dli_wcl_ell1_weight6_unsigned_sign_product_router [PROVED]
  --> dli_wcl_ell1_weight6_pair_heron_norm_router [PROVED]
       --ev--> dli_wcl_slot_1_6_emptiness [TARGET]
                --> dli_wcl_zone_coverage [CONDITIONAL]
```

The child factors the exact supplier polynomial but does not classify its
finite-characteristic zeros. Its target edge is evidence, not a requirement.
