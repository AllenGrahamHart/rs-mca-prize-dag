# Dependency sub-DAG - L1 marked constant-shift extremal kernel normal form

```text
l1_marked_constant_shift_multistrip_exclusion [PROVED] --\
                                                              +--> l1_marked_constant_shift_extremal_kernel_normal_form [PROVED]
pma_saturated_mixed_support_kernel [PROVED] ------------------/                         |
                                                                                       +--ev--> l1_mixed_residual_intersection_pin [PROVED]
                                                                                       +--ev--> l1_mixed_petal_amplification [TARGET]
                                                                                       +--ev--> petal_mixed_amplification [TARGET]
```

The node ends at a proved normal form and sharp family. It creates no
classification conjecture.
