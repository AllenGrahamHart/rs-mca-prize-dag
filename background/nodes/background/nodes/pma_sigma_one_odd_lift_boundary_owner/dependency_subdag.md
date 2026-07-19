# Dependency sub-DAG

```text
petal_g1_layer_maps [PROVED]
  -> pma_sigma_one_odd_lift_boundary_owner [PROVED]

pma_exact_periodic_owner [PROVED] --------------------\
pma_sigma_one_dyadic_near_coset_owner [PROVED] --------+-> combined owner line
pma_sigma_one_odd_lift_boundary_owner [PROVED] --------/

pma_sigma_one_odd_lift_boundary_owner [PROVED]
  -> pma_wide_residual [TARGET, evidence]
```

The parity factorization supplies a global source selector.  The support
injection then converts the selected class into two adjacent scale-two
binomial columns.
