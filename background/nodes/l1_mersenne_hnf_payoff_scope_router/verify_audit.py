#!/usr/bin/env python3
"""Independent hard-coded audit of the HNF payoff counts and ratio."""

from __future__ import annotations

from fractions import Fraction


ROWS = (
    (32768, 8191, 4),
    (524288, 131071, 4),
    (2097152, 524287, 4),
    (8589934592, 2147483647, 4),
    (65536, 8191, 8),
    (1048576, 131071, 8),
    (4194304, 524287, 8),
    (17179869184, 2147483647, 8),
    (131072, 8191, 16),
)


def live_degrees(m: int) -> tuple[int, ...]:
    return tuple(h for h in range(2, m) if not (m == 4 and h == 3))


def main() -> None:
    assert all(n == m * (p + 1) for n, p, m in ROWS)
    cells = [(n, p, m, h) for n, p, m in ROWS for h in live_degrees(m)]
    assert [len(live_degrees(m)) for m in (4, 8, 16)] == [1, 6, 14]
    assert len(cells) == 4 * 1 + 4 * 6 + 14 == 42
    assert sum(h % 2 == 0 for _, _, _, h in cells) == 4 + 12 + 7 == 23
    assert sum(h % 2 for _, _, _, h in cells) == 12 + 7 == 19
    nextmax = [(n, p, m, h) for n, p, m, h in cells if h == m - 1]
    assert len(nextmax) == 5

    for n, p, m in ROWS:
        for a in (p, (n + p) // 2, n):
            ratio = Fraction(n - a + p, p)
            assert ratio < m + 2

    print("L1_MERSENNE_HNF_PAYOFF_SCOPE_AUDIT_PASS")


if __name__ == "__main__":
    main()
