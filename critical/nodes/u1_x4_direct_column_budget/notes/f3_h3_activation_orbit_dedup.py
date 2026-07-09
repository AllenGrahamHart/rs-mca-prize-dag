#!/usr/bin/env python3
"""Deduplicate the n=96 h=3 activation exceptions into affine/Galois orbits."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
SUMMARY_PATH = HERE / "f3_h3_all_core_census_summary.json"
N = 96
UNITS = tuple(u for u in range(N) if math.gcd(u, N) == 1)


def canonical_pair(flat: list[int]) -> tuple[int, ...]:
    if len(flat) != 6:
        raise AssertionError(flat)
    left = tuple(sorted(flat[:3]))
    right = tuple(sorted(flat[3:]))
    if set(left) & set(right):
        raise AssertionError(flat)

    best: tuple[int, ...] | None = None
    for unit in UNITS:
        for shift in range(N):
            left_image = tuple(sorted((unit * x + shift) % N for x in left))
            right_image = tuple(sorted((unit * x + shift) % N for x in right))
            if set(left_image) & set(right_image):
                raise AssertionError((flat, unit, shift, left_image, right_image))
            for a, b in ((left_image, right_image), (right_image, left_image)):
                candidate = a + b
                if best is None or candidate < best:
                    best = candidate
    if best is None:
        raise AssertionError(flat)
    return best


def activation_orbit_dedup_summary() -> dict[str, int]:
    data = json.loads(SUMMARY_PATH.read_text())
    if data["n"] != N:
        raise AssertionError(data["n"])
    activations = data["activation_exceptions"]
    if len(activations) != 720:
        raise AssertionError(len(activations))

    by_prime: dict[int, set[tuple[int, ...]]] = defaultdict(set)
    all_orbits: set[tuple[int, ...]] = set()
    raw_prime_incidences = 0
    for record in activations:
        orbit = canonical_pair(record["shape"])
        all_orbits.add(orbit)
        primes = record["activation_primes"]
        if len(primes) != 1:
            raise AssertionError(record)
        for prime in primes:
            by_prime[int(prime)].add(orbit)
            raw_prime_incidences += 1

    orbit_primes: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for prime, orbits in by_prime.items():
        for orbit in orbits:
            orbit_primes[orbit].add(prime)
    repeated = {orbit: primes for orbit, primes in orbit_primes.items() if len(primes) > 1}
    if repeated:
        raise AssertionError({orbit: sorted(primes) for orbit, primes in repeated.items()})

    top = sorted(
        ((prime, len(orbits)) for prime, orbits in by_prime.items()),
        key=lambda item: (-item[1], item[0]),
    )
    max_prime, max_orbits = top[0]
    summary = {
        "raw_oriented_activations": len(activations),
        "raw_prime_incidences": raw_prime_incidences,
        "unique_orbits": len(all_orbits),
        "activation_primes": len(by_prime),
        "max_prime": max_prime,
        "max_deduped_per_prime": max_orbits,
        "repeated_orbits": len(repeated),
    }
    if (
        summary["unique_orbits"],
        summary["activation_primes"],
        summary["raw_prime_incidences"],
        summary["max_prime"],
        summary["max_deduped_per_prime"],
    ) != (
        167,
        82,
        720,
        37633,
        27,
    ):
        raise AssertionError(
            (
                summary["unique_orbits"],
                summary["activation_primes"],
                summary["raw_prime_incidences"],
                summary["max_prime"],
                summary["max_deduped_per_prime"],
            )
        )
    if summary["repeated_orbits"] != 0:
        raise AssertionError(summary)
    return summary


def main() -> None:
    summary = activation_orbit_dedup_summary()

    print("h=3 n=96 activation orbit dedup")
    print(f"raw oriented activation records: {summary['raw_oriented_activations']}")
    print(f"raw prime incidences: {summary['raw_prime_incidences']}")
    print(f"unique affine/Galois pair-orbits: {summary['unique_orbits']}")
    print(f"activation primes: {summary['activation_primes']}")
    print(
        "max deduped per-prime activation: "
        f"p={summary['max_prime']} count={summary['max_deduped_per_prime']}"
    )
    print(f"repeated canonical orbits across primes: {summary['repeated_orbits']}")
    print("H3_ACTIVATION_ORBIT_DEDUP_PASS")


if __name__ == "__main__":
    main()
