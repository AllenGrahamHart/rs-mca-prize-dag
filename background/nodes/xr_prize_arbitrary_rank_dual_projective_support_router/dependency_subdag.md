# Dependency sub-DAG

```text
xr_prize_arbitrary_w_trade_circuit_segre_router [PROVED] --------\
xr_prize_arbitrary_w_rank_two_dual_plane_support_router [PROVED]-+-> xr_prize_arbitrary_rank_dual_projective_support_router [PROVED]
xr_prize_arbitrary_w_rank_two_received_pair_router [PROVED] ----/                         |
                                                                                           v
                                                                         xr_highcore_collision_count [TARGET]
```

The coefficient circuit theorem is already arbitrary-rank. The two rank-two
routers provide the support and interaction templates, generalized here from
a projective line to `P^(r-1)`.
