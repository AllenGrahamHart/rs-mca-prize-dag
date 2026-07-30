#!/usr/bin/env python3
"""Verify the KoalaBear source-pencil compiler arithmetic."""

from math import factorial, gcd
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROWS = (
    (2, 30, 6, 0, 10395),
    (3, 20, 4, 0, 15400),
    (4, 15, 3, 0, 5775),
    (5, 12, 2, 2, 8316),
    (6, 10, 2, 0, 462),
    (10, 6, 1, 1, 66),
    (12, 5, 1, 0, 1),
    (30, 2, 0, 2, 462),
)


def partition_count(m: int, a: int, b: int) -> int:
    exceptional = m // 5 if b else 0
    denominator = factorial(m) ** a * factorial(a)
    denominator *= factorial(exceptional) ** b * factorial(b)
    return factorial(12) // denominator


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "{2,3,4,6,10,12}" in statement
    assert "No endpoint-to-carrier bridge" in contract

    for m, n, a, b, expected_partitions in ROWS:
        assert m * n == 60
        assert 5 * a + b == n
        assert partition_count(m, a, b) == expected_partitions
    p = 2130706433
    assert gcd(5, p**6 - 1) == 1
    assert 30 == 5 * 6
    assert 60 // 12 + 1 == 6
    assert [m for m, *_ in ROWS if 2**21 % m == 0] == [2, 4]
    print("RATE_HALF_KB_DECOMPOSITION_SOURCE_PENCIL_COMPILER_PASS")


if __name__ == "__main__":
    main()
