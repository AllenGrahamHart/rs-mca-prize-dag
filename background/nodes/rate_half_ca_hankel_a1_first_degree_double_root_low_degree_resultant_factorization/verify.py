#!/usr/bin/env python3
"""Replay degree and exponent identities in the low-degree resultant theorem."""


E = 183_251_937_963
RHO = 3 * E - 1

# Core-free cubic.
a3 = RHO + 3
b3 = 3 * RHO + 9
d3 = RHO
t = RHO + 4
assert b3 == 3 * a3
assert b3 * E == d3 * t + 3

# Core-one quadratic.
a2 = RHO + 2
b2 = 3 * RHO + 6
d2 = RHO - 1
assert b2 == 3 * a2
assert b2 * E == d2 * t + 6

# Ordinary cubic: L_0^3 R = H^rho S_+^3 and H=L_0 H_0.
ordinary_l0_exponent = d3 - 3
assert ordinary_l0_exponent >= 0
assert ordinary_l0_exponent + d3 * (t - 1) + 3 * 2 == b3 * E

print(
    "DOUBLE_ROOT_LOW_DEGREE_RESULTANT_FACTORIZATION_PASS",
    f"rho={RHO}",
    "residual_degrees=1,2",
)
