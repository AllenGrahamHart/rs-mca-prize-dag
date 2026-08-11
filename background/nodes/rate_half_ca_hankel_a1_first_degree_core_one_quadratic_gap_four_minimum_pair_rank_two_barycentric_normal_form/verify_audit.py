#!/usr/bin/env python3
"""Independent integer audit of the rank-two root-union ledger."""


def ceil_div(a, b):
    return -((-a) // b)


for e in (7, 11, 101, 183251937963):
    rho = 3 * e - 1
    for r in range(3):
        m = r + 3
        g = max(1, ceil_div(r * e - 3, r + 2))
        assert g + m * (e - g) <= 3 * e + 3
        assert 3 * (g + 1) <= rho + 3

print("RATE_HALF_QUADRATIC_MINIMUM_PAIR_RANK_TWO_NORMAL_FORM_AUDIT_PASS")
