#!/usr/bin/env python3
"""Replay the exact incidence and center-line arithmetic."""


E = 183_251_937_963
RHO = 3 * E - 1
N = 4 * RHO
T = RHO + 4

light = 3 * RHO + 5
active_heavy_degree = E - 6
inactive_heavy = RHO - 7

assert 1 + light + 1 + inactive_heavy == N
assert T + light * E + active_heavy_degree == T * RHO

# (h-1)(rho+1) <= h*rho is equivalent to h <= rho+1.
assert (RHO + 1 - 1) * (RHO + 1) <= (RHO + 1) * RHO
assert (RHO + 2 - 1) * (RHO + 1) > (RHO + 2) * RHO
assert T - (RHO + 1) == 3
for deficient in (0, 1, 2):
    cap = RHO + 1 - deficient
    assert T - cap == 3 + deficient

print(
    "QUADRATIC_GAP_FOUR_INCIDENCE_CENTER_SPREAD_PASS",
    f"rho={RHO}",
    f"light={light}",
    "triple_expanders=3,4,5",
)
