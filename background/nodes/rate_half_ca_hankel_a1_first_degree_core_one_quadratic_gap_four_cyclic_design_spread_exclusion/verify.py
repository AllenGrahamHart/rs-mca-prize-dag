#!/usr/bin/env python3
"""Verify the cyclic-window spread exclusion and bounded toy replays."""


def marked_starts(e):
    block_count = 3 * e + 3
    return {
        j
        for j in range(block_count)
        if ((j + 1) * 7) // block_count > (j * 7) // block_count
    }


def find_pair(e):
    block_count = 3 * e + 3
    marked = marked_starts(e)
    deficient = []
    for t in range(block_count):
        window = {(t - i) % block_count for i in range(e)}
        if len(window & marked) == 3:
            deficient.append(t)
    assert len(deficient) == e - 6
    return next(t for t in deficient if (t + 1) % block_count not in marked)


for exponent in range(14, 61):
    t = find_pair(exponent)
    block_count = 3 * exponent + 3
    marked = marked_starts(exponent)
    left = {(t - i) % block_count for i in range(exponent)}
    right = {((t + 1) - i) % block_count for i in range(exponent)}
    pair_window = left | right
    assert len(pair_window) == exponent + 1
    assert len(pair_window & marked) == 3
    disjoint = 0
    for k in range(block_count):
        third = {(k - i) % block_count for i in range(exponent)}
        disjoint += third.isdisjoint(pair_window)
    assert disjoint == exponent + 3
    rho = 3 * exponent - 1
    required = (rho + 7 + 1) // 2
    assert required > exponent + 3

official_e = 183251937963
official_rho = 3 * official_e - 1
assert official_e - 6 > 7
assert (official_rho + 7 + 1) // 2 > official_e + 3

print(
    "QUADRATIC_GAP_FOUR_CYCLIC_DESIGN_SPREAD_EXCLUSION_PASS",
    f"official_e={official_e}",
    f"cyclic_expanders={official_e + 3}",
)
