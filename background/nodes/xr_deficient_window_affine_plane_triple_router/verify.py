#!/usr/bin/env python3
"""Verify the affine-plane triple-router official arithmetic."""

from math import prod


ROWS = (
    (
        "1/4", 2**41, 2**33 + 1, 11, 6_840_580_026,
        3_288_278_226_685_641_424_276_252,
        3_288_278_229_440_559_627_968_627,
    ),
    (
        "1/8", 2**41, 2**33 + 1, 11, 6_840_580_026,
        3_288_278_226_685_641_424_276_252,
        3_288_278_229_440_559_627_968_627,
    ),
    (
        "1/16", 2**41, 2**32 + 1, 10, 3_523_371_942,
        3_288_278_224_426_143_341_124_038,
        3_288_278_232_544_748_236_305_545,
    ),
)


def floor_fraction(numerator: int, denominator: int) -> int:
    assert denominator > 0
    return numerator // denominator


checks = 0
for name, n, h, s, first_fail, floor_before, floor_at in ROWS:
    budget = (17 * n * n - 25 * (n - 4)) // 25
    x0 = (2 * h + 3) // 3 + 1

    def numerator(x: int) -> int:
        return 3 * n ** (s - 2) * prod(x - j for j in (3, 4, 5))

    def denominator(x: int) -> int:
        return (
            2
            * (h - x + 1)
            * (h - x)
            * (h - x - 1)
            * prod(x + j for j in range(3, s + 1))
        )

    def ratio_difference(x: int) -> int:
        return (
            (s - 2) * x * x
            + (5 - s) * h * x
            - (3 * s + 6) * x
            + (5 * s - 1) * h
            - 10 * s
            - 16
        )

    def difference_step(x: int) -> int:
        return (
            (s - 2) * (2 * x + 1)
            + (5 - s) * h
            - (3 * s + 6)
        )

    assert ratio_difference(x0) > 0
    assert difference_step(x0) > 0
    assert first_fail <= h - 2
    assert floor_fraction(numerator(first_fail - 1), denominator(first_fail - 1)) == floor_before
    assert floor_fraction(numerator(first_fail), denominator(first_fail)) == floor_at
    assert numerator(first_fail - 1) <= budget * denominator(first_fail - 1)
    assert numerator(first_fail) > budget * denominator(first_fail)
    assert first_fail - 1 >= x0

    # Ordered choices divided by six give the promised distinct-fiber triples.
    r, ell = 19, 5
    assert r > 2 * ell
    assert r * (r - ell) * (r - 2 * ell) % 6 == 0
    assert r * (r - ell) * (r - 2 * ell) // 6 == 399
    checks += 11

print(
    "XR_DEFICIENT_WINDOW_AFFINE_PLANE_TRIPLE_ROUTER_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
