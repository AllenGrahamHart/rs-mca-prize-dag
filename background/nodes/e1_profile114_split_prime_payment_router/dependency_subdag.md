# Dependency sub-DAG

```text
e1_profile210_exact_weighted_payment [PROVED] ----------------req--> e1_profile114_split_prime_payment_router [PROVED]
e1_profile210_split_prime_ideal_router [PROVED] ---------------req-->
e1_profile210_m1538_collision_exclusion [PROVED] --------------req-->
e1_profile210_m1028_energy2_log_exclusion [PROVED] ------------req-->
e1_profile210_m1028_energy3_modular_norm_exclusion [PROVED] ---req-->
e1_profile210_m1028_energy56_log_exclusion [PROVED] -----------req-->
e1_low_square_mass_weighted_kernel_dictionary [PROVED] -------req-->

e1_profile114_split_prime_payment_router [PROVED] --ev--> e1_official_low_square_mass_pair_budget [TARGET]
```

The pending energy-four certificate is not represented as a proved
requirement. Its emptiness is the explicit payment trigger in this node.
