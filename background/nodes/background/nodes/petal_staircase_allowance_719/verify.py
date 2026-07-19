#!/usr/bin/env python3
"""Verify the exact finite-row petal staircase inflation allowance."""

from __future__ import annotations

from math import comb


def main() -> None:
    rows = []
    for exponent in (41, 42, 43, 44):
        n = 1 << exponent
        column = comb(n + 6, 6)
        allowance, remainder = divmod(n**6, column)
        if allowance != 719:
            raise AssertionError((exponent, allowance))
        if not 719 * column <= n**6 < 720 * column:
            raise AssertionError((exponent, remainder))
        # Mutation control: a factor 720 never fits.
        if 720 * column <= n**6:
            raise AssertionError((exponent, "mutation-720-survived"))
        rows.append(f"2^{exponent}")
    print("PETAL_STAIRCASE_ALLOWANCE_PASS allowance=719 rows=" + ",".join(rows))


if __name__ == "__main__":
    main()

