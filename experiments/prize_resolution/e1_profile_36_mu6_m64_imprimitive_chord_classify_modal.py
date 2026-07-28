#!/usr/bin/env python3
"""Classify the all-one-parity multiplicity-six singleton supports."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu6-m64-imprimitive-chords")
image = modal.Image.debian_slim()


def multiplicity64(support: tuple[int, ...]) -> int:
    for derivative in range(16):
        if sum((derivative & ~exponent) == 0 for exponent in support) % 2:
            return derivative
    return 16


def odd_chord_mask128(support: tuple[int, ...]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            if delta == 64:
                continue
            lag = delta if delta < 64 else 128 - delta
            mask ^= 1 << (lag - 1)
    return mask


def canonical64(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted(unit * ((value - origin) % 64) % 64 for value in support))
        for origin in support
        for unit in range(1, 64, 2)
    )


@app.function(image=image, cpu=1.0, memory=192, timeout=90, max_containers=16)
def classify(shard: int, shards: int) -> dict[str, object]:
    examined = 0
    mu_three = 0
    weights = Counter()
    orbits: set[tuple[int, ...]] = set()
    for first in range(2 + shard, 61, shards):
        for tail in combinations(range(first + 1, 64), 3):
            support64 = (0, 1, first) + tail
            examined += 1
            if multiplicity64(support64) != 3:
                continue
            mu_three += 1
            lifted = tuple(2 * value for value in support64)
            weights[odd_chord_mask128(lifted).bit_count()] += 1
            orbits.add(canonical64(support64))
    return {
        "shard": shard,
        "examined": examined,
        "mu_three": mu_three,
        "weights": dict(weights),
        "orbits64": sorted(orbits),
    }


@app.local_entrypoint()
def main(
    shards: int = 16,
    output: str = (
        "experiments/prize_resolution/"
        "e1_profile_36_mu6_m64_imprimitive_chord_orbits.json"
    ),
) -> None:
    rows = list(classify.starmap((shard, shards) for shard in range(shards)))
    weights = Counter()
    orbits64: set[tuple[int, ...]] = set()
    for row in rows:
        weights.update({int(key): int(value) for key, value in row["weights"].items()})
        orbits64.update(tuple(orbit) for orbit in row["orbits64"])
    lifted_orbits = sorted(tuple(2 * value for value in orbit) for orbit in orbits64)
    payload = {
        "schema": "e1-profile-36-mu6-m64-imprimitive-chord-orbits-v1",
        "examined": sum(int(row["examined"]) for row in rows),
        "mu_three_normalized": sum(int(row["mu_three"]) for row in rows),
        "weights": dict(sorted(weights.items())),
        "orbit_weights": dict(sorted(Counter(
            odd_chord_mask128(orbit).bit_count() for orbit in lifted_orbits
        ).items())),
        "affine_orbits": len(lifted_orbits),
        "orbits": lifted_orbits,
    }
    assert payload["examined"] == 557845
    path = Path(output)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU6_M64_IMPRIMITIVE_CHORDS_PASS "
        f"examined={payload['examined']} mu3={payload['mu_three_normalized']} "
        f"weights={payload['weights']} orbit_weights={payload['orbit_weights']} "
        f"affine_orbits={payload['affine_orbits']}"
    )
    print(f"sha256={hashlib.sha256(path.read_bytes()).hexdigest()} output={output}")


if __name__ == "__main__":
    main()
