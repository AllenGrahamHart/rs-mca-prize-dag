#!/usr/bin/env python3
"""Independent integer feasibility audit for line and off-line incidence."""


def ceil_div(a, b):
    return -((-a) // b)


def bounds(e, j):
    rho = 3 * e - 1
    T = 3 * e + 3
    D = e - 6
    u = rho + j - 1
    numerator = e * u - (j - 2) * T + D
    lower = max(2, ceil_div(numerator, rho - j + 1))
    upper = u // j
    return lower, upper


for e in (7, 13, 127, 1009):
    rho = 3 * e - 1
    first = None
    for j in range(4, rho + 1):
        lower, upper = bounds(e, j)
        if lower <= upper:
            first = j
            break
    assert first == rho // 2 - 1

e = 183251937963
rho = 3 * e - 1
j0 = rho // 2 - 1
assert bounds(e, j0 - 1) == (4, 3)
assert bounds(e, j0) == (3, 3)
assert (3 * e + 3) - 3 == rho + 1

print("RATE_HALF_QUADRATIC_MACROSCOPIC_PAIR_UNION_FLOOR_AUDIT_PASS")
