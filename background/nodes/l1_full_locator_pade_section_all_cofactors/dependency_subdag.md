# Dependency sub-DAG

```text
l1_cofactor_prefix_pade_graph_normal_form [PROVED]
                         |
                        req
                         v
l1_full_locator_pade_section_all_cofactors [PROVED]
              |                         |
             req                        ev
              v                         v
l1_pade_remainder_jacobian_     l1_mixed_petal_amplification
tangent_dichotomy [PROVED]                 [TARGET]
```

The all-cofactor node consumes the below-cap graph only for `(FA4)`.  Its
uniform section identity follows directly from reversed polynomial division.
