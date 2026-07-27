#!/usr/bin/env python3
"""Independently replay the E30 light router in circular-gap coordinates."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
CLASSIFIER = HERE / "e30_two_six_odd_light_orbit_classifier.py"
RESULT = HERE / "e30_two_six_odd_light_orbit_result.json"


def distance(left: int, right: int) -> int:
    difference = abs(left - right)
    return min(difference, 128 - difference)


def signature(support: tuple[int, ...]) -> tuple[int, int, tuple[int, ...]]:
    counts = Counter(distance(left, right) for left, right in combinations(support, 2))
    diameter = counts[64]
    odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
    partition = tuple(sorted((count for chord, count in counts.items() if chord != 64), reverse=True))
    return diameter, odd, partition


def gap_supports() -> tuple[set[tuple[int, ...]], int]:
    two_odd = set()
    six_odd = 0
    for first in range(1, 126):
        for second in range(1, 127 - first):
            for third in range(1, 128 - first - second):
                fourth = 128 - first - second - third
                if fourth <= 0:
                    continue
                support = (0, first, first + second, first + second + third)
                diameter, odd, partition = signature(support)
                if diameter != 0:
                    continue
                if odd == 2:
                    assert partition in ((2, 2, 1, 1), (3, 2, 1))
                    two_odd.add(support)
                elif odd == 6:
                    assert partition == (1, 1, 1, 1, 1, 1)
                    six_odd += 1
    return two_odd, six_odd


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
    assert packet["schema"] == "e1-e30-two-six-odd-light-orbits-v1"
    assert packet["complete"] is True
    assert packet["source_sha256"] == hashlib.sha256(CLASSIFIER.read_bytes()).hexdigest()
    assert packet["normalized_two_odd_supports"] == 8168
    assert packet["normalized_six_odd_supports"] == 280720
    assert packet["two_odd_orbits"] == 87
    assert packet["two_odd_orbit_size_histogram"] == {
        "8": 1, "16": 4, "32": 11, "64": 23, "128": 47, "256": 1,
    }
    assert packet["two_odd_partition_histogram"] == {
        "2,2,1,1": 7920,
        "3,2,1": 248,
    }
    assert packet["two_odd_orbit_partition_histogram"] == {
        "2,2,1,1": 82,
        "3,2,1": 5,
    }
    assert packet["six_odd_orbit_lower_bound"] == 1097

    valid_two, six_count = gap_supports()
    assert len(valid_two) == 8168
    assert six_count == 280720
    covered: set[tuple[int, ...]] = set()
    for row in packet["rows"]:
        representative = tuple(map(int, row["representative"]))
        orbit = normalized_orbit(representative)
        assert len(orbit) == int(row["normalized_count"])
        assert not covered.intersection(orbit)
        covered.update(orbit)
        assert list(signature(representative)[2]) == row["multiplicity_partition"]
    assert covered == valid_two

    assert 1096 * 256 < six_count <= 1097 * 256
    representative_vectors = 1097 * 19_847_936
    assert representative_vectors == 21_773_185_792

    print(
        "E30_TWO_SIX_ODD_LIGHT_ORBIT_CHECK_PASS "
        "two=8168 two_orbits=87 six=280720 six_orbit_lower=1097 "
        "census_floor=21773185792"
    )


if __name__ == "__main__":
    main()
