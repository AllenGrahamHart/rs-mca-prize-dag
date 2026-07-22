# Dependency sub-DAG

```text
l1_official_frobenius_checkpoint_q_router [PROVED]
                  |
                  +--req--> l1_coarse_pfree_wronskian_distance_packing [PROVED]
                                            |
                                            +--ev--> l1_mixed_petal_amplification [TARGET]
```

The dependency identifies the official coarse p-free coordinates. The
Wronskian and packing argument itself is valid over every finite field.
