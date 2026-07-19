#!/usr/bin/env python3
"""Sub-dollar distance-class census for H3 low collision norms.

Decision: determine whether squared-distance-four obstructions have any odd
prime factor at complete toy orders. If not, attempt a uniform 2-primary
classification; if they do, retain distance four in the candidate generator.

Two sequential Modal functions request one CPU, 1 GiB, and at most 120 seconds
each. The hard requested-resource ceiling is below $0.004 at the 2026-07-18
published rates; the campaign cap is $0.10. Completed orders are checkpointed
locally and remote progress preserves partial counts.
"""

from __future__ import annotations

import json
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name("h3_low_distance_norm_class_pilot_result.json")
app = modal.App("rs-mca-h3-low-distance-norm-class-pilot")
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
    seen: set[tuple[int, int]] = set()
    orbit_counts: collections.Counter[int] = collections.Counter()
    raw_counts: collections.Counter[int] = collections.Counter()
    norms: dict[int, set[int]] = {2: set(), 4: set(), 6: set()}
    examples: dict[tuple[int, int], tuple[int, int]] = {}
    phi = fmpz_poly([1] + [0] * (half - 1) + [1])

    for left_position, left in enumerate(small):
        if left_position and left_position % 128 == 0:
            print(
                "H3_NORM_CLASS_PROGRESS "
                f"order={order} left={left_position}/{len(small)} "
                f"raw={sum(raw_counts.values())} orbits={sum(orbit_counts.values())} "
                f"elapsed={time.monotonic()-started:.3f}",
                flush=True,
            )
        for right in small[left_position + 1:]:
            square = distance(vectors[left], vectors[right])
            if square > 6:
                continue
            raw_counts[square] += 1
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
            normalized = norm // 4
            orbit_counts[square] += 1
            norms[square].add(normalized)
            examples.setdefault((square, normalized), representative)

    rows = {}
    for square in (2, 4, 6):
        odd_primes: set[int] = set()
        relevant_primes: set[int] = set()
        witness = None
        for norm in norms[square]:
            factors = {int(prime) for prime in factorint(norm) if int(prime) % 2}
            odd_primes.update(factors)
            relevant_primes.update(
                prime for prime in factors
                if prime >= order * order and prime % order == 1
            )
            if factors and witness is None:
                witness = {
                    "normalized_norm": norm,
                    "odd_factors": sorted(factors),
                    "representative": list(examples[(square, norm)]),
                }
        rows[str(square)] = {
            "raw_edges": raw_counts[square],
            "galois_exchange_orbits": orbit_counts[square],
            "distinct_normalized_norms": len(norms[square]),
            "odd_prime_factors": len(odd_primes),
            "relevant_prime_factors": len(relevant_primes),
            "first_odd_witness": witness,
        }

    return {
        "order": order,
        "small_vector_pairs": len(small),
        "classes": rows,
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
            print(f"H3_NORM_CLASS_PARTIAL order={order} error={error!r}", flush=True)
            continue
        results.append(result)
        OUTPUT.write_text(json.dumps({"results": results}, indent=2, sort_keys=True) + "\n")
        print("H3_NORM_CLASS_ROW " + json.dumps(result, sort_keys=True), flush=True)
    if not results:
        raise SystemExit("no completed norm-class rows")
    print(f"H3_NORM_CLASS_DONE completed={len(results)}/2 output={OUTPUT}")
