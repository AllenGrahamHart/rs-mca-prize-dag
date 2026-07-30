#!/usr/bin/env python3
"""Independent Burnside audit of the m4 adjacency-genus exclusion."""

from __future__ import annotations

from itertools import combinations, permutations
from math import lcm


PAIR_MASKS = tuple(sum(1 << value for value in pair) for pair in combinations(range(6), 2))
ADJACENCY = tuple(
    (left, right)
    for left in PAIR_MASKS
    for right in PAIR_MASKS
    if (left & right).bit_count() == 1
)
PASSPORTS = {
    "S6_652": ((6,), (5, 1), (2, 1, 1, 1, 1)),
    "S6_562": ((5, 1), (3, 2, 1), (2, 2, 2)),
    "A6_542": ((5, 1), (4, 2), (2, 2, 1, 1)),
    "S6_four_point": (
        (5, 1),
        (2, 1, 1, 1, 1),
        (2, 2, 1, 1),
        (2, 2, 2),
    ),
}
EXPECTED = {
    "S6_652": (244, 3, 5),
    "S6_562": (250, 6, 11),
    "A6_542": (246, 4, 7),
    "S6_four_point": (264, 13, 25),
}


def permutation_sign(value: tuple[int, ...]) -> int:
    inversions = sum(
        value[left] > value[right]
        for left in range(6)
        for right in range(left + 1, 6)
    )
    return -1 if inversions % 2 else 1


def representative(cycle_type: tuple[int, ...]) -> tuple[int, ...]:
    value = list(range(6))
    offset = 0
    for length in cycle_type:
        cycle = list(range(offset, offset + length))
        for index, point in enumerate(cycle):
            value[point] = cycle[(index + 1) % length]
        offset += length
    assert offset == 6
    return tuple(value)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[value]] for value in range(6))


def power(value: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result = tuple(range(6))
    for _ in range(exponent):
        result = compose(value, result)
    return result


def transport_mask(value: tuple[int, ...], mask: int) -> int:
    return sum(1 << value[letter] for letter in range(6) if mask & (1 << letter))


def fixed_adjacency_states(value: tuple[int, ...]) -> int:
    return sum(
        transport_mask(value, left) == left and transport_mask(value, right) == right
        for left, right in ADJACENCY
    )


def burnside_cycle_count(cycle_type: tuple[int, ...]) -> int:
    value = representative(cycle_type)
    order = lcm(*cycle_type)
    fixed_sum = sum(fixed_adjacency_states(power(value, exponent)) for exponent in range(order))
    assert fixed_sum % order == 0
    return fixed_sum // order


def act_pair(value: tuple[int, ...], mask: int) -> int:
    return transport_mask(value, mask)


def group_action_audit() -> None:
    symmetric = tuple(permutations(range(6)))
    alternating = tuple(value for value in symmetric if permutation_sign(value) == 1)
    base = PAIR_MASKS[0]
    base_state = ADJACENCY[0]
    for group, order, stabilizer_order in (
        (symmetric, 720, 48),
        (alternating, 360, 24),
    ):
        assert len(group) == order
        stabilizer = tuple(value for value in group if act_pair(value, base) == base)
        assert len(stabilizer) == stabilizer_order
        unseen = set(PAIR_MASKS)
        subdegrees = []
        while unseen:
            seed = next(iter(unseen))
            current = {act_pair(value, seed) for value in stabilizer}
            subdegrees.append(len(current))
            unseen -= current
        assert sorted(subdegrees) == [1, 6, 8]
        orbit = {
            (act_pair(value, base_state[0]), act_pair(value, base_state[1]))
            for value in group
        }
        assert len(orbit) == 120


def main() -> None:
    assert len(PAIR_MASKS) == 15
    assert len(ADJACENCY) == 120
    group_action_audit()

    cycle_counts = {
        cycle_type: burnside_cycle_count(cycle_type)
        for passport in PASSPORTS.values()
        for cycle_type in passport
    }
    assert cycle_counts == {
        (6,): 20,
        (5, 1): 24,
        (4, 2): 30,
        (3, 2, 1): 26,
        (2, 1, 1, 1, 1): 72,
        (2, 2, 1, 1): 60,
        (2, 2, 2): 60,
    }

    for label, passport in PASSPORTS.items():
        total_index = sum(120 - cycle_counts[cycle_type] for cycle_type in passport)
        numerator = -240 + total_index
        assert numerator % 2 == 0
        outer_genus = 1 + numerator // 2
        minimum_source_genus = 2 * outer_genus - 1
        assert (total_index, outer_genus, minimum_source_genus) == EXPECTED[label]
        assert minimum_source_genus > (2 - 1) * (4 - 1)

    characteristic = 2130706433
    assert characteristic % 2 == 1
    print("RATE_HALF_KB_M4_ADJACENCY_GENUS_BURNSIDE_AUDIT_PASS")
    print("RATE_HALF_KB_M4_ADJACENCY_GENUS_FOUR_OF_FOUR_EXCLUDED")


if __name__ == "__main__":
    main()
