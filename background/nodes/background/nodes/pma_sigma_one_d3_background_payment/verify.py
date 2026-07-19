#!/usr/bin/env python3
"""Exact official-grid replay of the sigma-one d=3,r=1 payment."""

from math import comb


CHECKS = 0


def check(label, condition):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


def low_bound(n, k):
    length = n - k
    return (k - 1) * (length // 2 + comb(length, 2) // 3) + comb(k - 1, 2) * (
        comb(length, 2) // 3 + comb(length, 3) // 4
    )


ppb_ranges = {den: [] for den in (2, 4, 8, 16)}
for exponent in range(13, 45):
    n = 1 << exponent
    for denominator in (2, 4, 8, 16):
        k = n // denominator
        length = n - k
        per_defect = comb(length, 3) // comb(4, 3)
        bound = comb(k - 1, 3) * per_defect
        check("exact pinned charge", per_defect == comb(length, 3) // 4)
        check("d31 n6/9216", 9216 * bound < n**6)
        check("combined n6/8192", 8192 * (bound + low_bound(n, k)) < n**6)
        ppb_ranges[denominator].append(bound * 1_000_000_000 // n**6)

# Mutation: omitting the minimum charge of four destroys the sharp rate-half
# allowance at the first official row.
n = 1 << 13
k = n // 2
length = n - k
wrong = comb(k - 1, 3) * comb(length, 3)
check("mutation missing owner charge rejected", 9216 * wrong >= n**6)

for denominator in (2, 4, 8, 16):
    values = ppb_ranges[denominator]
    print(
        f"rate=1/{denominator}: B_31/n^6 ppb range "
        f"[{min(values)},{max(values)}]"
    )

print(f"PMA sigma-one d3 background: PASS ({CHECKS} checks, 128 official rows)")
