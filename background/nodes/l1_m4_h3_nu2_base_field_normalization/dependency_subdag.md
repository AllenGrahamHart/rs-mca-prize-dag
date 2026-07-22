# Dependency sub-DAG

```text
l1_m4_h3_nu2_prime_field_belyi_normal_form [PROVED] --+
                                                          |
l1_m4_positive_value_coset_certificate [PROVED] ----------+-- req -->
                                                          |
                 l1_m4_h3_nu2_base_field_normalization [PROVED]
                                                          |
                                                          +-- ev --> l1_mixed_petal_amplification
```

The suppliers normalize the inner polynomial and the positive value triple.
The new node proves that the domain and complement normalize with them. It
supplies evidence to L1 without promoting the target.
