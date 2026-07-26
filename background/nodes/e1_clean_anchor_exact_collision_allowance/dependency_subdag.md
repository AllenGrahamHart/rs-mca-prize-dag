# Dependency sub-DAG

```text
acl_count [PROVED]
    --req--> e1_clean_anchor_exact_collision_allowance [PROVED]

qfloor_clean_anchor_norm_threshold_route_cut [PROVED]
    --req--> e1_clean_anchor_exact_collision_allowance [PROVED]

v13_base_field_normalization_guard [PROVED]
    --req--> e1_clean_anchor_exact_collision_allowance [PROVED]

e1_clean_anchor_exact_collision_allowance [PROVED]
    --req--> e1_fullness [CONDITIONAL]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The first input owns the characteristic-zero class theorem. The second owns
the exact six endpoint parameters and records why norm-threshold injectivity is
unavailable. The third supplies the generated-field currency rule. This node
supplies the finite loss conversion and the small-generated-field route cut. The red
official-prime node must still prove its collision-pair bounds, and the
universal unsafe target must still route every admissible row.
