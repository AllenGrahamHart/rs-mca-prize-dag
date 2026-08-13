#!/usr/bin/env python3
"""Replay the exact factor-degree arithmetic on the official row."""


def ceil_div(left: int, right: int) -> int:
    return (left + right - 1) // right


def main() -> None:
    e = 183251937963
    assert e % 2 == 1
    p = (3 * e - 1) // 2
    m = e - 2
    n = p - 3
    assert n == (3 * m - 1) // 2

    bounds = {}
    for d_a in (0, 1):
        r = 3 * p - 3 + d_a
        t = 3 * e
        c = 9 - 2 * d_a
        assert 2 * r == 9 * e - c
        assert t * n - r * m == (3 - d_a) * e - 9 + 2 * d_a

        threshold = ceil_div(3 * e, c)
        assert c * (threshold - 1) < 3 * e <= c * threshold
        bounds[d_a] = threshold

    assert bounds == {0: 61083979321, 1: 78536544842}
    print(
        "RATE_HALF_PAIRED_BIFORM_MACRO_FACTOR_PASS "
        "dA0=61083979321 dA1=78536544842"
    )


if __name__ == "__main__":
    main()
