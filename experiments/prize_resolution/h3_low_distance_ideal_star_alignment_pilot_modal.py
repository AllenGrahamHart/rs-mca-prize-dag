#!/usr/bin/env python3
"""Sub-dollar exact prime-ideal alignment pilot for the H3 ideal-star router.

Decision: screen every relevant toy-order principal-norm prime for an actual
low-distance rooted star at one common degree-one prime above p. This is
equivalent to divisibility of some normalized two-generator ideal norm, while
avoiding explicit ideal normal forms and raw star enumeration.

The two Modal functions run sequentially with one physical CPU, 1 GiB RAM,
and a 120-second hard timeout. The requested-resource ceiling is below $0.004
at the 2026-07-18 published rates; the campaign cost cap is $0.10. Completed
orders are written locally before the next order begins.
"""

from __future__ import annotations

import json
from pathlib import Path

import modal


INPUT = Path(__file__).with_name("h3_low_distance_ideal_star_gcd_pilot_result.json")
OUTPUT = Path(__file__).with_name("h3_low_distance_ideal_star_alignment_pilot_result.json")
app = modal.App("rs-mca-h3-low-distance-ideal-star-alignment-pilot")
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
        left, right = pair
        for exponent, coefficient in (
            ((left + right) % order, 1),
            (left, -1),
            (right, -1),
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
    adjacency: list[int] = []
    for left, left_vector in enumerate(small_vectors):
        mask = 0
        for right, right_vector in enumerate(small_vectors):
            if left != right and distance(left_vector, right_vector) <= 6:
                mask |= 1 << right
        adjacency.append(mask)

    def order_root(prime: int) -> int:
        exponent = (prime - 1) // order
        for base in range(2, 10_000):
            root = pow(base, exponent, prime)
            if pow(root, half, prime) == prime - 1:
                return root
        raise AssertionError((prime, "no order root"))

    aligned_primes: list[int] = []
    rich_rows: list[dict[str, int]] = []
    positive_x18_rows: list[dict[str, int]] = []
    violations: list[dict[str, int]] = []
    maximum_small_fiber = 0
    maximum_ordered_fiber = 0
    aligned_fiber_count = 0

    for prime_index, prime in enumerate(primes, start=1):
        if prime_index % 250 == 0:
            print(
                "H3_IDEAL_STAR_ALIGNMENT_PROGRESS "
                f"order={order} primes={prime_index}/{len(primes)} "
                f"aligned={len(aligned_primes)} rich={len(rich_rows)} "
                f"elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )
        root = order_root(prime)
        powers = [pow(root, exponent, prime) for exponent in range(order)]

        fibers: dict[int, int] = {}
        for index, (left, right) in enumerate(small_pairs):
            target = ((1 - powers[left]) * (1 - powers[right])) % prime
            fibers[target] = fibers.get(target, 0) | (1 << index)

        aligned_here = 0
        local_maximum = 0
        for mask in fibers.values():
            size = mask.bit_count()
            local_maximum = max(local_maximum, size)
            if size < 3:
                continue
            remaining = mask
            has_star = False
            while remaining:
                bit = remaining & -remaining
                center = bit.bit_length() - 1
                remaining ^= bit
                if (adjacency[center] & mask).bit_count() >= 2:
                    has_star = True
                    break
            if has_star:
                aligned_here += 1
        maximum_small_fiber = max(maximum_small_fiber, local_maximum)
        if aligned_here:
            aligned_primes.append(prime)
            aligned_fiber_count += aligned_here

        values = [(1 - powers[exponent]) % prime for exponent in range(1, order)]
        product: collections.Counter[int] = collections.Counter()
        quotient: collections.Counter[int] = collections.Counter()
        inverses = {value: pow(value, prime - 2, prime) for value in values}
        for left in values:
            inverse = inverses[left]
            for right in values:
                product[(left * right) % prime] += 1
                quotient[(right * inverse) % prime] += 1
        max_product = max(product.values())
        maximum_ordered_fiber = max(maximum_ordered_fiber, max_product)
        x18 = sum(
            max(count - 18, 0) * quotient.get(target, 0)
            for target, count in product.items() if target != 1
        )
        row = {"prime": prime, "max_P": max_product, "X18": x18}
        if max_product >= 19:
            rich_rows.append(row)
        if x18:
            positive_x18_rows.append(row)
        if 17 * x18 > 300 * order * order:
            violations.append(row)

    return {
        "order": order,
        "input_relevant_primes": len(primes),
        "aligned_ideal_star_primes": aligned_primes,
        "aligned_fiber_count": aligned_fiber_count,
        "maximum_small_fiber": maximum_small_fiber,
        "maximum_ordered_product_fiber": maximum_ordered_fiber,
        "rich_rows": rich_rows,
        "positive_x18_rows": positive_x18_rows,
        "c36_violations": violations,
        "complete": True,
        "elapsed_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    source = json.loads(INPUT.read_text())["results"]
    results: list[dict[str, object]] = []
    for row in source:
        order = int(row["order"])
        primes = [int(prime) for prime in row["single_edge_relevant_primes"]]
        try:
            result = screen.remote(order, primes)
        except BaseException as error:
            print(f"H3_IDEAL_STAR_ALIGNMENT_PARTIAL order={order} error={error!r}", flush=True)
            continue
        results.append(result)
        OUTPUT.write_text(json.dumps({"results": results}, indent=2, sort_keys=True) + "\n")
        print("H3_IDEAL_STAR_ALIGNMENT_ROW " + json.dumps(result, sort_keys=True), flush=True)
    if not results:
        raise SystemExit("no completed alignment rows")
    print(f"H3_IDEAL_STAR_ALIGNMENT_DONE completed={len(results)}/2 output={OUTPUT}")
