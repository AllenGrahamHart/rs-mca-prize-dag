# Dependency sub-DAG

```text
l1_pade_split_section_support_moment_inversion [PROVED]
                         |
                        req
                         v
l1_interior_bc_floor_higher_shell_q_routing [PROVED]
                         ^
                        req
                         |
l1_exact_shell_balanced_shifted_lattice_reduction [PROVED]
                         |
                         ev
                         v
l1_mixed_petal_amplification [TARGET]
```

The remaining L1 interior object is the guarded exact pencil after support-ray
deletion, not Paper D's raw base-field floor.
