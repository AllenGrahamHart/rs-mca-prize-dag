#!/usr/bin/env python3
"""Replay the two-simple degree and deficit-spread arithmetic."""


E = 183_251_937_963
RHO = 3 * E - 1
T = RHO + 4

d1 = (E - 3) // 2
d2 = (E - 9) // 2
assert E % 2 == 1
assert d1 + d2 == E - 6
assert T + (3 * RHO + 5) * E + d1 + d2 == T * RHO
assert 1 + (3 * RHO + 5) + 2 + (RHO - 8) == 4 * RHO

for pair_deficit in range(5):
    cap = RHO + 1 - pair_deficit
    assert T - cap == 3 + pair_deficit

print(
    "QUADRATIC_GAP_FOUR_TWO_SIMPLE_CENTER_SPREAD_PASS",
    f"degrees={d1},{d2}",
    "triple_expanders=3..7",
)
