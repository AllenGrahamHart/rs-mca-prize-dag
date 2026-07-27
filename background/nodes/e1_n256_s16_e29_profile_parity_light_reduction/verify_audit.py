#!/usr/bin/env python3
"""Independent audit of the E29 profile and light-support router."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "background/nodes/e1_n256_s16_e29_profile_parity_light_reduction/notes/e29_profile_parity_probe_result.json"


def solve(matrix: list[list[Fraction]], target: list[Fraction]) -> list[Fraction]:
    augmented = [row[:] + [value] for row, value in zip(matrix, target)]
    for column in range(len(matrix)):
        pivot = next(row for row in range(column, len(matrix)) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(len(matrix)):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [left - scale * right for left, right in zip(augmented[row], augmented[column])]
    return [row[-1] for row in augmented]


def recursive_profiles() -> list[tuple[tuple[int, ...], int, int]]:
    answer = []

    def visit(magnitude: int, energy: int, l1_norm: int, counts: list[int]) -> None:
        if magnitude == 6:
            if energy == 29 and l1_norm <= 17:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(
                    min(a * b - min(a, b), a * c - min(a, c), b * c - min(b, c))
                    for a in layers for b in layers for c in layers
                )
                answer.append((tuple(counts), cap, sum(counts[0::2])))
            return
        for count in range((29 - energy) // (magnitude * magnitude) + 1):
            next_l1 = l1_norm + magnitude * count
            if next_l1 > 17:
                break
            visit(magnitude + 1, energy + magnitude * magnitude * count, next_l1, counts + [count])

    visit(1, 0, 0, [])
    return sorted(answer, key=lambda item: (item[1], item[0]), reverse=True)


def distance(left: int, right: int) -> int:
    difference = abs(left - right)
    return min(difference, 128 - difference)


def signature(support: tuple[int, ...]) -> tuple[int, int]:
    counts = Counter(distance(left, right) for left, right in combinations(support, 2))
    return counts[64], sum(count % 2 for chord, count in counts.items() if chord != 64)


def normalized_orbit(representative: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        transformed
        for unit in range(1, 128, 2)
        for translation in range(128)
        for transformed in (tuple(sorted((unit * value + translation) % 128 for value in representative)),)
        if transformed[0] == 0
    }


def main() -> None:
    profiles = recursive_profiles()
    assert len(profiles) == 17
    survivors = [counts for counts, cap, odd in profiles if cap > 872 and odd <= 5]
    assert survivors == [
        (5, 6, 0, 0, 0), (1, 7, 0, 0, 0), (4, 4, 1, 0, 0),
        (0, 5, 1, 0, 0), (3, 2, 2, 0, 0), (5, 2, 0, 1, 0),
        (2, 0, 3, 0, 0), (1, 3, 0, 1, 0),
    ]

    matrix = [
        [Fraction(14**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(28), Fraction(3 * 14**2)],
        [Fraction(57**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(114), Fraction(3 * 57**2)],
    ]
    coefficient_forms = [
        solve(matrix, target)
        for target in (
            [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(1, 14), Fraction(0), Fraction(1, 57)],
        )
    ]
    forms = []
    for moment in (872, 873):
        raw = (1, 16, 314, 6880 + moment)
        forms.append(tuple(sum(raw[degree] * coefficient_forms[basis][degree] for degree in range(4)) for basis in range(3)))
    assert forms == [
        (Fraction(73965, 79507), Fraction(5542, 79507), Fraction(-3091, 105393)),
        (Fraction(73967, 79507), Fraction(5540, 79507), Fraction(-14401, 491834)),
    ]

    packet = json.loads(PACKET.read_text())
    representatives = packet["light_geometry"]["orbit_representatives"]
    covered: dict[int, set[tuple[int, ...]]] = {1: set(), 3: set(), 5: set()}
    for odd in covered:
        for raw in representatives[str(odd)]:
            orbit = normalized_orbit(tuple(int(value) for value in raw))
            assert all(signature(support) == (1, odd) for support in orbit)
            assert covered[odd].isdisjoint(orbit)
            covered[odd].update(orbit)
    expected: dict[int, set[tuple[int, ...]]] = {1: set(), 3: set(), 5: set()}
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        diameter, odd = signature(support)
        if diameter == 1:
            expected[odd].add(support)
    assert covered == expected
    assert {odd: len(values) for odd, values in covered.items()} == {1: 264, 3: 960, 5: 14_400}

    print("E1_N256_S16_E29_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS profiles=17 forms=2 supports=15624 orbits=119")


if __name__ == "__main__":
    main()
