#!/usr/bin/env python3
"""Sub-dollar weighted-multistar alignment pilot for the H3 router.

Decision: measure whether incident distance deficit at least four compresses
the complete toy-order two-leaf ideal-star survivor lists. The two Modal
functions run sequentially with one CPU, 1 GiB RAM, a 120-second hard timeout,
and max_containers=1. Completed orders are checkpointed locally.
"""

from __future__ import annotations

import json
from pathlib import Path

import modal


INPUT = Path(__file__).with_name("h3_low_distance_ideal_star_alignment_pilot_result.json")
OUTPUT = Path(__file__).with_name("h3_weighted_multistar_alignment_pilot_result.json")
app = modal.App("rs-mca-h3-weighted-multistar-alignment-pilot")
image = modal.Image.debian_slim()


@app.function(image=image, cpu=1, memory=1024, timeout=120, max_containers=1)
def screen(order: int, primes: list[int]) -> dict[str, object]:
    import collections
    import itertools
    import time

    started = time.monotonic()
    half = order // 2
    pairs = list(itertools.combinations_with_replacement(range(1, order), 2))

    def vector(pair: tuple[int, int]) -> dict[int, int]:
        out: collections.Counter[int] = collections.Counter()
        for exponent, coefficient in (
            ((pair[0] + pair[1]) % order, 1),
            (pair[0], -1),
            (pair[1], -1),
        ):
            if exponent >= half:
                exponent -= half
                coefficient = -coefficient
            out[exponent] += coefficient
        return {key: value for key, value in out.items() if value}

    def distance(left: dict[int, int], right: dict[int, int]) -> int:
        return sum(
            (left.get(key, 0) - right.get(key, 0)) ** 2
            for key in left.keys() | right.keys()
        )

    all_vectors = [vector(pair) for pair in pairs]
    small_pairs = [
        pair for pair, value in zip(pairs, all_vectors)
        if sum(coefficient * coefficient for coefficient in value.values()) <= 3
    ]
    small_vectors = [vector(pair) for pair in small_pairs]
    distance_four: list[int] = []
    distance_six: list[int] = []
    for left, left_vector in enumerate(small_vectors):
        mask_four = 0
        mask_six = 0
        for right, right_vector in enumerate(small_vectors):
            if left == right:
                continue
            square = distance(left_vector, right_vector)
            if square == 4:
                mask_four |= 1 << right
            elif square == 6:
                mask_six |= 1 << right
        distance_four.append(mask_four)
        distance_six.append(mask_six)

    def order_root(prime: int) -> int:
        exponent = (prime - 1) // order
        for base in range(2, 10_000):
            root = pow(base, exponent, prime)
            if pow(root, half, prime) == prime - 1:
                return root
        raise AssertionError((prime, "no order root"))

    survivors: list[int] = []
    surviving_fibers = 0
    maximum_weighted_degree = 0
    maximum_small_fiber = 0
    for prime_index, prime in enumerate(primes, start=1):
        if prime_index % 100 == 0:
            print(
                "H3_WEIGHTED_MULTISTAR_PROGRESS "
                f"order={order} primes={prime_index}/{len(primes)} "
                f"survivors={len(survivors)} elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )
        root = order_root(prime)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        fibers: dict[int, int] = {}
        for index, (left, right) in enumerate(small_pairs):
            target = ((1 - powers[left]) * (1 - powers[right])) % prime
            fibers[target] = fibers.get(target, 0) | (1 << index)

        survives = False
        for mask in fibers.values():
            maximum_small_fiber = max(maximum_small_fiber, mask.bit_count())
            if mask.bit_count() < 3:
                continue
            remaining = mask
            fiber_survives = False
            while remaining:
                bit = remaining & -remaining
                center = bit.bit_length() - 1
                remaining ^= bit
                score = (
                    2 * (distance_four[center] & mask).bit_count()
                    + (distance_six[center] & mask).bit_count()
                )
                maximum_weighted_degree = max(maximum_weighted_degree, score)
                if score >= 4:
                    fiber_survives = True
                    survives = True
                    break
            surviving_fibers += fiber_survives
        if survives:
            survivors.append(prime)

    return {
        "order": order,
        "input_two_leaf_primes": len(primes),
        "weighted_multistar_primes": survivors,
        "surviving_fiber_count": surviving_fibers,
        "maximum_small_fiber": maximum_small_fiber,
        "maximum_weighted_degree": maximum_weighted_degree,
        "complete": True,
        "elapsed_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    source = json.loads(INPUT.read_text())["results"]
    results: list[dict[str, object]] = []
    for row in source:
        order = int(row["order"])
        primes = [int(prime) for prime in row["aligned_ideal_star_primes"]]
        try:
            result = screen.remote(order, primes)
        except BaseException as error:
            print(f"H3_WEIGHTED_MULTISTAR_PARTIAL order={order} error={error!r}", flush=True)
            continue
        results.append(result)
        OUTPUT.write_text(json.dumps({"results": results}, indent=2, sort_keys=True) + "\n")
        print("H3_WEIGHTED_MULTISTAR_ROW " + json.dumps(result, sort_keys=True), flush=True)
    if not results:
        raise SystemExit("no completed weighted-multistar rows")
    print(f"H3_WEIGHTED_MULTISTAR_DONE completed={len(results)}/2 output={OUTPUT}")
