#!/usr/bin/env python3
"""Exact arithmetic replay of the top-band binomial-tail collapse."""

from math import ceil, comb


def tail(petals: int, first: int) -> int:
    return sum(comb(petals, t) for t in range(max(first, 0), petals + 1))


def main() -> None:
    rows = 0
    sharp = 0
    for ell in range(1, 65):
        for petals in range(2, 129):
            boundary = ell * (petals - 2)
            for retained in range(ell):
                for extra in (0, 1, ell, 2 * ell + 1):
                    degree = boundary + extra
                    first = ceil((ell + degree - retained) / ell)
                    value = tail(petals, first)
                    if first < petals - 1 or value > petals + 1:
                        raise AssertionError((ell, petals, degree, retained, first, value))
                    if retained == ell - 1 and extra == 0:
                        if first != petals - 1 or value != petals + 1:
                            raise AssertionError((ell, petals, first, value))
                        sharp += 1
                    rows += 1

    # Both strict remainder and top-band endpoint are load-bearing.
    ell, petals = 5, 8
    degree = ell * (petals - 2)
    if ceil((ell + degree - ell) / ell) != petals - 2:
        raise AssertionError("r=ell mutation was not detected")
    if ceil((ell + degree - 1 - (ell - 1)) / ell) != petals - 2:
        raise AssertionError("below-band mutation was not detected")

    for n, k, petals, ell, retained in (
        (64, 32, 8, 4, 1),
        (1024, 256, 128, 6, 0),
        (1 << 41, 1 << 37, 700, 1 << 31, 3),
    ):
        if petals * ell + (k - 1) + retained > n:
            continue
        if petals + 1 > n:
            raise AssertionError((n, k, petals))

    print(
        "PETAL_TOP_BAND_TAIL_COLLAPSE_PASS "
        f"rows={rows} sharp_rows={sharp} b4=1 mutations=2"
    )


if __name__ == "__main__":
    main()
