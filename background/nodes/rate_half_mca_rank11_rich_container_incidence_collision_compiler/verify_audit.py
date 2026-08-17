#!/usr/bin/env python3
"""Independent degree-balancing replay of rich-container collisions."""


def choose2(value: int) -> int:
    return value * (value - 1) // 2


def choose3(value: int) -> int:
    return value * (value - 1) * (value - 2) // 6


def ceiling_ratio(numerator: int, denominator: int) -> int:
    quotient, remainder = divmod(numerator, denominator)
    return quotient + bool(remainder)


def replay(count: int, expected):
    n, h = 1_048_576, 42_453
    incidence = count * h
    low, high_count = divmod(incidence, n)
    low_count = n - high_count
    pairs = low_count * choose2(low) + high_count * choose2(low + 1)
    triples = low_count * choose3(low) + high_count * choose3(low + 1)
    observed = (
        ceiling_ratio(incidence, n),
        ceiling_ratio(pairs, choose2(count)),
        ceiling_ratio(triples, choose3(count)),
    )
    assert observed == expected
    return observed


assert replay(508, (21, 1_640, 61)) == (21, 1_640, 61)
assert replay(254, (11, 1_562, 52)) == (11, 1_562, 52)
print("RANK11_RICH_CONTAINER_INCIDENCE_COLLISION_AUDIT_OK")
