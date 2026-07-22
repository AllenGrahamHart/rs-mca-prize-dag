# Dependency sub-DAG

```text
l1_coarse_pfree_wronskian_distance_packing [PROVED] ---req---+
l1_coarse_pfree_tame_tail_distance_upgrade [PROVED] ---req---+--> l1_coarse_pfree_wronskian_neighbor_compiler [PROVED]
                                                                         |
                                                                         +--ev--> l1_mixed_petal_amplification [TARGET]
```

The first supplier provides the nonzero Wronskian and its degree bound. The
second deletes formal collision strata below `tau_p`. This node adds
fixed-tail injectivity, the exact certificate census, and the neighbor sum.
