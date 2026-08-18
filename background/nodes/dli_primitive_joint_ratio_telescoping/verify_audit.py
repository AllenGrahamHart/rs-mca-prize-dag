#!/usr/bin/env python3
"""Independent structural audit of primitive ratio telescoping."""

from __future__ import annotations

from fractions import Fraction

import verify


def primitive_root(q: int) -> int:
    for g in range(2, q):
        if pow(g, (q - 1) // 2, q) != 1:
            return g
    raise AssertionError("primitive root missing")


def direct_counts(q: int, n: int, t: int) -> tuple[int, int]:
    zeta = pow(primitive_root(q), (q - 1) // n, q)
    total = primitive = 0
    for mask in range(1 << n):
        if any(
            sum(pow(zeta, r * i, q) for i in range(n) if mask >> i & 1) % q
            for r in range(1, t + 1)
        ):
            continue
        total += 1
        antipodal = all(
            bool(mask >> i & 1) == bool(mask >> (i + n // 2) & 1)
            for i in range(n // 2)
        )
        primitive += not antipodal
    return total, primitive


def main() -> None:
    result = verify.build()
    assert result["summary"]["rows"] == 45
    assert direct_counts(17, 16, 2) == (224, 208)
    assert direct_counts(17, 8, 2) == (4, 0)

    row = result["rows"]["32|4|97"]
    expected = Fraction(
        (176 - 16) << (32 * 2),
        45946768 * 615200 * 44299296,
    )
    assert row["z0"] == 176 and row["c1"] == 16
    assert Fraction(row["ratio_numerator"], row["ratio_denominator"]) == expected
    print("DLI_PRIMITIVE_RATIO_TELESCOPING_AUDIT_PASS")


if __name__ == "__main__":
    main()
