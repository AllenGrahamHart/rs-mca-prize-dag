#!/usr/bin/env python3
"""Classify the nine live cofactor-514 singleton-support strata."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu1-m514-chord-classify")
image = modal.Image.debian_slim()


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


@app.function(image=image, cpu=1.0, memory=512, timeout=180, max_containers=32)
def classify(shard: int, shards: int) -> dict[str, object]:
    examined = 0
    mu_one = 0
    retained = Counter()
    orbits: set[tuple[int, ...]] = set()
    for first in range(2 + shard, 125, shards):
        for tail in combinations(range(first + 1, 128), 3):
            support = (0, 1, first) + tail
            examined += 1
            if sum(support) % 2 != 1:
                continue
            mu_one += 1
            weight = odd_chord_mask(support).bit_count()
            if 3 <= weight <= 11:
                retained[weight] += 1
                orbits.add(canonical(support))
    return {
        "shard": shard,
        "examined": examined,
        "mu_one": mu_one,
        "retained": dict(retained),
        "orbits": sorted(orbits),
    }


@app.local_entrypoint()
def main(
    shards: int = 32,
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_mu1_m514_chord_orbits.json"
    ),
) -> None:
    rows = list(classify.starmap((shard, shards) for shard in range(shards)))
    retained = Counter()
    orbits: set[tuple[int, ...]] = set()
    for row in rows:
        retained.update({int(key): int(value) for key, value in row["retained"].items()})
        orbits.update(tuple(orbit) for orbit in row["orbits"])
    payload = {
        "schema": "e1-profile-36-mu1-m514-chord-orbits-v1",
        "examined": sum(int(row["examined"]) for row in rows),
        "mu_one": sum(int(row["mu_one"]) for row in rows),
        "retained": dict(sorted(retained.items())),
        "orbit_weights": dict(
            sorted(Counter(odd_chord_mask(orbit).bit_count() for orbit in orbits).items())
        ),
        "affine_orbits": len(orbits),
        "orbits": sorted(orbits),
    }
    output_path = Path(output)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU1_M514_CHORD_CLASSIFY_PASS "
        f"examined={payload['examined']} mu_one={payload['mu_one']} "
        f"retained={payload['retained']} orbit_weights={payload['orbit_weights']} "
        f"affine_orbits={payload['affine_orbits']}"
    )
    print(f"sha256={hashlib.sha256(output_path.read_bytes()).hexdigest()} output={output}")
    assert payload["examined"] == 10_009_125
    assert payload["mu_one"] == 5_005_539
