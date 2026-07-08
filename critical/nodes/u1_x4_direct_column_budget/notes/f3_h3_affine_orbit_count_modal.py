#!/usr/bin/env python3
"""Burnside count for n=96 h=3 disjoint-pair shapes modulo affine symmetries."""

from __future__ import annotations

import modal


app = modal.App("rs-mca-h3-affine-orbit-count")
image = modal.Image.debian_slim()

N = 96
N_SHARDS = 16


def unit_group() -> list[int]:
    import math

    return [u for u in range(N) if math.gcd(u, N) == 1]


def group_elements() -> list[tuple[int, int]]:
    return [(u, s) for u in unit_group() for s in range(N)]


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def burnside_shard(shard: int) -> dict:
    import itertools

    triples = list(itertools.combinations(range(N), 3))
    index = {t: i for i, t in enumerate(triples)}
    masks = [(1 << a) | (1 << b) | (1 << c) for a, b, c in triples]
    raw_objects = len(triples) * (len(list(itertools.combinations(range(N - 3), 3)))) // 2

    def image_index(trans, triple):
        vals = [trans[triple[0]], trans[triple[1]], trans[triple[2]]]
        vals.sort()
        return index[(vals[0], vals[1], vals[2])]

    def fixed_unordered_pairs_for(u: int, s: int) -> int:
        if u == 1 and s == 0:
            return raw_objects
        trans = [(u * x + s) % N for x in range(N)]
        mapping = [0] * len(triples)
        fixed = []
        for i, triple in enumerate(triples):
            j = image_index(trans, triple)
            mapping[i] = j
            if j == i:
                fixed.append(i)

        fixed_individual = 0
        for pos, i in enumerate(fixed):
            mi = masks[i]
            for j in fixed[pos + 1 :]:
                if mi & masks[j] == 0:
                    fixed_individual += 1

        swapped = 0
        for i, j in enumerate(mapping):
            if i < j and mapping[j] == i and (masks[i] & masks[j]) == 0:
                swapped += 1
        return fixed_individual + swapped

    elems = group_elements()
    mine = elems[shard::N_SHARDS]
    total = 0
    max_fixed = 0
    max_elem = None
    for u, s in mine:
        f = fixed_unordered_pairs_for(u, s)
        total += f
        if f > max_fixed:
            max_fixed = f
            max_elem = (u, s)
    return {
        "shard": shard,
        "elements": len(mine),
        "fixed_sum": total,
        "max_fixed": max_fixed,
        "max_elem": max_elem,
    }


@app.local_entrypoint()
def main():
    elems = group_elements()
    results = []
    for item in burnside_shard.map(range(N_SHARDS), return_exceptions=True):
        if isinstance(item, Exception):
            print(f"SHARD_ERROR {item!r}")
            continue
        results.append(item)
        print(
            f"shard={item['shard']} elements={item['elements']} "
            f"fixed_sum={item['fixed_sum']} max_fixed={item['max_fixed']} "
            f"max_elem={item['max_elem']}"
        )
    fixed_total = sum(r["fixed_sum"] for r in results)
    group_order = len(elems)
    print(f"GROUP_ORDER {group_order}")
    print(f"FIXED_TOTAL {fixed_total}")
    if fixed_total % group_order:
        raise AssertionError((fixed_total, group_order, fixed_total % group_order))
    print(f"AFFINE_ORBITS {fixed_total // group_order}")
    print("H3_AFFINE_ORBIT_COUNT_PASS")


if __name__ == "__main__":
    main()
