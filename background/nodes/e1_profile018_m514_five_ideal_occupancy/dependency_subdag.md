# Dependency sub-DAG

```text
e1_profile018_split_prime_payment_router [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_profile018_galois_norm_occupancy_dictionary [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_profile018_mod257_singleton_completion_no_go [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_s18_m514_hermite_two_profile_exclusion [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_s18_m514_e10_profile61_cubic_exclusion [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_s18_m514_e12_all_unit_parity_cubic_exclusion [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_s18_m514_e11_all_unit_dyadic_cubic_exclusion [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]
e1_profile018_e12_root_parity_screen_no_go [PROVED]
    --ev--> e1_profile018_m514_five_ideal_occupancy [PROVED]

e1_qzeta128_p257_class_orbit_certificate [PROVED]
    --req--> e1_profile018_qzeta128_class_descent_two_ideal_bound [PROVED]
e1_profile018_galois_norm_occupancy_dictionary [PROVED]
    --req--> e1_profile018_qzeta128_class_descent_two_ideal_bound [PROVED]
e1_profile018_qzeta128_class_descent_two_ideal_bound [PROVED]
    --req--> e1_profile018_m514_five_ideal_occupancy [PROVED]

e1_profile018_m514_five_ideal_occupancy [PROVED]
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
```
