# Dependency sub-DAG

```text
acl_count [PROVED] ----------------------------------------req-->
e1_clean_anchor_exact_collision_allowance [PROVED] -------req--> e1_low_square_mass_plotkin_coloring_compiler [PROVED]
e1_collision_square_mass_reparametrization [PROVED] ------req-->
e1_prime_field_l2_norm_collision_radius [PROVED] ----------req-->

e1_low_square_mass_plotkin_coloring_compiler [PROVED] --ev--> e1_official_low_square_mass_collision_coloring [TARGET]
e1_low_square_mass_plotkin_coloring_compiler [PROVED] --ev--> e1_official_low_square_mass_pair_budget [TARGET]
e1_low_square_mass_plotkin_coloring_compiler [PROVED] -req--> e1_low_square_mass_weighted_kernel_dictionary [PROVED]
e1_official_low_square_mass_collision_coloring [TARGET] --ev--> unsafe_crossing_family_instantiation [TARGET]
e1_official_low_square_mass_pair_budget [TARGET] -------ev--> unsafe_crossing_family_instantiation [TARGET]
```

Both edges into TARGETs are evidence-only. Open targets remain logical leaves;
the proved compiler records the consequence without making this alternative
supplier mandatory.
