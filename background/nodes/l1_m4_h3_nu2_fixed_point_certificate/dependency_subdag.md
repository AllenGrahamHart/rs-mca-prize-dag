# Dependency sub-DAG

```text
l1_m4_h3_nu2_base_field_normalization [PROVED]
                         |
                         +-- req --> l1_m4_h3_nu2_fixed_point_certificate [PROVED]
                                                   |
                                                   +-- ev --> l1_mixed_petal_amplification
```

The supplier descends the complete factorization to `F_p`. The new node uses
Frobenius orbit parity and the product of the fixed fiber to remove the last
domain scalar. It supplies evidence to L1 without promoting the target.
