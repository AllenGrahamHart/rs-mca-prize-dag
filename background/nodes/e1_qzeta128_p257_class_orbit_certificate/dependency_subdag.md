# Dependency sub-DAG

```text
e1_conductor256_full_unit_circular_basis [PROVED] --------req-->
e1_qzeta128_p257_j65_harbater_nonprincipality [PROVED] ------req-->
e1_qzeta128_p257_j63_fixed_field_nonprincipality_certificate [TARGET]
    --req--> e1_qzeta128_p257_two_involution_nonprincipality_certificate [CONDITIONAL]
    --req--> e1_qzeta128_p257_class_orbit_certificate [CONDITIONAL]
    --req--> e1_profile018_qzeta128_class_descent_two_ideal_bound [CONDITIONAL]
```

The published odd-class-number theorem and the Harbater theorem are external
theorem imports. The source evidence for the optional full-coordinate route
is not a dependency.
