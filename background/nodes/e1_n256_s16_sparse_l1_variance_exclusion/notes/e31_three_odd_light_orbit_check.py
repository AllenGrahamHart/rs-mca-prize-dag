#!/usr/bin/env python3
"""Independently replay the E31 three-odd light orbits in gap coordinates."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
CLASSIFIER = HERE / "e31_three_odd_light_orbit_classifier.py"
RESULT = HERE / "e31_three_odd_light_orbit_result.json"


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
    partition = tuple(
        sorted(
            (count for chord, count in counts.items() if chord != 64),
            reverse=True,
        )
    )
    return diameter, odd, partition


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
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e31-three-odd-light-orbits-v1"
    assert packet["complete"] is True
    assert packet["source_sha256"] == hashlib.sha256(CLASSIFIER.read_bytes()).hexdigest()
    assert int(packet["normalized_supports"]) == 960
    assert int(packet["orbits"]) == 8
    assert packet["normalized_orbit_size_histogram"] == {
        "32": 2,
        "64": 2,
        "128": 2,
        "256": 2,
    }
    assert packet["partition_histogram"] == {"2,1,1,1": 960}
    assert packet["repeated_shape_histogram"] == {"wedge": 8}

    valid = valid_gap_supports()
    assert len(valid) == 960
    covered: set[tuple[int, ...]] = set()
    rows = packet["rows"]
    assert isinstance(rows, list) and len(rows) == 8
    for row in rows:
        representative = tuple(map(int, row["representative"]))
        orbit = normalized_orbit(representative)
        assert len(orbit) == int(row["normalized_count"])
        assert not (covered & orbit)
        covered.update(orbit)
        counts = Counter(
            distance(left, right) for left, right in combinations(representative, 2)
        )
        assert counts[64] == 1
        repeated = int(row["repeated_distance"])
        assert counts[repeated] == 2
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
        "E31_THREE_ODD_LIGHT_ORBIT_CHECK_PASS "
        "gap_supports=960 orbits=8 diameter=1 repeated_wedges=8 mutation=1"
    )


if __name__ == "__main__":
    main()
