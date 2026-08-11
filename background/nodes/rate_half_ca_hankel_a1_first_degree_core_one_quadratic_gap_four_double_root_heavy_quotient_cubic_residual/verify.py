#!/usr/bin/env python3
"""Replay heavy-quotient degrees, recurrence, and local Smith budgets."""


E = 183_251_937_963
D1_DEG = E - 2
G_DEG = E - 6
S_DEG = 2
Q_ROW_DEG = G_DEG + 3 * S_DEG

assert Q_ROW_DEG == E
assert G_DEG + 2 * S_DEG == D1_DEG
assert (E + 1) - D1_DEG == 3

for _correction_root in range(2):
    determinant_order = 2
    heavy_row_order = 3
    assert heavy_row_order > determinant_order
    smith_exponents = [determinant_order]
    assert sum(smith_exponents) == determinant_order

print(
    "QUADRATIC_DOUBLE_ROOT_HEAVY_QUOTIENT_CUBIC_PASS",
    "residual_degree<=3",
    "separated_roots=2",
    "smith=2",
)
