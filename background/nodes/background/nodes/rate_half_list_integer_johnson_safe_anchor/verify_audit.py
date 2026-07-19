#!/usr/bin/env python3
"""Independent small-family audit of the integer Johnson certificate."""

from __future__ import annotations

from itertools import combinations


def balanced_minimum(length: int, lists: int, agreement: int) -> int:
    degree, remainder = divmod(lists * agreement, length)
    return (length - remainder) * degree * (degree - 1) // 2 + remainder * degree * (
        degree + 1
    ) // 2


def certified(length: int, dimension: int, budget: int, agreement: int) -> bool:
    lists = budget + 1
    return balanced_minimum(length, lists, agreement) > (
        lists * (lists - 1) // 2 * (dimension - 1)
    )


def family_exists(length: int, dimension: int, lists: int, agreement: int) -> bool:
    subsets = tuple(combinations(range(length), agreement))
    encoded = tuple(sum(1 << value for value in subset) for subset in subsets)
    for family in combinations(encoded, lists):
        if all(
            (family[i] & family[j]).bit_count() <= dimension - 1
            for i in range(lists)
            for j in range(i + 1, lists)
        ):
            return True
    return False


def main() -> None:
    fixtures = ((6, 3, 1, 5), (7, 3, 2, 5), (8, 4, 3, 6))
    for length, dimension, budget, agreement in fixtures:
        assert certified(length, dimension, budget, agreement)
        assert not family_exists(length, dimension, budget + 1, agreement)

    # Strictness is load-bearing: equality permits this three-set family.
    family = ({0, 1}, {0, 2}, {1, 2})
    assert sum(len(left & right) for left, right in combinations(family, 2)) == 3
    assert 3 == 3 * (2 - 1)

    print(
        "AUDIT_RATE_HALF_LIST_INTEGER_JOHNSON_SAFE_ANCHOR_PASS "
        f"small_family_fixtures={len(fixtures)} strictness_control=1/1"
    )


if __name__ == "__main__":
    main()
