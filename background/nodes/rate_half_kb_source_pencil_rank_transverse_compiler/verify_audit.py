#!/usr/bin/env python3
"""Independently enumerate every transverse outer type."""


EXPECTED = {
    2: (2, 4, 8),
    3: (2, 3, 4, 6, 12),
    4: (1, 2, 4, 8),
    6: (1, 2, 3, 4, 6, 8),
    10: (1, 2, 4, 5),
    12: (1, 2, 3, 4),
}


def divisors(value: int) -> tuple[int, ...]:
    return tuple(candidate for candidate in range(1, value + 1) if value % candidate == 0)


def main() -> None:
    rows = {}
    pairs = []
    for m in EXPECTED:
        n = 60 // m
        admitted = []
        for r in divisors(4 * m):
            delta = 4 * m // r
            if delta <= m * m and r <= n - 1:
                admitted.append(r)
                pairs.append((m, r, delta))
        rows[m] = tuple(admitted)
    assert rows == EXPECTED
    assert len(pairs) == 26
    assert len(set(pairs)) == 26
    print("RATE_HALF_KB_SOURCE_PENCIL_RANK_TRANSVERSE_COMPILER_AUDIT_PASS")


if __name__ == "__main__":
    main()
