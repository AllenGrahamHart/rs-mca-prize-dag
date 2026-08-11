#!/usr/bin/env python3
"""Replay row and marked-determinant factor degrees."""


E = 183_251_937_963
RHO = 3 * E - 1
D = RHO - 1

g1 = (E - 3) // 2
g2 = (E - 9) // 2
s1 = 1
s2 = 3
assert 2 * g1 + 3 * s1 == E
assert 2 * g2 + 3 * s2 == E

regular = E - 2
assert regular + 4 * g1 + 6 * s1 == D
assert regular + 4 * g2 + 6 * s2 == D

print(
    "QUADRATIC_GAP_FOUR_TWO_SIMPLE_MARKED_FACTORIZATION_PASS",
    f"supported_degrees={g1},{g2}",
    f"residual_degrees={s1},{s2}",
)
