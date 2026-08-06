#!/usr/bin/env python3
"""Count affine/Galois orbits of 3-subset cores in Z/96Z."""

from __future__ import annotations

import itertools
import math


N = 96


def canonical_core(triple: tuple[int, int, int]) -> tuple[int, int, int]:
    units = [u for u in range(N) if math.gcd(u, N) == 1]
    best = None
    for u in units:
        mapped = [(u * t) % N for t in triple]
        for shift in mapped:
            candidate = tuple(sorted((t - shift) % N for t in mapped))
            if best is None or candidate < best:
                best = candidate
    assert best is not None
    return best


def main() -> None:
    orbits: dict[tuple[int, int, int], int] = {}
    for triple in itertools.combinations(range(N), 3):
        c = canonical_core(triple)
        orbits[c] = orbits.get(c, 0) + 1
    if len(orbits) != 91:
        raise AssertionError(len(orbits))
    if sum(orbits.values()) != math.comb(N, 3):
        raise AssertionError(sum(orbits.values()))

    print(f"core_orbits={len(orbits)} total_triples={sum(orbits.values())}")
    print("representatives:")
    for rep, size in sorted(orbits.items()):
        print(f"  {rep}: {size}")
    print("H3_CORE_ORBIT_COUNT_PASS")


if __name__ == "__main__":
    main()
