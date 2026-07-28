#!/usr/bin/env python3
"""Count all normalized multiplicity-one singleton supports by odd chords."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

import modal


app = modal.App("e1-profile-36-mu1-chord-count")
image = modal.Image.debian_slim()


def odd_chord_weight(support: tuple[int, ...]) -> int:
    mask = 0
    for index, left in enumerate(support):
        for right in support[index + 1 :]:
            delta = right - left
            if delta == 64:
                continue
            lag = delta if delta < 64 else 128 - delta
            mask ^= 1 << lag
    return mask.bit_count()


@app.function(image=image, cpu=1.0, memory=128, timeout=60, max_containers=16)
def count(shard: int, shards: int) -> dict[str, object]:
    examined = 0
    mu_one = 0
    weights = Counter()
    for first in range(2 + shard, 125, shards):
        for tail in combinations(range(first + 1, 128), 3):
            support = (0, 1, first) + tail
            examined += 1
            if sum(support) % 2 != 1:
                continue
            mu_one += 1
            weights[odd_chord_weight(support)] += 1
    return {
        "shard": shard,
        "examined": examined,
        "mu_one": mu_one,
        "weights": dict(weights),
    }


@app.local_entrypoint()
def main(shards: int = 16) -> None:
    rows = list(count.starmap((shard, shards) for shard in range(shards)))
    weights = Counter()
    for row in rows:
        weights.update({int(key): int(value) for key, value in row["weights"].items()})
    examined = sum(int(row["examined"]) for row in rows)
    mu_one = sum(int(row["mu_one"]) for row in rows)
    assert examined == 10_009_125
    assert mu_one == 5_005_539
    assert sum(weights.values()) == mu_one
    print(
        "E1_PROFILE_36_MU1_CHORD_COUNT_PASS "
        f"examined={examined} mu_one={mu_one} weights={dict(sorted(weights.items()))}"
    )
