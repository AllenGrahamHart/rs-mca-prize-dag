#!/usr/bin/env python3
"""Check the E=35 high-outer three-layer quotient coupling exactly."""

from __future__ import annotations

from collections.abc import Iterator
from itertools import product


CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}
EXPECTED_HIGH = {
    (2, 1, 0, 0, 6, 0, 0, 0, 3),
    (2, 0, 0, 1, 6, 0, 0, 0, 3),
    (2, 0, 0, 0, 6, 1, 0, 0, 3),
    (2, 0, 0, 0, 6, 0, 0, 1, 3),
}


def allocations(
    capacities: tuple[int, ...], total: int, index: int = 0
) -> Iterator[tuple[int, ...]]:
    if index == len(capacities):
        if total == 0:
            yield ()
        return
    for count in range(min(capacities[index], total) + 1):
        for suffix in allocations(capacities, total - count, index + 1):
            yield (count,) + suffix


def residue_counts(counts: tuple[int, ...]) -> tuple[int, ...]:
    residues = [0] * 16
    residues[0] = 2 * counts[0]
    residues[8] = 2 * counts[8]
    for residue in range(1, 8):
        residues[residue] = residues[16 - residue] = counts[residue]
    return tuple(residues)


def directed_bound(
    left: tuple[int, ...],
    right: tuple[int, ...],
    target: tuple[int, ...],
) -> int:
    answer = 0
    for target_residue in range(16):
        pairs = sum(
            left[left_residue] * right[(-target_residue - left_residue) % 16]
            for left_residue in range(16)
        )
        if target_residue == 0:
            pairs -= min(sum(left), sum(right))
        per_target = sum(
            min(left[left_residue], right[(-target_residue - left_residue) % 16])
            for left_residue in range(16)
        )
        answer += min(pairs, target[target_residue] * per_target)
    return answer


def triple_bound(
    first: tuple[int, ...],
    second: tuple[int, ...],
    third: tuple[int, ...],
) -> int:
    return min(
        directed_bound(first, second, third),
        directed_bound(first, third, second),
        directed_bound(second, third, first),
    )


def layered_objective(
    outer: tuple[int, ...],
    middle: tuple[int, ...],
    top: tuple[int, ...],
) -> int:
    layers = tuple(map(residue_counts, (outer, middle, top)))
    return sum(
        0
        if first == second == third == 2
        else triple_bound(layers[first], layers[second], layers[third])
        for first, second, third in product(range(3), repeat=3)
    )


def main() -> None:
    high_by_order = {}
    outer_counts = {}
    for order, capacities in CAPACITIES.items():
        high = []
        tested = 0
        for outer in allocations(capacities, 12):
            if not any(outer[index] for index in (1, 3, 5, 7)):
                continue
            tested += 1
            residues = residue_counts(outer)
            aaa = triple_bound(residues, residues, residues)
            if aaa > 458:
                high.append((aaa, outer))
        high_by_order[order] = high
        outer_counts[order] = tested

    assert outer_counts == {128: 104_750, 64: 32_346}
    assert {outer for value, outer in high_by_order[128] if value == 460} == (
        EXPECTED_HIGH
    )
    assert len(high_by_order[128]) == 4
    assert high_by_order[64] == []

    nested_tested = 0
    nested_maximum = -1
    for _, outer in high_by_order[128]:
        for middle in allocations(outer, 6):
            for top_index, count in enumerate(middle):
                if count == 0:
                    continue
                top = tuple(int(index == top_index) for index in range(9))
                nested_tested += 1
                nested_maximum = max(
                    nested_maximum, layered_objective(outer, middle, top)
                )

    assert nested_tested == 276
    assert nested_maximum == 2054
    assert 458 + 1704 == 2162
    assert max(2162, nested_maximum, 454 + 1704) == 2162
    print(
        "E1_E35_HIGH_OUTER_COUPLING_CHECK_PASS "
        "outer=104750/32346 high=4/0 nested=276 maximum=2054 global=2162"
    )


if __name__ == "__main__":
    main()
