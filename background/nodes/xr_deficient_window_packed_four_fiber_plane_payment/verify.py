#!/usr/bin/env python3
"""Verify the packed four-fiber geometry and official plane payments."""

from itertools import combinations
from math import prod


def pairings(items: tuple[int, int, int, int]):
    first = items[0]
    for mate in items[1:]:
        left = tuple(sorted((first, mate)))
        right = tuple(sorted(set(items) - set(left)))
        yield tuple(sorted((left, right)))


checks = 0
four_pairings = set(pairings((0, 1, 2, 3)))
assert len(four_pairings) == 3
checks += 1

for t in range(2, 8):
    target_geometries = set()
    for pairing in four_pairings:
        for x, y in combinations(range(t), 2):
            target_geometries.add((pairing, (x, y)))
            target_geometries.add((pairing, (y, x)))
    block_geometries = {
        (fiber_pair, tail)
        for fiber_pair in combinations(range(4), 2)
        for tail in range(t)
    }
    assert len(target_geometries) == 3 * t * (t - 1)
    assert len(block_geometries) == 6 * t
    assert 2 * (9 * t) == 3 * len(block_geometries)
    checks += 3

ROWS = (
    ("1/4,1/8", 2**41, 2**33 + 1, 11),
    ("1/16", 2**41, 2**32 + 1, 10),
)

EXPECTED_CAPS = {
    (11, 2): 333_594_496_688_188_697_227_430,
    (11, 3): 500_391_745_030_230_497_876_741,
    (11, 4): 667_188_993_370_903_933_216_457,
    (11, 5): 833_986_241_710_209_003_246_588,
    (11, 6): 1_000_783_490_048_145_707_967_140,
    (11, 7): 1_167_580_738_384_714_047_378_121,
    (10, 2): 289_152_338_183_910_832_037_167,
    (10, 3): 433_728_507_274_286_589_926_945,
}

for name, n, h, s in ROWS:
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    sigma = d - ell - 1 - 2 * r
    w = d + ell
    assert ell > sigma + 2

    for t in range(2, sigma + 3):
        e = 4 * ell + t
        N = n - e
        owner = 9 * t
        numerator = owner * prod(N - j for j in range(s - 2))
        denominator = prod(w + j for j in range(3, s + 1))
        cap = numerator // denominator
        budget = (17 * n * n - 25 * (n - e)) // 25
        assert cap == EXPECTED_CAPS[(s, t)]
        assert numerator <= budget * denominator
        checks += 3

# Counting complete target geometries loses the decisive block-incidence
# factor when t>2.
t = 5
assert 3 * 2 * len(tuple(combinations(range(t), 2))) == 3 * t * (t - 1)
assert 9 * t < 9 * t * (t - 1)
checks += 2

print(
    "XR_DEFICIENT_WINDOW_PACKED_FOUR_FIBER_PLANE_PAYMENT_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
