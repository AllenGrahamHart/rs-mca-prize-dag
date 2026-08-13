#!/usr/bin/env python3
"""Replay the exact deficit and threshold arithmetic on the official row."""


def ceil_div(left: int, right: int) -> int:
    return (left + right - 1) // right


def least_with_parity(numerator: int, denominator: int, parity: int) -> int:
    value = ceil_div(numerator, denominator)
    if value % 2 != parity:
        value += 1
    return value


def main() -> None:
    e = 183251937963
    assert e % 2 == 1
    p = (3 * e - 1) // 2
    capital_m = e - 2
    capital_n = p - 3
    assert 2 * capital_n - 3 * capital_m == -1

    thresholds = {}
    for d_a in (0, 1):
        q = 9 - 2 * d_a
        r = 3 * p - 3 + d_a
        t = 3 * e
        assert 2 * r == 9 * e - q

        large_odd = least_with_parity(3 * e, q, 1)
        huge_even = least_with_parity(6 * e, q, 0)
        assert q * large_odd >= 3 * e
        assert q * (large_odd - 2) < 3 * e
        assert q * huge_even >= 6 * e
        assert q * (huge_even - 2) < 6 * e
        assert 3 * large_odd > capital_m
        assert 2 * huge_even > capital_m
        assert large_odd + huge_even > capital_m
        thresholds[d_a] = (large_odd, huge_even)

        samples = {
            max(1, large_odd - 2),
            large_odd,
            max(2, huge_even - 2),
            huge_even,
            capital_m,
        }
        for degree in samples:
            n_min = ceil_div(r * degree, t)
            chi = 2 * n_min - 3 * degree
            if degree % 2:
                expected = 1 if q * degree < 3 * e else -1
            else:
                expected = 0 if q * degree < 6 * e else -2
            assert chi == expected

    assert thresholds == {
        0: (61083979321, 122167958642),
        1: (78536544843, 157073089684),
    }
    print(
        "RATE_HALF_PAIRED_BIFORM_FACTOR_TRICHOTOMY_PASS "
        "dA0=(61083979321,122167958642) "
        "dA1=(78536544843,157073089684)"
    )


if __name__ == "__main__":
    main()
