#!/usr/bin/env python3
"""Independent audit of the E26 profile and light-support router."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTES = HERE
TWO = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_two_six_odd_light_orbit_result.json"
SIX = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes/e30_six_odd_mask_orbits_result.json"


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
            if energy == 26 and l1_norm <= 16:
                layers = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(min(a*b-min(a,b), a*c-min(a,c), b*c-min(b,c)) for a in layers for b in layers for c in layers)
                answer.append((tuple(counts), cap, sum(counts[0::2])))
            return
        for count in range((26 - energy) // (magnitude * magnitude) + 1):
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
    assert len(profiles) == 13
    assert [counts for counts, cap, odd in profiles if cap > 228 and odd <= 6] == [
        (6,5,0,0,0), (2,6,0,0,0), (5,3,1,0,0), (1,4,1,0,0),
        (4,1,2,0,0), (0,2,2,0,0), (6,1,0,1,0), (2,2,0,1,0),
        (1,0,1,1,0), (1,0,0,0,1),
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
    for moment in (228,229):
        raw = (1,16,308,6592+moment)
        evaluated.append(tuple(sum(raw[degree]*forms[basis][degree] for degree in range(4)) for basis in range(3)))
    assert evaluated == [
        (Fraction(73379,79507), Fraction(6128,79507), Fraction(-9755,245917)),
        (Fraction(73381,79507), Fraction(6126,79507), Fraction(-58459,1475502)),
    ]

    probe = json.loads((NOTES / "e26_profile_parity_probe_result.json").read_text())
    two_packet = json.loads(TWO.read_text())
    two: set[tuple[int, ...]] = set()
    for row in two_packet["rows"]:
        raw = row["representative"]
        orbit = normalized_orbit(tuple(raw))
        assert two.isdisjoint(orbit) and all(signature(item) == (0,2) for item in orbit)
        two.update(orbit)
    six_packet = json.loads(SIX.read_text())
    six: set[tuple[int, ...]] = set()
    for row in six_packet["rows"]:
        for raw in row["orbits"]:
            orbit = normalized_orbit(tuple(raw))
            assert six.isdisjoint(orbit) and all(signature(item) == (0,6) for item in orbit)
            six.update(orbit)
    expected_two: set[tuple[int, ...]] = set()
    expected_six: set[tuple[int, ...]] = set()
    two_diameter = 0
    for rest in combinations(range(1,128),3):
        support = (0,) + rest
        sig = signature(support)
        if sig[0] == 2:
            assert sig[1] == 0
            two_diameter += 1
        if sig == (0,2): expected_two.add(support)
        if sig == (0,6): expected_six.add(support)
    assert two_diameter == 63
    assert two == expected_two and len(two) == 8168
    assert six == expected_six and len(six) == 280720
    assert probe["relevant_affine_templates"] == 87 + 1234
    assert probe["direct_vector_floor"] == (87 + 1234) * 310124 * 64

    print("E26_PROFILE_PARITY_PROBE_AUDIT_PASS profiles=13 forms=2 two=8168/87 six=280720/1234 router=1321")


if __name__ == "__main__":
    main()
