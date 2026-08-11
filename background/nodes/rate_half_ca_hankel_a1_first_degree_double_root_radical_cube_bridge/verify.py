#!/usr/bin/env python3
"""Replay the residual-exponent arithmetic in the radical cube bridge."""


def complement(multiplicities):
    return tuple(3 - z for z in multiplicities)


assert complement((1, 2)) == (2, 1)
assert complement((2,)) == (1,)
assert complement((1, 1, 1)) == (2, 2, 2)
assert complement((3,)) == (0,)

# Divisor subtractions from the proved local normal forms.
# Cubic no-ordinary: (V_s+V_d)-D = A.
assert (1 + 1) - 1 == 1
# Quadratic double: (R+3B)-(R+2B) = B.
assert 3 - 2 == 1

print("DOUBLE_ROOT_RADICAL_CUBE_BRIDGE_PASS cases=2")
