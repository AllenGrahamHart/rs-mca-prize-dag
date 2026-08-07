# CATCH #71 (2026-07-10): this script verifies the SUPERSEDED envelope
# arithmetic (2890/6986 constants). Corrected: R^2 envelope, (4/9), 5780n;
# the combined-6986 corollary is dead. Kept for provenance; do not consume.
#!/usr/bin/env python3
"""Exact official-row arithmetic for the h=3 trace-zero payment."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_per_row_accident_pose import compiled_bound


OFFICIAL_EXPONENTS = tuple(range(13, 42))
TRACEZERO_C = 2_890
NONZERO_C = 4_096
COMBINED_C = TRACEZERO_C + NONZERO_C


def floor_scaled_cube_root(numerator: int, denominator: int) -> int:
    lo, hi = 0, 1
    while denominator * hi**3 <= numerator:
        hi *= 2
    while lo + 1 < hi:
        middle = (lo + hi) // 2
        if denominator * middle**3 <= numerator:
            lo = middle
        else:
            hi = middle
    return lo


@dataclass(frozen=True)
class Row:
    exponent: int
    n: int
    a: int
    b: int
    linear_slack: int
    sparse_slack: int
    prime_slack: int
    degree_cube_slack: int


def official_rows() -> tuple[Row, ...]:
    rows: list[Row] = []
    for exponent in OFFICIAL_EXPONENTS:
        n = 1 << exponent
        a = floor_scaled_cube_root(27 * n * n, 64)
        b = floor_scaled_cube_root(125 * n, 64) + 1
        d = a

        linear_slack = a * b * b - d * (a + d)
        sparse_slack = n - a * b
        prime_slack = n * n + 1 - (a + n * b)
        degree_cube_slack = 64 * a**3 * n**2 - (a + 2 * n * b) ** 3
        if min(linear_slack, prime_slack, degree_cube_slack) <= 0:
            raise AssertionError((exponent, a, b, linear_slack, prime_slack))
        if sparse_slack < 0:
            raise AssertionError((exponent, a, b, sparse_slack))

        # (2/9)n^(1/3) < TRACEZERO_C, cubed without real arithmetic.
        if 8 * n >= (9 * TRACEZERO_C) ** 3:
            raise AssertionError((exponent, n, TRACEZERO_C))
        if compiled_bound(n, COMBINED_C) >= n**3:
            raise AssertionError((exponent, COMBINED_C))

        rows.append(
            Row(
                exponent,
                n,
                a,
                b,
                linear_slack,
                sparse_slack,
                prime_slack,
                degree_cube_slack,
            )
        )
    return tuple(rows)


def main() -> None:
    rows = official_rows()
    print(
        "H3_TRACEZERO_OFFICIAL_PAYMENT_PASS "
        f"rows={len(rows)} trace_c={TRACEZERO_C} combined_c={COMBINED_C}"
    )


if __name__ == "__main__":
    main()
