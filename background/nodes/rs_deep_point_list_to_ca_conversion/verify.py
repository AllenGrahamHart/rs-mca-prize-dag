#!/usr/bin/env python3
"""Replay the exact integer-numerator deep-point specialization."""


def ceil_div(a: int, b: int) -> int:
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def list_bound(q: int, n: int, k: int, numerator: int) -> int:
    denominator = q - n - k * numerator
    assert denominator > 0
    return ceil_div(numerator * (q - n), denominator)


def main() -> None:
    checks = 0
    for n, k, numerator in ((31, 7, 2), (8191, 99, 1 << 20), (4095, 819, 10**12)):
        q0 = n + k * numerator
        for gap in (1, 2, k, 2 * k * numerator + 1):
            q = q0 + gap
            bound = list_bound(q, n, k, numerator)
            denominator = q - n - k * numerator
            assert (bound - 1) * denominator < numerator * (q - n)
            assert numerator * (q - n) <= bound * denominator
            checks += 1

        # The strict denominator gate is sharp for this algebraic corollary.
        assert q0 - n - k * numerator == 0

    print(f"RS_DEEP_POINT_LIST_TO_CA_CONVERSION_PASS checks={checks}")


if __name__ == "__main__":
    main()
