#!/usr/bin/env python3
"""Independent positive-gap replay of the E32 four-odd light orbits."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
CLASSIFIER = HERE / "e32_four_odd_light_orbit_classifier.py"
RESULT = HERE / "e32_four_odd_light_orbit_result.json"


def distance(left: int, right: int) -> int:
    difference = abs(left - right)
    return min(difference, 128 - difference)


def profile(support: tuple[int, ...]) -> tuple[int, int, tuple[int, ...]]:
    counts = Counter(
        distance(support[left], support[right])
        for left in range(4)
        for right in range(left + 1, 4)
    )
    diameter = counts[64]
    odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
    return diameter, odd, tuple(sorted(counts.values(), reverse=True))


def valid_gap_supports() -> set[tuple[int, ...]]:
    answer = set()
    for first_gap in range(1, 126):
        for second_gap in range(1, 127 - first_gap):
            for third_gap in range(1, 128 - first_gap - second_gap):
                fourth_gap = 128 - first_gap - second_gap - third_gap
                if fourth_gap <= 0:
                    continue
                support = (
                    0,
                    first_gap,
                    first_gap + second_gap,
                    first_gap + second_gap + third_gap,
                )
                diameter, odd, multiplicities = profile(support)
                if diameter in (0, 2) and odd == 4:
                    assert diameter == 0
                    assert multiplicities == (2, 1, 1, 1, 1)
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
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e32-four-odd-light-orbits-v1"
    assert packet["complete"] is True
    assert packet["source_sha256"] == hashlib.sha256(CLASSIFIER.read_bytes()).hexdigest()
    assert int(packet["normalized_supports"]) == 28_800
    assert int(packet["orbits"]) == 148
    assert packet["normalized_orbit_size_histogram"] == {
        "32": 4,
        "64": 16,
        "128": 40,
        "256": 88,
    }
    assert packet["repeated_shape_histogram"] == {"wedge": 148}

    valid = valid_gap_supports()
    assert len(valid) == 28_800
    covered: set[tuple[int, ...]] = set()
    rows = packet["rows"]
    assert isinstance(rows, list) and len(rows) == 148
    for row in rows:
        representative = tuple(map(int, row["representative"]))
        orbit = normalized_orbit(representative)
        assert len(orbit) == int(row["normalized_count"])
        assert not (covered & orbit)
        covered.update(orbit)
        counts = Counter(
            distance(left, right) for left, right in combinations(representative, 2)
        )
        repeated = int(row["repeated_distance"])
        assert counts[repeated] == 2
        assert sorted(counts.values(), reverse=True) == [2, 1, 1, 1, 1]
        repeated_edges = [
            frozenset((left, right))
            for left, right in combinations(representative, 2)
            if distance(left, right) == repeated
        ]
        assert repeated_edges[0] & repeated_edges[1]
        assert row["repeated_shape"] == "wedge"
    assert covered == valid
    assert len(covered - normalized_orbit(tuple(rows[-1]["representative"]))) < len(valid)

    print(
        "E32_FOUR_ODD_LIGHT_ORBIT_CHECK_PASS "
        "gap_supports=28800 orbits=148 diameters=0 repeated_wedges=148 mutation=1"
    )


if __name__ == "__main__":
    main()
