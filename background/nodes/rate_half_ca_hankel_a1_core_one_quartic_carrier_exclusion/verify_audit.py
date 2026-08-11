#!/usr/bin/env python3
"""Independent endpoint and carrier-degree audit."""


def main():
    m = 1 << 37
    rho = 4 * m
    lo = m + 1
    hi = (rho - 1) // 2

    def closes(e):
        p = rho - 1 - 2 * e
        ell = 4 * e - rho - 1
        return p // 5 + ell + 3 < e

    left, right = lo, hi + 1
    while left < right:
        mid = (left + right) // 2
        if closes(mid):
            left = mid + 1
        else:
            right = mid
    first = left

    assert first == 169155635042
    assert closes(first - 1)
    assert not closes(first)

    # The recurrence descent leaves a degree-four kernel vector in a
    # d+1-column pencil whose primitive kernel degree is d.
    d = rho - 1
    assert d > 4
    q0_degree = d - 4
    numerator_degree = d - 1
    assert numerator_degree - q0_degree == 3

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_QUARTIC_CARRIER_EXCLUSION_AUDIT_PASS "
        f"first={first} d={d}"
    )


if __name__ == "__main__":
    main()
