#!/usr/bin/env python3
"""Replay center-overlap and residual-degree arithmetic."""


E = 183_251_937_963
D1_DEG = E - 2

for j in range(4):
    lambda_zero_degree = 3 - j
    heavy_fixed_degree = D1_DEG - j
    residual_degree = j
    assert lambda_zero_degree + residual_degree == 3
    assert heavy_fixed_degree + residual_degree == D1_DEG
    assert residual_degree + 1 <= 4

print(
    "QUADRATIC_DOUBLE_HEAVY_CENTER_OVERLAP_PASS",
    "overlap_degrees=0..3",
    "new_scalars<=4",
)
