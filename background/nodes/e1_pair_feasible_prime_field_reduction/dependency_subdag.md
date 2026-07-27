# Dependency sub-DAG

```text
e1_pair_feasible_ambient_generation [PROVED]
    --req--> e1_pair_feasible_prime_field_reduction [PROVED]

e1_pair_feasible_prime_field_reduction [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The reduction validates the prime-field sparse-kernel interface on the live
pair branch. It supplies no collision count.
