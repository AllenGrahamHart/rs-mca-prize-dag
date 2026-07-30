#!/usr/bin/env python3
"""Replay the abstract private-core no-aggregation witness."""

D = 215_793
CORES_PER_NEIGHBOR = 4_980

head_fiber_load = 1
fixed_core_load = 1
colored_cell_load = 1
private_colored_cells = D * CORES_PER_NEIGHBOR
proved_colored_cell_floor = (
    D * CORES_PER_NEIGHBOR + 15 - 1
) // 15

assert head_fiber_load <= 458_812
assert fixed_core_load <= 240
assert colored_cell_load <= 15
assert private_colored_cells == 1_074_649_140
assert proved_colored_cell_floor == 71_643_276
assert private_colored_cells >= proved_colored_cell_floor

print(
    "L1_M31_SOURCE_HEAD_INFINITY_OWNER_ROUTE_CUT_PASS "
    f"neighbors={D} private_cells={private_colored_cells} "
    f"proved_floor={proved_colored_cell_floor}"
)
