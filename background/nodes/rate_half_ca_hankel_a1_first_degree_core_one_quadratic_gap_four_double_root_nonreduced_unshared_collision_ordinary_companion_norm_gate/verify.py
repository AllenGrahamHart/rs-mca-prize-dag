#!/usr/bin/env python3
"""Replay the ordinary-companion norm degree and order ledger."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


checks = 0
for e in list(range(9, 200, 2)) + [183251937963]:
    p = (3 * e - 1) // 2
    r_rows = 3 * p - 2
    require(2 * r_rows == 9 * e - 7, "classified row count")
    checks += 1

    for m, n, padding_order, correction_order, residual_cap in (
        (2, 3, 1, 1, 7),
        (4, 6, 2, 2, 14),
    ):
        sigma = 3 * e * n - r_rows * m
        require(sigma == 7 * m // 2 == residual_cap, "norm residual cap")
        require(padding_order == m // 2, "heavy-row forced divisor")
        require(correction_order == m // 2, "correction order")
        require(residual_cap - padding_order in (6, 12), "reduced gate cap")
        require(residual_cap < r_rows, "interpolation uniqueness")
        checks += 5

official_e = 183251937963
official_p = (3 * official_e - 1) // 2
official_r = 3 * official_p - 2
require(official_r == 824633720830, "official U_0 size")
checks += 1

print(f"RATE_HALF_COLLISION_ORDINARY_COMPANION_NORM_PASS checks={checks}")
