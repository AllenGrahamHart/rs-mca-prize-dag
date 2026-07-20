# Dependency sub-DAG - L1 marked constant-shift sub-two-ell exclusion

```text
l1_bounded_polarity_marked_full_pencil_reduction [PROVED] --\
                                                               +--> l1_marked_constant_shift_subtwoell_exclusion [PROVED]
pma_coset_subtwoell_saturation_exclusion [PROVED] -------------/                         |
                                                                                         +--ev--> l1_mixed_residual_intersection_pin [PROVED]
                                                                                         +--ev--> l1_mixed_petal_amplification [TARGET]
                                                                                         +--ev--> petal_mixed_amplification [TARGET]
```

The result closes a strict marked subbranch and terminates. It creates no new
predicate.
