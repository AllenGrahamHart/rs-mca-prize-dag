#!/usr/bin/env python3
"""Independent audit of the E=31 profile and light-support router."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e31_profile_parity_light_reduction"
CLASSIFIER = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_classifier.py"
RESULT = ROOT / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e31_three_odd_light_orbit_result.json"


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
            augmented[row] = [
                left - scale * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return [row[-1] for row in augmented]


def log_bounds(value: Fraction, terms: int = 8) -> tuple[Fraction, Fraction]:
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(
        parameter ** (2 * index + 1) / (2 * index + 1)
        for index in range(terms)
    )
    degree = 2 * terms + 1
    return lower, lower + 2 * parameter**degree / (degree * (1 - parameter * parameter))


def recursive_profiles() -> list[tuple[tuple[int, ...], int, int]]:
    answer: list[tuple[tuple[int, ...], int, int]] = []

    def visit(magnitude: int, energy: int, l1_norm: int, counts: list[int]) -> None:
        if magnitude == 6:
            if energy == 31 and l1_norm <= 17:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(
                    min(
                        first * second - min(first, second),
                        first * third - min(first, third),
                        second * third - min(second, third),
                    )
                    for first in layers
                    for second in layers
                    for third in layers
                )
                answer.append((tuple(counts), cap, sum(counts[0::2])))
            return
        maximum = (31 - energy) // (magnitude * magnitude)
        for count in range(maximum + 1):
            new_l1 = l1_norm + magnitude * count
            if new_l1 > 17:
                break
            visit(magnitude + 1, energy + magnitude * magnitude * count, new_l1, counts + [count])

    visit(1, 0, 0, [])
    return sorted(answer, key=lambda item: (item[1], item[0]), reverse=True)


def matching_ledgers() -> set[int]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    ledgers: set[int] = set()

    def visit(available: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> None:
        if not available:
            light_edges = sum(weights[left] == weights[right] == 1 for left, right in edges)
            if light_edges == 1:
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


def profile(support: tuple[int, ...]) -> tuple[int, int, tuple[int, ...]]:
    counts = Counter(distance(left, right) for left, right in combinations(support, 2))
    diameter = counts[64]
    odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
    partition = tuple(sorted((count for chord, count in counts.items() if chord != 64), reverse=True))
    return diameter, odd, partition


def valid_gap_supports() -> set[tuple[int, ...]]:
    answer = set()
    for first in range(1, 126):
        for second in range(1, 127 - first):
            for third in range(1, 128 - first - second):
                fourth = 128 - first - second - third
                if fourth <= 0:
                    continue
                support = (0, first, first + second, first + second + third)
                diameter, odd, partition = profile(support)
                if diameter == 1 and odd == 3:
                    assert partition == (2, 1, 1, 1)
                    answer.add(support)
    return answer


def normalized_orbit(representative: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        transformed
        for unit in range(1, 128, 2)
        for translation in range(128)
        for transformed in (
            tuple(sorted((unit * value + translation) % 128 for value in representative)),
        )
        if transformed[0] == 0
    }


def main() -> None:
    profiles = recursive_profiles()
    assert len(profiles) == 15
    above = [(counts, cap, odd) for counts, cap, odd in profiles if cap > 1302]
    assert len(above) == 8
    survivors = [(counts, cap) for counts, cap, odd in above if odd <= 5]
    assert [counts for counts, _ in survivors] == [
        (3, 7, 0, 0, 0), (2, 5, 1, 0, 0), (1, 3, 2, 0, 0),
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
    for moment in (1302, 1303):
        raw_moments = (1, 16, 16**2 + 62, 16**3 + 3 * 16 * 62 + moment)
        forms.append(tuple(
            sum(raw_moments[degree] * coefficient_forms[basis][degree] for degree in range(4))
            for basis in range(3)
        ))
    assert forms == [
        (Fraction(74357, 79507), Fraction(5150, 79507), Fraction(-16528, 737751)),
        (Fraction(74359, 79507), Fraction(5148, 79507), Fraction(-10995, 491834)),
    ]

    l2, u2 = log_bounds(Fraction(2))
    l87, u87 = log_bounds(Fraction(8, 7))
    l6457, u6457 = log_bounds(Fraction(64, 57))
    assert Fraction(-568121, 2544224) * u2 + forms[0][0] * l87 + forms[0][1] * l6457 - forms[0][2] > 0
    assert Fraction(-567993, 2544224) * l2 + forms[1][0] * u87 + forms[1][1] * u6457 - forms[1][2] < 0

    assert matching_ledgers() == {1, 5, 9, 17, 21}
    packet = json.loads(RESULT.read_text())
    assert packet["source_sha256"] == hashlib.sha256(CLASSIFIER.read_bytes()).hexdigest()
    valid = valid_gap_supports()
    assert len(valid) == 960
    covered: set[tuple[int, ...]] = set()
    for row in packet["rows"]:
        orbit = normalized_orbit(tuple(row["representative"]))
        assert len(orbit) == row["normalized_count"]
        assert not covered.intersection(orbit)
        covered.update(orbit)
    assert covered == valid

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    statement = (ROOT / nodes[NODE]["refs"][0]).read_text()
    assert "This theorem is a reduction" in statement
    assert "not an exclusion" in statement

    print(
        "E1_N256_S16_E31_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS "
        "recursive_profiles=15 hermite=independent matchings=complete gap_supports=960 mutations=4"
    )


if __name__ == "__main__":
    main()
