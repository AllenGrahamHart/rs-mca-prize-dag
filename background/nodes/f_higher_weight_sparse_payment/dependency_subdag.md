# Dependency sub-DAG

```text
f_sparse_rank_split [PROVED] -------------------ev--+
xr_syzygy_flat_transport [PROVED] --------------ev--+--> f_higher_weight_sparse_payment [TARGET]
xr_highcore_collision_count [TARGET] -----------ev--+

f_higher_weight_sparse_payment [TARGET]
  --req--> f_many_sparse_structure [CONDITIONAL]
```

The XR target is route evidence, not a silently assumed theorem. The missing
statement is the aggregate owner-aware payment after transport.
