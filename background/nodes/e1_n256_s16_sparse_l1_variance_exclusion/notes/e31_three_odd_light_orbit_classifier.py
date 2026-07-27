#!/usr/bin/env python3
"""Classify the three-odd E31 light supports under affine odd units."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = HERE / "e31_three_odd_light_orbit_result.json"
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


def repeated_shape(support: tuple[int, ...], repeated: int) -> str:
    edges = [
        (left, right)
        for left, right in combinations(support, 2)
        if distance(left, right) == repeated
    ]
    degrees = Counter(vertex for edge in edges for vertex in edge)
    degree_sequence = tuple(sorted((degrees[vertex] for vertex in support), reverse=True))
    names = {
        (3, 1, 1, 1): "star",
        (2, 2, 1, 1): "path",
        (2, 2, 2, 0): "triangle",
        (2, 1, 1, 0): "wedge",
        (1, 1, 1, 1): "matching",
    }
    return names.get(degree_sequence, "degrees-" + "-".join(map(str, degree_sequence)))


def main() -> None:
    orbit_counts: defaultdict[tuple[int, ...], int] = defaultdict(int)
    normalized = 0
    partition_histogram: Counter[tuple[int, ...]] = Counter()
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        counts = distance_counts(support)
        if counts[64] != 1:
            continue
        odd_count = sum(count % 2 for chord, count in counts.items() if chord != 64)
        if odd_count != 3:
            continue
        normalized += 1
        partition = tuple(
            sorted(
                (count for chord, count in counts.items() if chord != 64),
                reverse=True,
            )
        )
        assert partition in ((3, 1, 1), (2, 1, 1, 1))
        partition_histogram[partition] += 1
        orbit_counts[canonical(support)] += 1

    rows = []
    for representative, count in sorted(orbit_counts.items()):
        counts = distance_counts(representative)
        repeated, multiplicity = max(
            (
                (chord, amount)
                for chord, amount in counts.items()
                if chord != 64
            ),
            key=lambda item: item[1],
        )
        partition = tuple(
            sorted(
                (amount for chord, amount in counts.items() if chord != 64),
                reverse=True,
            )
        )
        rows.append(
            {
                "representative": list(representative),
                "normalized_count": count,
                "multiplicity_partition": list(partition),
                "repeated_distance": repeated,
                "repeated_multiplicity": multiplicity,
                "repeated_shape": repeated_shape(representative, repeated),
            }
        )

    packet = {
        "schema": "e1-e31-three-odd-light-orbits-v1",
        "complete": True,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "normalized_supports": normalized,
        "orbits": len(rows),
        "normalized_orbit_size_histogram": {
            str(size): count
            for size, count in sorted(Counter(orbit_counts.values()).items())
        },
        "partition_histogram": {
            ",".join(map(str, partition)): count
            for partition, count in sorted(partition_histogram.items())
        },
        "orbit_partition_histogram": dict(
            sorted(
                Counter(
                    ",".join(map(str, row["multiplicity_partition"]))
                    for row in rows
                ).items()
            )
        ),
        "repeated_shape_histogram": dict(
            sorted(Counter(row["repeated_shape"] for row in rows).items())
        ),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E31_THREE_ODD_LIGHT_ORBIT_CLASSIFIER_PASS "
        f"normalized={normalized} orbits={len(rows)} "
        f"partitions={packet['partition_histogram']} "
        f"sizes={packet['normalized_orbit_size_histogram']} "
        f"shapes={packet['repeated_shape_histogram']}"
    )


if __name__ == "__main__":
    main()
