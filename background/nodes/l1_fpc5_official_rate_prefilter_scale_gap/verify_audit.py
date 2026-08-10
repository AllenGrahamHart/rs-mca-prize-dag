#!/usr/bin/env python3
"""Independent monotonicity and convexity audit of the scale gap."""


PREFIXES = ((4, 5, 12), (8, 7, 28), (16, 15, 56))
EXPECTED = {(4, 13): 911, (8, 29): 486, (16, 57): 278}


def joint_value(N: int, b: int, h: int, c: int, d: int) -> int:
    u = d - c
    r = 2 * d - h
    return b * d * d + N * u * u - N * b * r


def first_ordinary(N: int, h: int, lower: int, upper: int) -> int | None:
    def feasible(d: int) -> bool:
        return d * d <= N * (2 * d - h)

    if lower > upper or not feasible(upper):
        return None
    while lower < upper:
        middle = (lower + upper) // 2
        if feasible(middle):
            upper = middle
        else:
            lower = middle + 1
    return lower


def audit_survivor(R: int, s: int, M: int, t: int) -> int | None:
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
    lower = first_ordinary(N, h, lower, upper)
    if lower is None:
        return None

    c = (t - 1) * ell
    if lower < c or b == 0:
        return lower

    A = N + b
    vertex_floor = N * (c + b) // A
    vertex_ceiling = (N * (c + b) + A - 1) // A
    candidates = {
        lower,
        upper,
        max(lower, min(upper, vertex_floor)),
        max(lower, min(upper, vertex_ceiling)),
    }
    if min(joint_value(N, b, h, c, d) for d in candidates) > 0:
        return None

    # G is nonincreasing up to the real vertex. Locate the first feasible
    # integer independently of the primary verifier's discriminant interval.
    right = min(upper, vertex_ceiling)
    while lower < right:
        middle = (lower + right) // 2
        if joint_value(N, b, h, c, middle) <= 0:
            right = middle
        else:
            lower = middle + 1
    return lower


def main() -> None:
    cells = 0
    for R, first, last in PREFIXES:
        for s in range(13, 45):
            for M in range(first, last + 1):
                for t in range(2, M + 1):
                    assert audit_survivor(R, s, M, t) is None
                    cells += 1
    assert cells == 59904

    for (R, M), d in EXPECTED.items():
        assert audit_survivor(R, 13, M, 3) == d

    assert audit_survivor(2, 13, 5, 3) == 1506
    print(
        "L1_FPC5_OFFICIAL_RATE_PREFILTER_SCALE_GAP_AUDIT_PASS "
        f"cells={cells} hostile_boundaries=3 rate_half_control=1"
    )


if __name__ == "__main__":
    main()
