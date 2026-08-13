#!/usr/bin/env python3
"""Independent arithmetic audit for the Pade-parity quotient fence."""

e = 183251937963
n = 274877906941
total = 824633720830
d = 549755813887
r = 91625968982

assert d == total - n - 2 == 2 * n + 5 == 3 * e - 2
assert 3 * r == n + 5
assert 3 * r - (e + 1) == r
assert n + 1 - r == e - 3 == 183251937960

print(
    "RATE_HALF_SHAPE_A_PADE_PARITY_QUOTIENT_AUDIT_PASS",
    f"algebra={total}",
    f"dual_degree={d}",
    f"mandatory={e + 1}",
    f"quotient={r}",
)
