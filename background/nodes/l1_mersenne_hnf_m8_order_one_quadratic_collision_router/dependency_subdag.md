# Dependency sub-DAG

```text
l1_mersenne_hnf_order_one_frobenius_gate [PROVED]
  |                                      
  +------------------------------+       
                                 v       
l1_mersenne_hnf_m8_order_one_conic_reduction [PROVED]
  |                                      
  +------------------------------+       
                                 v       
l1_mersenne_hnf_m8_order_one_quadratic_collision_router [PROVED]
  |
  v (evidence)
l1_mixed_petal_amplification [TARGET]
```
