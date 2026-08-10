#!/usr/bin/env python3
"""Exact square-root replay of the official FPC5 prefilter scale gap."""

from math import isqrt


PREFIXES = ((4, 5, 12), (8, 7, 28), (16, 15, 56))
BOUNDARIES = {
    (4, 13, 3): (472, 9, 911, 406, -33),
    (8, 29, 3): (247, 6, 486, 231, -8),
    (16, 57, 3): (134, 43, 278, 154, 10),
}


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def pf6_survivor(R: int, s: int, M: int, t: int) -> int | None:
    n = 1 << s
    k = n // R
    N = k - 1
    ell, b = divmod((R - 1) * k + 1, M)
    h = t * ell

    lower = (h + 1) // 2
    upper = min(
        ell * (M - 2) - 1,
        N,
        (t - 1) * ell + b,
        (N + (t - 2) * ell + b) // 2,
    )
    if lower > upper or h > N:
        return None

    lower = max(lower, N - isqrt(N * (N - h)))
    if lower > upper:
        return None

    c = (t - 1) * ell
    if lower <= min(upper, c - 1) or b == 0:
        return lower

    A = N + b
    B = -2 * N * (c + b)
    C = N * (c * c + b * h)
    discriminant = B * B - 4 * A * C
    if discriminant < 0:
        return None

    root_floor = isqrt(discriminant)
    joint_lower = ceil_div(-root_floor - B, 2 * A)
    joint_upper = (root_floor - B) // (2 * A)
    lower = max(lower, joint_lower)
    upper = min(upper, joint_upper)
    return lower if lower <= upper else None


def check_pf6(R: int, s: int, M: int, t: int, d: int) -> None:
    n = 1 << s
    k = n // R
    N = k - 1
    ell, b = divmod((R - 1) * k + 1, M)
    h = t * ell
    r = 2 * d - h
    u = d - (t - 1) * ell
    joint = b * d * d + N * u * u - N * b * r
    assert r >= 0
    assert u <= b
    assert 2 * d <= N + (t - 2) * ell + b
    assert d * d <= N * r
    assert u < 0 or b == 0 or joint <= 0
    assert d <= min(ell * (M - 2) - 1, N)


def main() -> None:
    low_t_cells = 0
    high_t_cells = 0
    for R, first, last in PREFIXES:
        for s in range(13, 45):
            k = (1 << s) // R
            for M in range(first, last + 1):
                ell, _ = divmod((R - 1) * k + 1, M)
                assert ell >= k // 4
                for t in (2, 3):
                    assert pf6_survivor(R, s, M, t) is None
                    low_t_cells += 1
                for t in range(4, M + 1):
                    assert t * ell > k - 1
                    high_t_cells += 1

    assert low_t_cells == 4608
    assert high_t_cells == 55296

    for (R, M, t), expected in BOUNDARIES.items():
        d = pf6_survivor(R, 13, M, t)
        assert d == expected[2]
        n = 1 << 13
        k = n // R
        ell, b = divmod((R - 1) * k + 1, M)
        r = 2 * d - t * ell
        u = d - (t - 1) * ell
        assert (ell, b, d, r, u) == expected
        check_pf6(R, 13, M, t, d)

    print(
        "L1_FPC5_OFFICIAL_RATE_PREFILTER_SCALE_GAP_PASS "
        f"low_t_cells={low_t_cells} high_t_cells={high_t_cells} "
        "cutoffs=12,28,56 boundaries=13,29,57"
    )


if __name__ == "__main__":
    main()
