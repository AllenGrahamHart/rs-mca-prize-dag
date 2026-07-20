# Dependency sub-DAG - L1 marked constant-shift multistrip exclusion

```text
l1_bounded_polarity_marked_full_pencil_reduction [PROVED] --\
                                                               +--> l1_marked_constant_shift_multistrip_exclusion [PROVED]
pma_coset_subtwoell_saturation_exclusion [PROVED] -------------/                         |
                                                                                         +--ev--> l1_mixed_residual_intersection_pin [PROVED]
                                                                                         +--ev--> l1_mixed_petal_amplification [TARGET]
                                                                                         +--ev--> petal_mixed_amplification [TARGET]
```

This theorem subsumes the first marked strip but does not turn any surviving
cell into a new predicate.
