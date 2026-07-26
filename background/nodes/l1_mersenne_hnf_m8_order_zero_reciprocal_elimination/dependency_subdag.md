# Dependency sub-DAG

```text
l1_mersenne_next_to_maximal_hypergeometric_normal_form [PROVED]
                              |
                              v
l1_mersenne_hnf_frobenius_reciprocal_gate [PROVED]
                              |
                              v
l1_mersenne_hnf_m8_order_zero_reciprocal_elimination [PROVED]
                              |
                              v  (evidence)
                    l1_mixed_petal_amplification [TARGET]
```

The reciprocal gate supplies the exact bounded coefficient equations. This
node proves their first three equations have no non-prime-field solution at
the four `m=8` characteristics, so no later cyclotomic or inner test is
needed in that chamber.
