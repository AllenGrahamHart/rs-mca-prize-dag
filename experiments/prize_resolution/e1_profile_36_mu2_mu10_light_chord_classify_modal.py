#!/usr/bin/env python3
"""Classify low-chord six-sets at multiplicities two and ten."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu2-mu10-light-chords")
image = modal.Image.debian_slim()
TARGETS = (2, 10)


def multiplicity(support: tuple[int, ...]) -> int:
    for derivative in range(16):
        if sum((derivative & ~exponent) == 0 for exponent in support) % 2:
            return derivative
    return 16


def odd_chord_mask(support: tuple[int, ...]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            if delta == 64:
                continue
            lag = delta if delta < 64 else 128 - delta
            mask ^= 1 << lag
    return mask


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted(unit * ((value - origin) % 128) % 128 for value in support))
        for origin in support
        for unit in range(1, 128, 2)
    )


@app.function(image=image, cpu=1.0, memory=512, timeout=120, max_containers=16)
def classify(shard: int, shards: int) -> dict[str, object]:
    examined = 0
    multiplicity_counts = Counter()
    retained = {target: Counter() for target in TARGETS}
    orbits = {target: set() for target in TARGETS}
    available = [position for position in range(128) if position not in (0, 2)]
    for first_index in range(shard, 123, shards):
        for tail_indices in combinations(range(first_index + 1, 126), 3):
            indices = (first_index,) + tail_indices
            support = tuple(sorted((0, 2, *(available[index] for index in indices))))
            examined += 1
            mu = multiplicity(support)
            if mu not in TARGETS:
                continue
            multiplicity_counts[mu] += 1
            odd_classes = odd_chord_mask(support).bit_count()
            if odd_classes <= 6:
                retained[mu][odd_classes] += 1
                orbits[mu].add(canonical(support))
    return {
        "shard": shard,
        "examined": examined,
        "multiplicity_counts": dict(multiplicity_counts),
        "retained": {str(mu): dict(counts) for mu, counts in retained.items()},
        "orbits": {str(mu): sorted(values) for mu, values in orbits.items()},
    }


@app.local_entrypoint()
def main(
    shards: int = 16,
    output: str = "experiments/prize_resolution/e1_profile_36_mu2_mu10_light_chord_orbits.json",
) -> None:
    rows = list(classify.starmap((shard, shards) for shard in range(shards)))
    multiplicity_counts = Counter()
    retained = {target: Counter() for target in TARGETS}
    orbits = {target: set() for target in TARGETS}
    for row in rows:
        multiplicity_counts.update(
            {int(key): int(value) for key, value in row["multiplicity_counts"].items()}
        )
        for target in TARGETS:
            retained[target].update(
                {
                    int(key): int(value)
                    for key, value in row["retained"][str(target)].items()
                }
            )
            orbits[target].update(
                tuple(orbit) for orbit in row["orbits"][str(target)]
            )

    payload = {
        "schema": "e1-profile-36-mu2-mu10-light-chord-orbits-v1",
        "examined": sum(int(row["examined"]) for row in rows),
        "anchor": [0, 2],
        "multiplicity_counts": dict(sorted(multiplicity_counts.items())),
        "targets": {
            str(target): {
                "retained": dict(sorted(retained[target].items())),
                "affine_orbits": len(orbits[target]),
                "orbits": sorted(orbits[target]),
            }
            for target in TARGETS
        },
    }
    output_path = Path(output)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(output_path.read_bytes()).hexdigest()
    print(
        f"examined={payload['examined']} multiplicity_counts={payload['multiplicity_counts']}"
    )
    for target in TARGETS:
        print(
            f"mu={target} retained={payload['targets'][str(target)]['retained']} "
            f"affine_orbits={payload['targets'][str(target)]['affine_orbits']}"
        )
    print(f"sha256={digest} output={output}")
    assert payload["examined"] == 10_009_125
    print("E1_PROFILE_36_MU2_MU10_LIGHT_CHORD_CLASSIFY_PASS")
