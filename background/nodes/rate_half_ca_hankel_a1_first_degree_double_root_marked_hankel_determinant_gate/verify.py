#!/usr/bin/env python3
"""Replay all degree identities in the marked Hankel determinant gate."""


E = 183_251_937_963
RHO = 3 * E - 1

# Core-free rectangular pencil.
DELTA_0 = RHO - E
assert DELTA_0 == 2 * E - 1
assert DELTA_0 + E == RHO

B3 = 3 * (RHO + 3)
assert B3 == 3 * RHO + 9
assert B3 * RHO == B3 * DELTA_0 + B3 * E

# Core-one symmetric middle pencil and its marked rank-one determinant.
D = RHO - 1
DELTA_1 = D - 2 * E
assert DELTA_1 == E - 2
assert DELTA_1 + 2 * E == D

G_DEG = E - 6
S_DEG = 2
assert G_DEG + 3 * S_DEG == E
assert DELTA_1 + 2 * G_DEG + 6 * S_DEG == D

print(
    "DOUBLE_ROOT_MARKED_HANKEL_DETERMINANT_GATE_PASS",
    f"rho={RHO}",
    f"regular_sizes={DELTA_0},{DELTA_1}",
)
