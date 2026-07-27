#!/usr/bin/env python3
"""Classify the E30 two-odd light branch and count the six-odd branch."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULT = HERE / "e30_two_six_odd_light_orbit_result.json"
UNITS = tuple(range(1, 128, 2))


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * (value - anchor)) % 128 for value in support))
        for anchor in support
        for unit in UNITS
    )


def main() -> None:
    odd_counts: Counter[int] = Counter()
    partition_counts: Counter[tuple[int, tuple[int, ...]]] = Counter()
    two_odd_orbits: defaultdict[tuple[int, ...], int] = defaultdict(int)
    orbit_partition: dict[tuple[int, ...], tuple[int, ...]] = {}

    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        counts = Counter(distance(left, right) for left, right in combinations(support, 2))
        diameter = counts[64]
        odd = sum(count % 2 for chord, count in counts.items() if chord != 64)
        odd_counts[(diameter << 4) | odd] += 1
        if diameter != 0 or odd not in (2, 6):
            continue
        partition = tuple(sorted((count for chord, count in counts.items() if chord != 64), reverse=True))
        partition_counts[(odd, partition)] += 1
        if odd == 2:
            representative = canonical(support)
            two_odd_orbits[representative] += 1
            previous = orbit_partition.setdefault(representative, partition)
            assert previous == partition

    two_odd = sum(two_odd_orbits.values())
    six_odd = partition_counts[(6, (1, 1, 1, 1, 1, 1))]
    rows = [
        {
            "representative": list(representative),
            "normalized_count": count,
            "multiplicity_partition": list(orbit_partition[representative]),
        }
        for representative, count in sorted(two_odd_orbits.items())
    ]
    packet = {
        "schema": "e1-e30-two-six-odd-light-orbits-v1",
        "complete": True,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "normalized_two_odd_supports": two_odd,
        "normalized_six_odd_supports": six_odd,
        "two_odd_orbits": len(rows),
        "two_odd_orbit_size_histogram": {
            str(size): count
            for size, count in sorted(Counter(two_odd_orbits.values()).items())
        },
        "two_odd_partition_histogram": {
            ",".join(map(str, partition)): count
            for (odd, partition), count in sorted(partition_counts.items())
            if odd == 2
        },
        "two_odd_orbit_partition_histogram": {
            ",".join(map(str, partition)): count
            for partition, count in sorted(Counter(orbit_partition.values()).items())
        },
        "six_odd_partition_histogram": {
            "1,1,1,1,1,1": six_odd,
        },
        "six_odd_orbit_lower_bound": math.ceil(six_odd / 256),
        "all_diameter_odd_counts": {
            f"{key >> 4},{key & 15}": count for key, count in sorted(odd_counts.items())
        },
        "rows": rows,
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E30_TWO_SIX_ODD_LIGHT_ORBIT_CLASSIFIER_PASS "
        f"two={two_odd} two_orbits={len(rows)} six={six_odd} "
        f"six_orbit_lower={packet['six_odd_orbit_lower_bound']}"
    )


if __name__ == "__main__":
    main()
