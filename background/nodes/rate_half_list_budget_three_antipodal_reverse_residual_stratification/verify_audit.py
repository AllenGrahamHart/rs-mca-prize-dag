#!/usr/bin/env python3
"""Audit the exact residual degree against all small floor strata."""

from __future__ import annotations


def ceiling_divide(numerator: int, denominator: int) -> int:
    return -(-numerator // denominator)


def main() -> None:
    cases = 0
    for r in range(1, 1025):
        for q in (2, 3, 4):
            minimum_v = max(0, ceiling_divide((q - 1) * r - 4, q))
            boundary_degree = r + 4 - q * (r - minimum_v)
            assert 0 <= boundary_degree < q or minimum_v == 0

            for v in range(minimum_v, r):
                degree = r + 4 - q * (r - v)
                assert degree == boundary_degree + q * (v - minimum_v)
                assert degree >= 0
                cases += 1

            if minimum_v:
                assert r + 4 - q * (r - (minimum_v - 1)) < 0

    r = (1 << 37) - 1
    official = {
        2: ((1 << 36) - 2, 1),
        3: (((1 << 38) - 4) // 3, 2),
    }
    for q, (v, expected_degree) in official.items():
        assert r + 4 - q * (r - v) == expected_degree
        assert r + 4 - q * (r - (v - 1)) < 0

    print(
        "AUDIT_RATE_HALF_ANTIPODAL_REVERSE_RESIDUAL_PASS "
        f"small_floor_cases={cases} official_mutations=2"
    )


if __name__ == "__main__":
    main()
