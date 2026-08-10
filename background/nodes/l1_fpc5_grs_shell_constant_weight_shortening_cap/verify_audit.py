#!/usr/bin/env python3
"""Independent direct-binomial audit of the shortening formula."""

from math import comb


def direct(length: int, weight: int, distance_half: int, depth: int) -> int:
    residual = weight - depth
    if residual < distance_half:
        base = 1
    else:
        denominator = residual**2 - (length - depth) * (
            residual - distance_half
        )
        assert denominator > 0
        base = (length - depth) * distance_half // denominator
    return comb(length, depth) * base // comb(weight, depth)


def main() -> None:
    rows = (
        (511, 248, 127, 4, 5402),
        (511, 225, 125, 4, 10127),
        (511, 224, 125, 4, 7396),
        (511, 223, 125, 3, 5492),
        (511, 222, 125, 3, 3723),
        (511, 221, 125, 3, 2815),
        (511, 220, 125, 2, 1839),
        (511, 219, 125, 2, 1326),
    )
    for length, weight, distance_half, depth, expected in rows:
        assert direct(length, weight, distance_half, depth) == expected
        if depth:
            residual = weight - (depth - 1)
            previous = residual**2 - (length - depth + 1) * (
                residual - distance_half
            )
            assert previous <= 0 or direct(
                length, weight, distance_half, depth - 1
            ) >= expected

    print(
        "L1_FPC5_GRS_SHELL_CONSTANT_WEIGHT_SHORTENING_CAP_AUDIT_PASS "
        "direct_rows=8"
    )


if __name__ == "__main__":
    main()
