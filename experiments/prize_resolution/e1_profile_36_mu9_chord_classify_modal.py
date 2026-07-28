#!/usr/bin/env python3
"""Classify all affine six-singleton supports of exact multiplicity nine."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu9-chords")
image = modal.Image.debian_slim()


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
    mu9 = 0
    weights = Counter()
    orbits: set[tuple[int, ...]] = set()
    for first in range(2 + shard, 125, shards):
        for tail in combinations(range(first + 1, 128), 3):
            support = (0, 1, first) + tail
            examined += 1
            if multiplicity(support) != 9:
                continue
            mu9 += 1
            weights[odd_chord_mask(support).bit_count()] += 1
            orbits.add(canonical(support))
    return {
        "shard": shard,
        "examined": examined,
        "mu9": mu9,
        "weights": dict(weights),
        "orbits": sorted(orbits),
    }


@app.local_entrypoint()
def main(
    shards: int = 16,
    output: str = "experiments/prize_resolution/e1_profile_36_mu9_chord_orbits.json",
) -> None:
    rows = list(classify.starmap((shard, shards) for shard in range(shards)))
    weights = Counter()
    orbits: set[tuple[int, ...]] = set()
    for row in rows:
        weights.update({int(key): int(value) for key, value in row["weights"].items()})
        orbits.update(tuple(orbit) for orbit in row["orbits"])
    payload = {
        "schema": "e1-profile-36-mu9-chord-orbits-v1",
        "examined": sum(int(row["examined"]) for row in rows),
        "mu9": sum(int(row["mu9"]) for row in rows),
        "weights": dict(sorted(weights.items())),
        "orbit_weights": dict(
            sorted(Counter(odd_chord_mask(orbit).bit_count() for orbit in orbits).items())
        ),
        "affine_orbits": len(orbits),
        "orbits": sorted(orbits),
    }
    output_path = Path(output)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"examined={payload['examined']} mu9={payload['mu9']} "
        f"weights={payload['weights']} orbit_weights={payload['orbit_weights']} "
        f"affine_orbits={payload['affine_orbits']}"
    )
    print(f"sha256={hashlib.sha256(output_path.read_bytes()).hexdigest()} output={output}")
    assert payload["examined"] == 10_009_125
    print("E1_PROFILE_36_MU9_CHORD_CLASSIFY_PASS")
