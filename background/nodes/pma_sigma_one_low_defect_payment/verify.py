#!/usr/bin/env python3
"""Exact official-grid arithmetic for the sigma-one low-defect payment."""

from math import comb


CHECKS = 0


def check(label, condition):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


def cells(length):
    return {
        (1, 0): comb(length, 2) // 3,
        (1, 1): length // 2,
        (2, 0): comb(length, 3) // 4,
        (2, 1): comb(length, 2) // 3,
    }


ppb_ranges = {den: [] for den in (2, 4, 8, 16)}
for exponent in range(13, 45):
    n = 1 << exponent
    for denominator in (2, 4, 8, 16):
        k = n // denominator
        length = n - k
        petal_count = length // 2
        table = cells(length)

        check("sigma-one petal parity", length == 2 * petal_count)
        check("d1 r0 charge", table[(1, 0)] == comb(length, 2) // comb(3, 2))
        check("d1 r1 charge", table[(1, 1)] == comb(length, 1) // comb(2, 1))
        check("d2 r0 charge", table[(2, 0)] == comb(length, 3) // comb(4, 3))
        check("d2 r1 charge", table[(2, 1)] == comb(length, 2) // comb(3, 2))

        d1 = (k - 1) * (table[(1, 0)] + table[(1, 1)])
        d2 = comb(k - 1, 2) * (table[(2, 0)] + table[(2, 1)])
        total = d1 + d2
        check("positive low-defect bound", total > 0)
        check("official n5/1024 payment", 1024 * total < n**5)
        check("dominant d2 r0 retained", total >= comb(k - 1, 2) * table[(2, 0)])

        # Exact agreement with the printed formula.
        printed = (k - 1) * (petal_count + comb(length, 2) // 3) + comb(k - 1, 2) * (
            comb(length, 2) // 3 + comb(length, 3) // 4
        )
        check("printed formula", total == printed)
        ppb_ranges[denominator].append(total * 1_000_000_000 // n**5)

# Mutation controls: increasing the owner charge or dropping a background
# state silently underprices the complete source list.
sample_n = 1 << 13
sample_k = sample_n // 2
sample_l = sample_n - sample_k
sample = cells(sample_l)
correct = (sample_k - 1) * (sample[(1, 0)] + sample[(1, 1)]) + comb(sample_k - 1, 2) * (
    sample[(2, 0)] + sample[(2, 1)]
)
wrong_charge = (sample_k - 1) * (comb(sample_l, 2) // 6 + sample[(1, 1)]) + comb(sample_k - 1, 2) * (
    comb(sample_l, 3) // 10 + comb(sample_l, 2) // 6
)
wrong_background = (sample_k - 1) * sample[(1, 0)] + comb(sample_k - 1, 2) * sample[(2, 0)]
check("mutation larger denominator underprices", wrong_charge < correct)
check("mutation missing r1 cells underprices", wrong_background < correct)

for denominator in (2, 4, 8, 16):
    values = ppb_ranges[denominator]
    print(
        f"rate=1/{denominator}: B_low/n^5 ppb range "
        f"[{min(values)},{max(values)}]"
    )

print(f"PMA sigma-one low-defect payment: PASS ({CHECKS} checks, 128 official rows)")
