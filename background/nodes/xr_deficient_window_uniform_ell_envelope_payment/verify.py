#!/usr/bin/env python3
"""Verify packed tuple extrema and the uniform higher-ell comparison."""

from itertools import combinations
from math import comb, prod


def partitions(total: int, cap: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    top = min(total, cap, ceiling if ceiling is not None else cap)
    for first in range(top, 0, -1):
        for tail in partitions(total - first, cap, first):
            yield (first,) + tail


def elementary(parts: tuple[int, ...], order: int) -> int:
    return sum(prod(parts[index] for index in choice)
               for choice in combinations(range(len(parts)), order))


def packed(r: int, ell: int, order: int) -> int:
    q, u = divmod(r, ell)
    return (
        comb(q, order) * ell**order
        + comb(q, order - 1) * ell ** (order - 1) * u
    )


checks = 0
for ell in range(1, 7):
    for r in range(1, 25):
        profiles = list(partitions(r, ell))
        for order in range(2, 7):
            assert min(elementary(profile, order) for profile in profiles) == packed(
                r, ell, order
            )
            checks += 1

# Exceeding the cap invalidates the packed minimum.
assert elementary((4, 3, 2), 3) < packed(9, 3, 3)
checks += 1


ROWS = (
    ("1/4,1/8", 2**41, 2**33 + 1, 11, 8_500_560_263),
    ("1/16", 2**41, 2**32 + 1, 10, 4_265_559_234),
)
SAMPLE_ELLS = (1, 2, 3, 8, 64, 1024, 1_000_000, 10_000_000)

for name, n, h, s, endpoint in ROWS:
    budget = (17 * n * n - 25 * (n - 4)) // 25
    for ell in SAMPLE_ELLS:
        x = endpoint - (s - 1) * (ell - 1)
        y = x + (s - 1) * (ell - 1)
        assert y == endpoint

        e = x - 2 * ell - 1
        reference_e = y - 3
        r = h - x + ell
        assert reference_e - e == (s + 1) * (ell - 1)
        assert r - s * ell > 0
        for j in range(s + 1):
            assert (r - j * ell) - (h - y + 1 - j) == (
                (s - j) * (ell - 1)
            )

        numerator = (s + 1) * prod(e - j for j in range(s + 1))
        denominator = 2 * prod(r - j * ell for j in range(s + 1))
        assert numerator <= budget * denominator
        checks += s + 6

    # No-go boundary r=2ell+1 with packed profile (ell,ell,1).
    ell = (h - 4) // 7
    r = 2 * ell + 1
    d = h - r
    x = d + ell
    e = d - ell - 1
    assert 7 * ell <= h - 4 < 7 * (ell + 1)
    assert d >= (2 * h + 3) // 3
    assert d <= h - 2
    assert ell <= 3 * d - 2 * h - 1
    assert e >= 2 * r

    pair_tuples = ell * ell + 2 * ell
    triple_tuples = ell * ell
    pair_num = n ** (s - 1) * comb(e, 2)
    pair_den = pair_tuples * prod(x + j for j in range(2, s + 1))
    triple_num = 3 * n ** (s - 2) * comb(e, 3)
    triple_den = 2 * triple_tuples * prod(x + j for j in range(3, s + 1))

    expected = {
        11: (
            45_181_176_163_178_354_561_043_298,
            371_272_336_285_157_761_266_139_535_266_618,
        ),
        10: (
            77_453_444_237_271_295_453_973_206,
            159_116_714_494_935_354_830_177_169_055_992,
        ),
    }
    assert pair_num // pair_den == expected[s][0] > budget
    assert triple_num // triple_den == expected[s][1] > budget
    assert packed(r, ell, 2) == pair_tuples
    assert packed(r, ell, 3) == triple_tuples
    assert all(packed(r, ell, order) == 0 for order in range(4, s + 2))
    checks += 13

print(
    "XR_DEFICIENT_WINDOW_UNIFORM_ELL_ENVELOPE_PAYMENT_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
