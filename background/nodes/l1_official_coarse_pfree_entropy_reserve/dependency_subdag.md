# Dependency sub-DAG

```text
l1_official_reserve_tame_refinement_router [PROVED] ----\
l1_official_newton_cofactor_window_router [PROVED] ------+--> l1_official_coarse_pfree_entropy_reserve [PROVED]
l1_official_frobenius_checkpoint_q_router [PROVED] ------/                         |
                                                                                   +--ev--> l1_mixed_petal_amplification [TARGET]
```

The node calibrates only the checkpoint-depth ambient average. The consumer
still owes the max-to-average and collective Pade-section estimates.
