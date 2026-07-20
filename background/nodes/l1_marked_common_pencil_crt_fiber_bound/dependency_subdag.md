# Dependency sub-DAG - L1 marked common-pencil CRT fiber bound

```text
l1_marked_constant_shift_forney_window_normal_form [PROVED] --\
                                                                  +--> l1_marked_common_pencil_crt_fiber_bound [PROVED]
l1_bounded_polarity_marked_full_pencil_reduction [PROVED] --------/                         |
                                                                                            +--ev--> l1_mixed_residual_intersection_pin [PROVED]
                                                                                            +--ev--> l1_mixed_petal_amplification [TARGET]
                                                                                            +--ev--> petal_mixed_amplification [TARGET]
```

The result isolates locator counting as the remaining common-pencil
obligation and creates no new predicate.
