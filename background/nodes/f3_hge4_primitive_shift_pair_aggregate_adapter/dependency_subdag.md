# Dependency sub-DAG

```text
x81_minimal_trade_square_shift [PROVED] ----------------req--+
x82_square_shift_certifier_keys [PROVED] ---------------req--+
x83_uniform_square_shift_obstruction_gate [PROVED] -----req--+
f3_shiftpair_weld [PROVED] -----------------------------req--+--> f3_hge4_primitive_shift_pair_aggregate_adapter [PROVED]
v13_prefix_collision_ledger [PROVED] -------------------req--+                    |
v13_second_moment_shift_pair_identity [PROVED] ---------req--+                    +--ev--> f3_hge4_norm_gate_count [TARGET]
```

