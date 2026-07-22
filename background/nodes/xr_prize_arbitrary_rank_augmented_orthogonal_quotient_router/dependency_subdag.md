# Dependency sub-DAG

```text
xr_prize_arbitrary_rank_dual_projective_support_router [PROVED] --\
xr_prize_arbitrary_w_rank_two_received_pair_router [PROVED] -------+-> xr_prize_arbitrary_rank_augmented_orthogonal_quotient_router [PROVED]
                                                                                          |
                                                                                          v
                                                                        xr_highcore_collision_count [TARGET]
```

The arbitrary-rank router supplies the projective circuit and pairing
equations. The rank-two interaction router supplies the already audited
orthogonal/perfect-pairing boundary case generalized here by quotienting the
full row space by the augmented-orthogonal kernel.
