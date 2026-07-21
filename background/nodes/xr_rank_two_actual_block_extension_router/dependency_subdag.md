# Dependency sub-DAG

```text
xr_rank_two_dual_support_extension_factorization [PROVED] --\
xr_rank_two_received_pair_alternating_router [PROVED] ------+
                                                            v
xr_rank_two_actual_block_extension_router [PROVED]
                                                            |
                                                            v
xr_highcore_collision_count [TARGET]
```

The first parent supplies `R_i,Z_i,T_i`; the second supplies the selected
trade-row parity check. The result decomposes and counts all remaining
per-row block extensions, but leaves family compatibility and ownership at
the target.
