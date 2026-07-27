#!/usr/bin/env python3
"""Independent audit of the E28 profile and light-support router."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e28_profile_parity_light_reduction/notes"
FOUR = ROOT / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes/e32_four_odd_light_orbit_result.json"


def solve(matrix: list[list[Fraction]], target: list[Fraction]) -> list[Fraction]:
    augmented = [row[:] + [value] for row, value in zip(matrix, target)]
    for column in range(len(matrix)):
        pivot = next(row for row in range(column, len(matrix)) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(len(matrix)):
            if row != column:
                scale = augmented[row][column]
                augmented[row] = [left - scale * right for left, right in zip(augmented[row], augmented[column])]
    return [row[-1] for row in augmented]


def recursive_profiles() -> list[tuple[tuple[int, ...], int, int]]:
    answer = []

    def visit(magnitude: int, energy: int, l1_norm: int, counts: list[int]) -> None:
        if magnitude == 6:
            if energy == 28 and l1_norm <= 16:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(min(a*b-min(a,b), a*c-min(a,c), b*c-min(b,c)) for a in layers for b in layers for c in layers)
                answer.append((tuple(counts), cap, sum(counts[0::2])))
            return
        for count in range((28 - energy) // (magnitude * magnitude) + 1):
            next_l1 = l1_norm + magnitude * count
            if next_l1 > 16:
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
        transformed for unit in range(1, 128, 2) for translation in range(128)
        for transformed in (tuple(sorted((unit * value + translation) % 128 for value in representative)),)
        if transformed[0] == 0
    }


def main() -> None:
    profiles = recursive_profiles()
    assert len(profiles) == 14
    assert [counts for counts, cap, odd in profiles if cap > 658 and odd <= 6] == [
        (4,6,0,0,0), (0,7,0,0,0), (3,4,1,0,0), (2,2,2,0,0),
        (4,2,0,1,0), (1,0,3,0,0), (0,3,0,1,0), (3,0,1,1,0),
    ]
    matrix = [
        [Fraction(14**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(28), Fraction(3 * 14**2)],
        [Fraction(57**power) for power in range(4)],
        [Fraction(0), Fraction(1), Fraction(114), Fraction(3 * 57**2)],
    ]
    forms = [solve(matrix, target) for target in (
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1,14), Fraction(0), Fraction(1,57)],
    )]
    evaluated = []
    for moment in (658,659):
        raw = (1,16,312,6784+moment)
        evaluated.append(tuple(sum(raw[degree]*forms[basis][degree] for degree in range(4)) for basis in range(3)))
    assert evaluated == [
        (Fraction(73771,79507), Fraction(5736,79507), Fraction(-8052,245917)),
        (Fraction(73773,79507), Fraction(5734,79507), Fraction(-2539,77658)),
    ]

    probe = json.loads((NOTES / "e28_profile_parity_probe_result.json").read_text())
    zero: set[tuple[int, ...]] = set()
    for raw in probe["light_geometry"]["zero_odd_orbits"]:
        orbit = normalized_orbit(tuple(raw))
        assert zero.isdisjoint(orbit) and all(signature(item) == (2,0) for item in orbit)
        zero.update(orbit)
    four_packet = json.loads(FOUR.read_text())
    four: set[tuple[int, ...]] = set()
    for row in four_packet["rows"]:
        orbit = normalized_orbit(tuple(row["representative"]))
        assert four.isdisjoint(orbit) and all(signature(item) == (0,4) for item in orbit)
        four.update(orbit)
    expected_zero: set[tuple[int, ...]] = set()
    expected_four: set[tuple[int, ...]] = set()
    for rest in combinations(range(1,128),3):
        support = (0,) + rest
        sig = signature(support)
        if sig == (2,0): expected_zero.add(support)
        if sig == (0,4): expected_four.add(support)
    assert zero == expected_zero and len(zero) == 63
    assert four == expected_four and len(four) == 28800

    print("E1_N256_S16_E28_PROFILE_PARITY_LIGHT_REDUCTION_AUDIT_PASS profiles=14 forms=2 zero=63/6 four=28800/148")


if __name__ == "__main__":
    main()
