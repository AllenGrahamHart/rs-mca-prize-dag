# Dependency sub-DAG

```text
xr_higher_rank_uniform_split_pencil_reduction [PROVED] --\
xr_rank_two_three_anchor_grs3_factorization [PROVED] ----+
xr_rank_two_four_anchor_quadric_centroid_atlas [PROVED] -+
                                                          v
xr_rank_two_received_pair_alternating_router [PROVED]
                                                          |
                                                          v
xr_highcore_collision_count [TARGET]
```

The uniform parent supplies the actual agreement equation. The two branch
parents supply complete coefficient spans. The result routes their necessary
received-pair interactions but does not supply all block parity checks.
