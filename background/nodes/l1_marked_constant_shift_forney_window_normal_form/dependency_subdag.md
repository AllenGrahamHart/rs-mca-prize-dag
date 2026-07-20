# Dependency sub-DAG - L1 marked constant-shift Forney-window normal form

```text
l1_marked_constant_shift_multistrip_exclusion [PROVED] --\
                                                              +--> l1_marked_constant_shift_forney_window_normal_form [PROVED]
pma_saturated_mixed_support_kernel [PROVED] ------------------/                         |
                                                                                       +--ev--> l1_mixed_residual_intersection_pin [PROVED]
                                                                                       +--ev--> l1_mixed_petal_amplification [TARGET]
                                                                                       +--ev--> petal_mixed_amplification [TARGET]
```

The normal form subsumes the extremal endpoint but leaves profile ownership
as the existing target's direct obligation.
