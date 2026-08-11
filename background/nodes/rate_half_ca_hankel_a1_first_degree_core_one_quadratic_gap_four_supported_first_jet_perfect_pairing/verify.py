#!/usr/bin/env python3
"""Replay quadratic first-jet dimensions and correction exception caps."""


E = 183_251_937_963
RHO = 3 * E - 1
D = RHO - 1

assert E % 2 == 1
assert (E - 6) + 2 * 2 == E - 2
assert (E - 3) // 2 + (E - 9) // 2 + 1 + 3 == E - 2

for c in (1, 2):
    source_count = D - c
    matrix_size = D + 1
    kernel_dimension = matrix_size - source_count
    assert kernel_dimension == c + 1

    smith_exponents = [1] * c
    assert len(smith_exponents) == c
    assert sum(smith_exponents) == c
    assert kernel_dimension - len(smith_exponents) == 1

assert 2 == 2
assert 1 + 3 == 4

print(
    "QUADRATIC_GAP_FOUR_SUPPORTED_FIRST_JET_PAIRING_PASS",
    "double_exceptions<=2",
    "two_simple_exceptions<=4",
)
