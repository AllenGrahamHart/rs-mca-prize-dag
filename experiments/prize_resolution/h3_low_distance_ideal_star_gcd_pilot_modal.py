#!/usr/bin/env python3
"""Sub-dollar pilot for the H3 low-distance ideal-star selector.

Decision: at toy dyadic orders, measure the complete relevant-prime superset
obtained by requiring one center to have two incident normalized collision
norms divisible by the same prime. Every ideal-star prime passes this gcd
screen, although the converse need not hold.

* strong prime compression selects exact two-generator ideal norms next;
* weak compression selects symbolic ideal-star classification instead.

The two Modal functions run sequentially with one physical CPU, 1 GiB RAM,
and a 120-second hard timeout. At the 2026-07-18 published function rates, the
requested-resource ceiling is below $0.004; the campaign cost cap is $0.10.
The completed n=32 result is written before n=64 starts, and progress lines
preserve partial n=64 counts if its hard timeout fires.
"""

from __future__ import annotations

import json
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("h3_low_distance_ideal_star_gcd_pilot_result.json")
app = modal.App("rs-mca-h3-low-distance-ideal-star-gcd-pilot")
image = modal.Image.debian_slim().pip_install("python-flint", "sympy")


@app.function(image=image, cpu=1, memory=1024, timeout=120, max_containers=1)
def census(order: int) -> dict[str, object]:
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

    def square_norm(value: dict[int, int]) -> int:
        return sum(coefficient * coefficient for coefficient in value.values())

    def distance(left: dict[int, int], right: dict[int, int]) -> int:
        return sum(
            (left.get(key, 0) - right.get(key, 0)) ** 2
            for key in left.keys() | right.keys()
        )

    def move(index: int, multiplier: int) -> int:
        pair = pairs[index]
        moved = tuple(sorted((pair[0] * multiplier % order,
                              pair[1] * multiplier % order)))
        return pair_index[moved]

    vectors = [vector(pair) for pair in pairs]
    small = tuple(index for index, value in enumerate(vectors) if square_norm(value) <= 3)
    small_set = set(small)

    unseen_centers = set(small)
    center_orbits: dict[int, set[int]] = {}
    while unseen_centers:
        center = min(unseen_centers)
        orbit = {move(center, multiplier) for multiplier in multipliers}
        if not orbit <= small_set:
            raise AssertionError("small-vector orbit escaped")
        representative = min(orbit)
        center_orbits[representative] = orbit
        unseen_centers.difference_update(orbit)

    center_representatives = set(center_orbits)
    incident: dict[int, dict[tuple[int, int], int]] = {
        center: {} for center in center_representatives
    }
    seen: set[tuple[int, int]] = set()
    norm_counter: collections.Counter[int] = collections.Counter()
    raw_low_edges = 0
    orbit_count = 0
    phi = fmpz_poly([1] + [0] * (half - 1) + [1])

    for left_position, left in enumerate(small):
        if left_position and left_position % 128 == 0:
            print(
                "H3_IDEAL_STAR_EDGE_PROGRESS "
                f"order={order} centers={left_position}/{len(small)} "
                f"edges={raw_low_edges} orbits={orbit_count} "
                f"elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )
        for right in small[left_position + 1:]:
            if distance(vectors[left], vectors[right]) > 6:
                continue
            raw_low_edges += 1
            edge = (left, right)
            if edge in seen:
                continue

            orbit = {
                tuple(sorted((move(left, multiplier), move(right, multiplier))))
                for multiplier in multipliers
            }
            seen.update(orbit)
            representative = min(orbit)
            first, second = representative
            coefficients = [0] * half
            for coordinate, value in vectors[first].items():
                coefficients[coordinate] += value
            for coordinate, value in vectors[second].items():
                coefficients[coordinate] -= value
            while coefficients and coefficients[-1] == 0:
                coefficients.pop()
            norm = abs(int(phi.resultant(fmpz_poly(coefficients))))
            if norm == 0 or norm % 4:
                raise AssertionError((order, representative, norm))
            normalized_norm = norm // 4
            norm_counter[normalized_norm] += 1
            orbit_count += 1

            for moved_edge in orbit:
                for center in moved_edge:
                    if center in center_representatives:
                        incident[center][moved_edge] = normalized_norm

    if len(seen) != raw_low_edges:
        raise AssertionError((len(seen), raw_low_edges))

    factor_cache: dict[int, tuple[int, ...]] = {}
    all_relevant: set[int] = set()
    for index, norm in enumerate(norm_counter, start=1):
        factors = tuple(
            int(prime) for prime in factorint(norm)
            if int(prime) >= order * order and int(prime) % order == 1
        )
        factor_cache[norm] = factors
        all_relevant.update(factors)
        if index % 1000 == 0:
            print(
                "H3_IDEAL_STAR_FACTOR_PROGRESS "
                f"order={order} norms={index}/{len(norm_counter)} "
                f"relevant={len(all_relevant)} elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )

    repeated_relevant: set[int] = set()
    center_prime_rows = 0
    maximum_prime_incidence = 0
    raw_rooted_stars = 0
    for center, orbit in center_orbits.items():
        edge_norms = incident[center].values()
        degree = len(incident[center])
        raw_rooted_stars += len(orbit) * degree * (degree - 1) // 2
        counts: collections.Counter[int] = collections.Counter()
        for norm in edge_norms:
            counts.update(factor_cache[norm])
        for prime, count in counts.items():
            maximum_prime_incidence = max(maximum_prime_incidence, count)
            if count >= 2:
                repeated_relevant.add(prime)
                center_prime_rows += 1

    return {
        "order": order,
        "unordered_root_pairs": len(pairs),
        "small_vector_pairs": len(small),
        "galois_center_orbits": len(center_orbits),
        "raw_low_edges": raw_low_edges,
        "galois_exchange_edge_orbits": orbit_count,
        "raw_rooted_stars": raw_rooted_stars,
        "distinct_normalized_principal_norms": len(norm_counter),
        "single_edge_relevant_primes": sorted(all_relevant),
        "two_incident_edge_relevant_primes": sorted(repeated_relevant),
        "center_prime_rows": center_prime_rows,
        "maximum_prime_incidence": maximum_prime_incidence,
        "complete": True,
        "elapsed_seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    results: list[dict[str, object]] = []
    for order in (32, 64):
        try:
            result = census.remote(order)
        except BaseException as error:
            print(f"H3_IDEAL_STAR_PILOT_PARTIAL order={order} error={error!r}", flush=True)
            continue
        results.append(result)
        OUTPUT.write_text(json.dumps({"results": results}, indent=2, sort_keys=True) + "\n")
        print("H3_IDEAL_STAR_PILOT_ROW " + json.dumps(result, sort_keys=True), flush=True)
    if not results:
        raise SystemExit("no completed pilot rows")
    print(f"H3_IDEAL_STAR_PILOT_DONE completed={len(results)}/2 output={OUTPUT}")
