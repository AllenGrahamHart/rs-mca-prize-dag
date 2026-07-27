#!/usr/bin/env python3
"""Independent audit of the E=30 profile and light-support frontier."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_profile_parity_light_reduction"
PACKET = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_result.json"


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
            if energy == 30 and l1_norm <= 18:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(
                    min(
                        first * second - min(first, second),
                        first * third - min(first, third),
                        second * third - min(second, third),
                    )
                    for first in layers for second in layers for third in layers
                )
                answer.append((tuple(counts), cap, sum(counts[0::2])))
            return
        for count in range((30 - energy) // (magnitude * magnitude) + 1):
            new_l1 = l1_norm + magnitude * count
            if new_l1 > 18:
                break
            visit(magnitude + 1, energy + magnitude * magnitude * count, new_l1, counts + [count])

    visit(1, 0, 0, [])
    return sorted(answer, key=lambda item: (item[1], item[0]), reverse=True)


def matching_ledgers() -> set[int]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    ledgers = set()

    def visit(available: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> None:
        if not available:
            light_edges = sum(weights[left] == weights[right] == 1 for left, right in edges)
            if light_edges == 0:
                ledgers.add(sum((weights[left] * weights[right]) ** 2 for left, right in edges))
            return
        first = available[0]
        visit(available[1:], edges)
        for offset, second in enumerate(available[1:]):
            remainder = available[1:offset + 1] + available[offset + 2:]
            visit(remainder, edges + ((first, second),))

    visit(tuple(range(7)), ())
    return ledgers


def distance(left: int, right: int) -> int:
    difference = abs(left - right)
    return min(difference, 128 - difference)


def signature(support: tuple[int, ...]) -> tuple[int, int, tuple[int, ...]]:
    counts = Counter(distance(left, right) for left, right in combinations(support, 2))
    return (
        counts[64],
        sum(count % 2 for chord, count in counts.items() if chord != 64),
        tuple(sorted((count for chord, count in counts.items() if chord != 64), reverse=True)),
    )


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
    assert len(profiles) == 18
    above = [profile for profile in profiles if profile[1] > 1087]
    assert len(above) == 13
    survivors = [counts for counts, _, odd in above if odd <= 6]
    assert survivors == [
        (6, 6, 0, 0, 0), (2, 7, 0, 0, 0), (5, 4, 1, 0, 0),
        (1, 5, 1, 0, 0), (4, 2, 2, 0, 0), (0, 3, 2, 0, 0),
        (6, 2, 0, 1, 0), (3, 0, 3, 0, 0),
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
    for moment in (1087, 1088):
        raw = (1, 16, 316, 6976 + moment)
        forms.append(tuple(sum(raw[degree] * coefficient_forms[basis][degree] for degree in range(4)) for basis in range(3)))
    assert forms == [
        (Fraction(74161, 79507), Fraction(5346, 79507), Fraction(-38165, 1475502)),
        (Fraction(74163, 79507), Fraction(5344, 79507), Fraction(-907, 35131)),
    ]
    assert matching_ledgers() == {0, 4, 8, 12, 16, 20}

    packet = json.loads(PACKET.read_text())
    covered: set[tuple[int, ...]] = set()
    for row in packet["rows"]:
        representative = tuple(map(int, row["representative"]))
        orbit = normalized_orbit(representative)
        assert not covered.intersection(orbit)
        covered.update(orbit)
        assert signature(representative)[0:2] == (0, 2)
    assert len(covered) == 8168
    assert sum(row["normalized_count"] for row in packet["rows"]) == 8168
    assert len(packet["rows"]) == 87
    assert packet["normalized_six_odd_supports"] == 280720
    assert packet["six_odd_orbit_lower_bound"] == 1097

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    statement = (ROOT / nodes[NODE]["refs"][0]).read_text()
    assert "not an exclusion" in statement
    assert "at least 21,773,185,792" in statement

    print(
        "E1_N256_S16_E30_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS "
        "recursive_profiles=18 hermite=independent matchings=complete two_orbits=87 mutations=4"
    )


if __name__ == "__main__":
    main()
