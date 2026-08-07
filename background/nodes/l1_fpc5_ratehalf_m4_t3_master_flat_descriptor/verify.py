#!/usr/bin/env python3
"""Exact arithmetic replay for the M=4,t=3 master-flat descriptor."""

from __future__ import annotations


def v2(value: int) -> int:
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def main() -> None:
    checked = 0
    odd_cells = 0
    for log_n in (13, 14):
        n = 1 << log_n
        k = n // 2
        for b in range(7, k + 2):
            if (k + 1 - b) % 4:
                continue
            ell = (k + 1 - b) // 4
            if not 0 <= b < ell:
                continue
            assert n == 8 * ell + 2 * b - 2
            for a in range(1, (b - 3) // 4 + 1):
                johnson = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
                if johnson > 0:
                    continue
                j = 2 * ell - a
                r = ell - 2 * a + 1
                codimension = j - r
                assert codimension == ell + a - 1
                assert j - 2 * r == 3 * a - 2 >= 1
                assert n <= 10 * ell - 4
                assert n - log_n * codimension <= -3 * ell - 4
                if a % 2:
                    odd_cells += 1
                    assert j % 2 == 1
                    assert v2(j) == 0
                else:
                    assert v2(j) >= 1
                checked += 1

    assert checked > 0 and odd_cells > 0
    print(
        "PASS: master-flat dimensions, sub-balance, and dyadic parity",
        f"cells={checked}",
        f"odd={odd_cells}",
    )


if __name__ == "__main__":
    main()
