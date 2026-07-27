#!/usr/bin/env python3
"""Classify four-odd E32 light supports under affine odd-unit transport."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = HERE / "e32_four_odd_light_orbit_result.json"
UNITS = tuple(range(1, 128, 2))


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def distance_counts(support: tuple[int, ...]) -> Counter[int]:
    return Counter(distance(left, right) for left, right in combinations(support, 2))


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * (value - anchor)) % 128 for value in support))
        for anchor in support
        for unit in UNITS
    )


def main() -> None:
    orbit_counts: defaultdict[tuple[int, ...], int] = defaultdict(int)
    normalized = 0
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        counts = distance_counts(support)
        diameter_count = counts[64]
        odd_count = sum(count % 2 for chord, count in counts.items() if chord != 64)
        if diameter_count not in (0, 2) or odd_count != 4:
            continue
        normalized += 1
        assert diameter_count == 0
        assert sorted(counts.values(), reverse=True) == [2, 1, 1, 1, 1]
        orbit_counts[canonical(support)] += 1

    rows = []
    for representative, count in sorted(orbit_counts.items()):
        counts = distance_counts(representative)
        repeated = next(chord for chord, multiplicity in counts.items() if multiplicity == 2)
        repeated_edges = [
            frozenset((left, right))
            for left, right in combinations(representative, 2)
            if distance(left, right) == repeated
        ]
        repeated_shape = "wedge" if repeated_edges[0] & repeated_edges[1] else "matching"
        rows.append(
            {
                "representative": list(representative),
                "normalized_count": count,
                "repeated_distance": repeated,
                "repeated_shape": repeated_shape,
            }
        )
    packet = {
        "schema": "e1-e32-four-odd-light-orbits-v1",
        "complete": True,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "normalized_supports": normalized,
        "orbits": len(rows),
        "normalized_orbit_size_histogram": {
            str(size): count for size, count in sorted(Counter(orbit_counts.values()).items())
        },
        "repeated_shape_histogram": dict(sorted(Counter(row["repeated_shape"] for row in rows).items())),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E32_FOUR_ODD_LIGHT_ORBIT_CLASSIFIER_PASS "
        f"normalized={normalized} orbits={len(rows)} "
        f"sizes={packet['normalized_orbit_size_histogram']} "
        f"shapes={packet['repeated_shape_histogram']}"
    )


if __name__ == "__main__":
    main()
