# frontier: m720_remaining_gate_replay

Closed.

The n=16 calibration rows are already locally replayed by
`m720_small_gate_replay`, and the h=5 n=32 row is locally replayed by
`m720_h5_n32_gate_replay`.

The h=3 large rows are now also proved by `m720_h3_large_gate_replay`, using a
memory-controlled sorted-record exact replay. There is no remaining leaf under
this node.
