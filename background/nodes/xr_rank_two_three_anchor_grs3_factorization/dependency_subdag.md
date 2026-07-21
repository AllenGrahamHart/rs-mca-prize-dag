# Dependency sub-DAG

```text
xr_higher_rank_uniform_split_pencil_reduction [PROVED] --\
                                                        +
xr_rank_two_fundamental_circuit_owner [PROVED] ---------+
                                                        v
xr_rank_two_three_anchor_grs3_factorization [PROVED]
                                                        |
                                                        v
xr_highcore_collision_count [TARGET]
```

The first parent supplies the polynomial row-space representation. The
second supplies the global Mobius hyperplane when the coefficient rank is
three. The result classifies weights and owner coefficients, but does not
count realized support embeddings.
