# Dependency sub-DAG - reciprocal-quadratic PMA obstruction

```text
pma_sigma_one_b11_scope [PROVED] --------------------------+
                                                            |
pma_sigma_one_d3_diffuse_hyperplane_reduction [PROVED] ----+
                                                            v
pma_sigma_one_d3_reciprocal_quadratic_obstruction [PROVED]
                              | req
                              v
              pma_sigma_one_index_two_core_owner [PROVED]
                              | req
                              v
              pma_sigma_one_dyadic_near_coset_owner [PROVED]
                              | req                          | ev
                              v                              v
              petal_mixed_amplification [TARGET]   pma_wide_residual [REFUTED]
```

This theorem is a required route guard for the amber mixed-petal implication:
any proof must account for the explicit family before charging the complement.
The proved owner ladder supplies that payment and then broadens it to every
eligible dyadic coset. The obstruction remains evidence for, not a logical
premise of, the red leaf and does not close that residual.
