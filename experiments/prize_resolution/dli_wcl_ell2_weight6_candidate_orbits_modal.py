#!/usr/bin/env python3
"""Count weight-six router candidates modulo dilation and triple rebasing."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-dli-wcl-weight6-candidate-orbits")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=2, memory=4096, timeout=300)
def census(order: int = 1024) -> dict[str, object]:
    import hashlib
    from collections import Counter, defaultdict
    from itertools import combinations

    half = order // 2
    units = tuple(range(1, order, 2))
    available = tuple(value for value in range(1, order) if value != half)
    legal_pairs = {
        pair
        for pair in combinations(available, 2)
        if (pair[1] - pair[0]) % order != half
    }

    unseen = set(legal_pairs)
    pair_representative: dict[tuple[int, int], tuple[int, int]] = {}
    canonicalizers: dict[tuple[int, int], tuple[int, ...]] = {}
    representatives = []
    pair_orbit_histogram: Counter[int] = Counter()

    while unseen:
        seed = min(unseen)
        images: dict[tuple[int, int], list[int]] = defaultdict(list)
        for unit in units:
            image_pair = tuple(
                sorted((unit * seed[0] % order, unit * seed[1] % order))
            )
            images[image_pair].append(unit)
        representative = min(images)
        representative_units = images[representative]
        representatives.append(representative)
        pair_orbit_histogram[len(images)] += 1
        for pair, seed_to_pair_units in images.items():
            seed_to_pair = seed_to_pair_units[0]
            inverse = pow(seed_to_pair, -1, order)
            maps_to_representative = tuple(
                sorted(unit * inverse % order for unit in representative_units)
            )
            pair_representative[pair] = representative
            canonicalizers[pair] = maps_to_representative
        unseen.difference_update(images)

    if len(pair_representative) != len(legal_pairs):
        raise AssertionError("pair orbit partition incomplete")

    def canonical_key(a: int, b: int, product: int) -> tuple[int, int, int]:
        presentations = (
            ((a, b), product),
            ((-a % order, b - a), product - 3 * a),
            ((-b % order, a - b), product - 3 * b),
        )
        keys = []
        for raw_pair, raw_product in presentations:
            pair = tuple(sorted(value % order for value in raw_pair))
            representative = pair_representative[pair]
            for unit in canonicalizers[pair]:
                keys.append(
                    (
                        representative[0],
                        representative[1],
                        unit * raw_product % order,
                    )
                )
        return min(keys)

    multiplicities: Counter[tuple[int, int, int]] = Counter()
    for a, b in sorted(representatives):
        for product in range(order):
            multiplicities[canonical_key(a, b, product)] += 1

    keys = sorted(multiplicities)
    digest = hashlib.sha256()
    for key in keys:
        digest.update(f"{key[0]},{key[1]},{key[2]}\n".encode())

    # Every generator preserves the canonical key.
    controls = 0
    for key in keys[:: max(1, len(keys) // 257)]:
        a, b, product = key
        for unit in (1, 3, 511, 513, 1023):
            if canonical_key(
                unit * a % order,
                unit * b % order,
                unit * product % order,
            ) != key:
                raise AssertionError("dilation canonicalization")
            controls += 1
        for raw_pair, raw_product in (
            ((-a % order, b - a), product - 3 * a),
            ((-b % order, a - b), product - 3 * b),
        ):
            if canonical_key(raw_pair[0], raw_pair[1], raw_product % order) != key:
                raise AssertionError("rebase canonicalization")
            controls += 1

    return {
        "schema": "dli-wcl-ell2-weight6-candidate-orbits-v1",
        "order": order,
        "legal_pairs": len(legal_pairs),
        "pair_orbits": len(representatives),
        "pair_orbit_size_histogram": dict(sorted(pair_orbit_histogram.items())),
        "router_presentations": len(representatives) * order,
        "candidate_orbits": len(keys),
        "presentation_multiplicity_histogram": dict(
            sorted(Counter(multiplicities.values()).items())
        ),
        "representative_digest": digest.hexdigest(),
        "canonicalization_controls": controls,
        "status": "COMPLETE",
    }


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(census.remote(), sort_keys=True))
