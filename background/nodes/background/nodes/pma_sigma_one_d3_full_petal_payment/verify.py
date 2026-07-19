#!/usr/bin/env python3
"""Verify the sigma-one PMA defect-three full-petal payment."""

from __future__ import annotations

from itertools import product
from math import comb


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


# Abstract occupancy check: five agreements in pair-petals, with a full petal,
# leave at least two further interpolation points outside the selected petal.
for petals in range(3, 8):
    for profile in product(range(3), repeat=petals):
        if sum(profile) < 5 or 2 not in profile:
            continue
        first_full = profile.index(2)
        check(sum(profile) - profile[first_full] >= 3, f"occupancy {profile}")


rows = 0
for denominator in (2, 4, 8, 16):
    for exponent in range(13, 45):
        n = 1 << exponent
        k = n // denominator
        L = n - k
        M = L // 2
        b_full = comb(k - 1, 3) * M * comb(L - 2, 2)
        b_31 = comb(k - 1, 3) * (comb(L, 3) // 4)
        b_low = (
            (k - 1) * (M + comb(L, 2) // 3)
            + comb(k - 1, 2) * (comb(L, 2) // 3 + comb(L, 3) // 4)
        )
        check(b_full * 1536 < n**6, f"full bound rate=1/{denominator}, n={n}")
        check(
            (b_low + b_31 + b_full) * 1024 < n**6,
            f"combined bound rate=1/{denominator}, n={n}",
        )
        rows += 1

print(f"PMA sigma-one d3 full-petal: PASS ({CHECKS} checks, {rows} official rows)")
