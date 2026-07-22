# Dependency sub-DAG

```text
xr_prize_arbitrary_w_rank_two_dual_plane_support_router [PROVED] --\
xr_rank_two_received_pair_alternating_router [PROVED] ------------+-> xr_prize_arbitrary_w_rank_two_received_pair_router [PROVED]
                                                                                          |
                                                                                          v
                                                                        xr_highcore_collision_count [TARGET]
```

The dual-plane packet supplies arbitrary-`W` support rows. The uniform
interaction router supplies the coefficient calculation, which this node
replays without importing an MDS support factorization.
