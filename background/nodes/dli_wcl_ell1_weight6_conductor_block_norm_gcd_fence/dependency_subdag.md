# Dependency sub-DAG

```text
dli_wcl_ell1_weight6_parity_adapted_heron_descent [PROVED]
  --> dli_wcl_ell1_weight6_conductor_block_norm_gcd_fence [PROVED]
       --ev--> dli_wcl_slot_1_6_emptiness [TARGET]
                --> dli_wcl_zone_coverage [CONDITIONAL]
```

The child gives the exact conductor owner and closes one proposed arithmetic
route negatively. It supplies no compatible-prime exclusion, so the outgoing
edge remains evidence.
