#!/usr/bin/env python3
"""Classify all affine six-singleton supports of exact multiplicity four."""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path

import modal


app = modal.App("e1-profile-36-mu4-m16-chords")
image = modal.Image.debian_slim()

BRANCHES = {
    "primitive": {"modulus": 128, "multiplicity": 4, "lift": 1, "shards": 16},
    "one_division": {"modulus": 64, "multiplicity": 2, "lift": 2, "shards": 4},
    "two_divisions": {"modulus": 32, "multiplicity": 1, "lift": 4, "shards": 1},
}


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
            mask ^= 1 << (lag - 1)
    return mask


def canonical(support: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    return min(
        tuple(sorted(unit * ((value - origin) % modulus) % modulus for value in support))
        for origin in support
        for unit in range(1, modulus, 2)
    )


@app.function(image=image, cpu=1.0, memory=256, timeout=120, max_containers=21)
def classify(branch: str, shard: int) -> dict[str, object]:
    spec = BRANCHES[branch]
    modulus = int(spec["modulus"])
    target = int(spec["multiplicity"])
    lift = int(spec["lift"])
    shards = int(spec["shards"])
    examined = 0
    matching = 0
    weights = Counter()
    orbits: set[tuple[int, ...]] = set()
    for first in range(2 + shard, modulus - 3, shards):
        for tail in combinations(range(first + 1, modulus), 3):
            support = (0, 1, first) + tail
            examined += 1
            if multiplicity(support) != target:
                continue
            matching += 1
            representative = canonical(support, modulus)
            lifted = tuple(lift * value for value in representative)
            weights[odd_chord_mask(lifted).bit_count()] += 1
            orbits.add(lifted)
    return {
        "branch": branch,
        "shard": shard,
        "examined": examined,
        "matching": matching,
        "weights": dict(weights),
        "orbits": sorted(orbits),
    }


@app.local_entrypoint()
def main(
    output: str = "experiments/prize_resolution/e1_profile_36_mu4_m16_chord_orbits.json",
) -> None:
    tasks = [
        (branch, shard)
        for branch, spec in BRANCHES.items()
        for shard in range(int(spec["shards"]))
    ]
    rows = list(classify.starmap(tasks, order_outputs=True))
    payload_branches: dict[str, object] = {}
    combined_orbits: set[tuple[int, ...]] = set()
    for branch, spec in BRANCHES.items():
        branch_rows = [row for row in rows if row["branch"] == branch]
        weights = Counter()
        orbits: set[tuple[int, ...]] = set()
        for row in branch_rows:
            weights.update({int(key): int(value) for key, value in row["weights"].items()})
            orbits.update(tuple(orbit) for orbit in row["orbits"])
        combined_orbits.update(orbits)
        payload_branches[branch] = {
            "modulus": spec["modulus"],
            "quotient_multiplicity": spec["multiplicity"],
            "lift": spec["lift"],
            "examined": sum(int(row["examined"]) for row in branch_rows),
            "matching": sum(int(row["matching"]) for row in branch_rows),
            "weights": dict(sorted(weights.items())),
            "orbit_weights": dict(sorted(Counter(
                odd_chord_mask(orbit).bit_count() for orbit in orbits
            ).items())),
            "affine_orbits": len(orbits),
            "orbits": sorted(orbits),
        }
    assert payload_branches["primitive"]["examined"] == 10009125
    assert payload_branches["one_division"]["examined"] == 557845
    assert payload_branches["two_divisions"]["examined"] == 27405
    assert sum(branch["affine_orbits"] for branch in payload_branches.values()) == len(combined_orbits)
    payload = {
        "schema": "e1-profile-36-mu4-m16-chord-orbits-v1",
        "branches": payload_branches,
        "affine_orbits": len(combined_orbits),
        "orbit_weights": dict(sorted(Counter(
            odd_chord_mask(orbit).bit_count() for orbit in combined_orbits
        ).items())),
        "orbits": sorted(combined_orbits),
    }
    path = Path(output)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU4_M16_CHORDS_PASS "
        f"branches={[(name, value['matching'], value['affine_orbits']) for name, value in payload_branches.items()]} "
        f"orbit_weights={payload['orbit_weights']} affine_orbits={payload['affine_orbits']}"
    )
    print(f"sha256={hashlib.sha256(path.read_bytes()).hexdigest()} output={output}")


if __name__ == "__main__":
    main()
