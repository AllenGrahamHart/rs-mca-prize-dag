# Dependency sub-DAG

```text
xr_higher_rank_uniform_split_pencil_reduction [PROVED] --\
xr_trade_circuit_arity_segre_atlas [PROVED] ------------+
xr_higher_rank_rank_two_shell_maxwell_router [PROVED] ---+-> xr_rank_two_proper_circuit_defect_host_router [PROVED]
xr_rank_two_maxwell_collision_defect_identity [PROVED] --/                         |
                                                                                   v
                                                                 xr_highcore_collision_count [TARGET]
```

Minimal-core proper-subset density supplies the positive deficit sign. The
collision identity converts it to a defect lower bound; the shell router
supplies the parity-sensitive zero-mass floor; the circuit atlas restricts
the proper rank-two templates to four and five blocks.
