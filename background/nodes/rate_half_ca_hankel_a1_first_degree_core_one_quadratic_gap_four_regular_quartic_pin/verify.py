#!/usr/bin/env python3
"""Replay regular-factor and marked-determinant degrees."""


E = 183_251_937_963
RHO = 3 * E - 1
D = RHO - 1
regular = E - 2
loss = E - 6
assert regular - loss == 4

# Double-root marked determinant.
assert 4 + 3 * loss + 6 * 2 == D

# Two-simple marked determinants.
g1 = (E - 3) // 2
g2 = (E - 9) // 2
assert g1 + g2 == loss
assert 4 + 5 * g1 + g2 + 6 * 1 == D
assert 4 + g1 + 5 * g2 + 6 * 3 == D

print(
    "QUADRATIC_GAP_FOUR_REGULAR_QUARTIC_PIN_PASS",
    f"regular_degree={regular}",
    "residual_degree=4",
)
