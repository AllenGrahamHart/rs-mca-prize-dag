#!/usr/bin/env python3
"""Classify mu=1 six-sets with at most five odd folded chord classes."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu1-light-chords")
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
    best = None
    for origin in support:
        shifted = tuple((value - origin) % 128 for value in support)
        for unit in range(1, 128, 2):
            image_support = tuple(sorted(unit * value % 128 for value in shifted))
            if best is None or image_support < best:
                best = image_support
    assert best is not None
    return best


@app.function(image=image, cpu=1, memory=1024, timeout=150, max_containers=16)
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
            odd_classes = odd_chord_mask(support).bit_count()
            if odd_classes <= 6:
                retained[odd_classes] += 1
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
    shards: int = 16,
    output: str = "experiments/prize_resolution/e1_profile_36_mu1_light_chord_orbits.json",
) -> None:
    rows = list(classify.starmap((shard, shards) for shard in range(shards)))
    examined = sum(int(row["examined"]) for row in rows)
    mu_one = sum(int(row["mu_one"]) for row in rows)
    retained = Counter()
    orbits: set[tuple[int, ...]] = set()
    for row in rows:
        retained.update({int(key): int(value) for key, value in row["retained"].items()})
        orbits.update(tuple(orbit) for orbit in row["orbits"])

    payload = {
        "schema": "e1-profile-36-mu1-light-chord-orbits-v1",
        "examined": examined,
        "mu_one": mu_one,
        "retained": dict(sorted(retained.items())),
        "affine_orbits": len(orbits),
        "orbits": sorted(orbits),
    }
    output_path = Path(output)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(output_path.read_bytes()).hexdigest()
    print(f"examined={examined} mu_one={mu_one} retained={dict(sorted(retained.items()))}")
    print(f"affine_orbits={len(orbits)} sha256={digest} output={output}")
    assert examined == 10_009_125
    print("E1_PROFILE_36_MU1_LIGHT_CHORD_CLASSIFY_PASS")
