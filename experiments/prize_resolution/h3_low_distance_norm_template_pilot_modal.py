#!/usr/bin/env python3
"""Sub-dollar pilot for H3 low-distance norm-template compression.

Decision: determine whether exact collision norms merge the very large raw
Galois-orbit family into a small number of templates at toy dyadic orders.

* strong compression selects an algebraic template-classification attack;
* weak compression confirms that CR-001 needs a stronger collision selector.

The two sequential Modal functions request one physical CPU and 1 GiB each,
with a 60-second hard timeout. At the 2026-07-18 published function rates,
their requested CPU and memory ceiling is below $0.002; the campaign cost cap
is $0.10 including startup variance. Each completed order is written locally
before the next begins, and remote progress lines preserve partial counts.
"""

from __future__ import annotations

import json
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("h3_low_distance_norm_template_pilot_result.json")
app = modal.App("rs-mca-h3-low-distance-norm-template-pilot")
image = modal.Image.debian_slim().pip_install("python-flint", "sympy")


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=1)
def census(order: int, norm_limit: int | None) -> dict[str, object]:
    import collections
    import itertools
    import time

    from flint import fmpz_poly
    from sympy import factorint

    started = time.monotonic()
    half = order // 2
    multipliers = tuple(range(1, order, 2))
    pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
    pair_index = {pair: index for index, pair in enumerate(pairs)}

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

    def move(pair: tuple[int, int], multiplier: int) -> int:
        moved = tuple(sorted((pair[0] * multiplier % order, pair[1] * multiplier % order)))
        return pair_index[moved]

    vectors = [vector(pair) for pair in pairs]
    seen: set[tuple[int, int]] = set()
    representatives: list[tuple[int, int]] = []
    low_edges = 0
    distance_counts: collections.Counter[int] = collections.Counter()
    for left in range(len(pairs)):
        if left and left % 256 == 0:
            print(
                "H3_TEMPLATE_ORBIT_PROGRESS "
                f"order={order} left={left}/{len(pairs)} low={low_edges} "
                f"orbits={len(representatives)} elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )
        for right in range(left + 1, len(pairs)):
            square = distance(vectors[left], vectors[right])
            if square > 6:
                continue
            low_edges += 1
            distance_counts[square] += 1
            edge = (left, right)
            if edge in seen:
                continue
            orbit = set()
            for multiplier in multipliers:
                moved = tuple(sorted((move(pairs[left], multiplier), move(pairs[right], multiplier))))
                orbit.add(moved)
            seen.update(orbit)
            representatives.append(min(orbit))

    phi = fmpz_poly([1] + [0] * (half - 1) + [1])
    selected = representatives if norm_limit is None else representatives[:norm_limit]
    norms: collections.Counter[int] = collections.Counter()
    relevant_primes: set[int] = set()
    for index, (left, right) in enumerate(selected, start=1):
        coefficients = [0] * half
        for coordinate, value in vectors[left].items():
            coefficients[coordinate] += value
        for coordinate, value in vectors[right].items():
            coefficients[coordinate] -= value
        while coefficients and coefficients[-1] == 0:
            coefficients.pop()
        norm = abs(int(phi.resultant(fmpz_poly(coefficients))))
        if norm == 0:
            raise AssertionError((order, left, right, "zero norm"))
        norms[norm] += 1
        if order == 32:
            for prime in factorint(norm):
                if prime % order == 1 and prime >= order * order:
                    relevant_primes.add(int(prime))
        if index % 1000 == 0:
            print(
                "H3_TEMPLATE_NORM_PROGRESS "
                f"order={order} norms={index}/{len(selected)} "
                f"distinct={len(norms)} elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )

    return {
        "order": order,
        "unordered_root_pairs": len(pairs),
        "raw_low_edges": low_edges,
        "galois_exchange_orbits": len(representatives),
        "distance_histogram": {str(key): value for key, value in sorted(distance_counts.items())},
        "norms_computed": len(selected),
        "distinct_absolute_norms": len(norms),
        "largest_norm_bits": max(norms).bit_length() if norms else 0,
        "largest_template_multiplicity": max(norms.values()) if norms else 0,
        "relevant_primes": sorted(relevant_primes),
        "complete_norm_census": len(selected) == len(representatives),
        "elapsed_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for order, norm_limit in ((32, None), (64, 5000)):
        try:
            result = census.remote(order, norm_limit)
        except BaseException as error:
            print(f"H3_TEMPLATE_PILOT_PARTIAL order={order} error={error!r}", flush=True)
            continue
        results.append(result)
        OUTPUT.write_text(json.dumps({"results": results}, indent=2, sort_keys=True) + "\n")
        print("H3_TEMPLATE_PILOT_ROW " + json.dumps(result, sort_keys=True), flush=True)
    if not results:
        raise SystemExit("no completed pilot rows")
    print(f"H3_TEMPLATE_PILOT_DONE completed={len(results)}/2 output={OUTPUT}")
