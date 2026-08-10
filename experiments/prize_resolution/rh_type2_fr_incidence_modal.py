#!/usr/bin/env python3
"""Bounded search for an incidence-only countermodel to the FR route."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-rh-type2-fr-incidence")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def search() -> dict:
    import hashlib
    import random
    import time

    m = 64
    field_order = 257
    generator = 3
    subgroup = {pow(generator, 4 * j, field_order) for j in range(m)}
    cosets = [
        {(pow(generator, i, field_order) * x) % field_order for x in subgroup}
        for i in range(4)
    ]
    if set().union(*cosets) != set(range(1, field_order)):
        return {"status": "void", "reason": "cosets_do_not_partition"}
    if sum(len(coset) for coset in cosets) != field_order - 1:
        return {"status": "void", "reason": "cosets_not_disjoint"}

    domain = [(i, x) for i in range(4) for x in range(1, field_order)]
    blocks = {}
    for gamma in range(field_order):
        block = {
            (i, (gamma + a) % field_order)
            for i, coset in enumerate(cosets)
            for a in coset
            if (gamma + a) % field_order != 0
        }
        if gamma == 0:
            block.remove((0, 1))
        blocks[gamma] = block

    sizes = {gamma: len(block) for gamma, block in blocks.items()}
    degrees = {
        point: sum(point in block for block in blocks.values()) for point in domain
    }
    pair_intersections = {
        (g, h): len(blocks[g] & blocks[h])
        for g in range(field_order)
        for h in range(g + 1, field_order)
    }
    if set(sizes.values()) != {4 * m - 1}:
        return {"status": "void", "reason": "block_size", "sizes": sizes}
    if sorted(degrees.values()) != [m - 1] + [m] * (16 * m - 1):
        return {"status": "void", "reason": "degree_profile"}
    if max(pair_intersections.values()) > m - 1:
        return {"status": "void", "reason": "pair_overlap"}

    rng = random.Random(0xF17)
    anchor = sorted(blocks[0])
    outside = sorted(set(domain) - blocks[0])
    deadline = time.monotonic() + 50.0
    trials = 0
    while time.monotonic() < deadline:
        trials += 1
        w_set = set(rng.sample(anchor, 3 * m - 3))
        w_set.update(rng.sample(outside, 4 * m + 2))
        intersections = {
            gamma: len(block & w_set) for gamma, block in blocks.items()
        }
        if max(intersections.values()) > 3 * m - 3:
            continue
        spends = {
            gamma: len(block - w_set) for gamma, block in blocks.items()
        }
        if min(spends.values()) < m + 2:
            continue
        unions = {
            f"{g},{h}": len(blocks[g] | blocks[h])
            for g in range(field_order)
            for h in range(g + 1, field_order)
        }
        mask = 0
        for i, x in w_set:
            mask |= 1 << (i * (field_order - 1) + x - 1)
        mask_bytes = mask.to_bytes(len(domain) // 8, "little")
        return {
            "status": "witness",
            "trials": trials,
            "m": m,
            "N": len(domain),
            "rho": 4 * m - 1,
            "T": len(blocks),
            "a": len(w_set),
            "deficit": sum(m - degree for degree in degrees.values()),
            "minimum_pair_union": min(unions.values()),
            "minimum_spend": min(spends.values()),
            "maximum_intersection_with_W": max(intersections.values()),
            "maximizers": [
                gamma
                for gamma, value in intersections.items()
                if value == max(intersections.values())
            ],
            "W_bitset_hex_little_endian": mask_bytes.hex(),
            "W_sha256": hashlib.sha256(mask_bytes).hexdigest(),
            "block_intersections_with_W": intersections,
        }
    return {"status": "no_witness", "trials": trials}


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(search.remote(), sort_keys=True))
