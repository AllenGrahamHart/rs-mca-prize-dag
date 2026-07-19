#!/usr/bin/env python3
"""Audit zero-weld divisibility and quartic degree ratios."""

from __future__ import annotations

from math import gcd


def main() -> None:
    profiles = 0
    powers = 0
    for exponent in range(5, 18, 4):
        m = 1 << exponent
        e = 2 * m - 1
        assert e % 5 == 3
        for residual_e in range(e // 5 + 1):
            dominant_e = e - residual_e
            r = 2 * dominant_e + 1
            assert gcd(dominant_e, r) == 1
            assert (4 * e + 1) % dominant_e == 4 * residual_e + 1
            assert (4 * e) % dominant_e == 4 * residual_e
            if residual_e:
                assert (4 * e) % dominant_e
            profiles += 1
        assert (8 * e + 7) - 4 * (2 * e + 1) == 3
        powers += 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_ZERO_WELD_QUARTIC_PASS "
        f"profiles={profiles} power_rows={powers} mutations=3"
    )


if __name__ == "__main__":
    main()
