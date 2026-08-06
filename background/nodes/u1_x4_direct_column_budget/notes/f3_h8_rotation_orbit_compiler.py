#!/usr/bin/env python3
"""Compile the safe rotation-orbit count for h=8 n=64 supports."""

from __future__ import annotations

from collections import Counter
import math


N = 64
SUPPORT_SIZE = 16

EXPECTED = {
    "all_supports": 488526937079580,
    "anchored_supports": 122131734269895,
    "rotation_group_size": 64,
    "all_rotation_orbits": 7633233556276,
    "antipodal_supports": 10518300,
    "antipodal_rotation_orbits": 328756,
    "nonantipodal_rotation_orbits": 7633233227520,
}


def translation_cycles(size: int, shift: int) -> tuple[int, ...]:
    seen = [False] * size
    cycles: list[int] = []
    for start in range(size):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = (current + shift) % size
        cycles.append(length)
    return tuple(sorted(cycles))


def fixed_subsets(cycles: tuple[int, ...], subset_size: int) -> int:
    """Number of subset_size unions of cycles with the given cycle lengths."""
    dp = [0] * (subset_size + 1)
    dp[0] = 1
    for length in cycles:
        for total in range(subset_size, length - 1, -1):
            dp[total] += dp[total - length]
    return dp[subset_size]


def cyclic_orbit_count(size: int, subset_size: int) -> tuple[int, Counter[tuple[int, ...]]]:
    cycle_types = Counter(translation_cycles(size, shift) for shift in range(size))
    fixed_sum = sum(
        multiplicity * fixed_subsets(cycles, subset_size)
        for cycles, multiplicity in cycle_types.items()
    )
    if fixed_sum % size:
        raise AssertionError((size, subset_size, fixed_sum))
    return fixed_sum // size, cycle_types


def main() -> None:
    all_supports = math.comb(N, SUPPORT_SIZE)
    anchored_supports = math.comb(N - 1, SUPPORT_SIZE - 1)

    all_rotation_orbits, support_cycle_types = cyclic_orbit_count(N, SUPPORT_SIZE)

    # Antipodal 16-supports are exactly 8-subsets of the 32 antipodal pairs.
    pair_count = N // 2
    antipodal_supports = math.comb(pair_count, SUPPORT_SIZE // 2)
    antipodal_rotation_orbits, pair_cycle_types = cyclic_orbit_count(
        pair_count, SUPPORT_SIZE // 2
    )
    nonantipodal_rotation_orbits = all_rotation_orbits - antipodal_rotation_orbits

    actual = {
        "all_supports": all_supports,
        "anchored_supports": anchored_supports,
        "rotation_group_size": N,
        "all_rotation_orbits": all_rotation_orbits,
        "antipodal_supports": antipodal_supports,
        "antipodal_rotation_orbits": antipodal_rotation_orbits,
        "nonantipodal_rotation_orbits": nonantipodal_rotation_orbits,
    }
    if actual != EXPECTED:
        raise AssertionError((actual, EXPECTED))
    if len(support_cycle_types) != 7 or len(pair_cycle_types) != 6:
        raise AssertionError((support_cycle_types, pair_cycle_types))

    anchored_nonantipodal = math.comb(N - 1, SUPPORT_SIZE - 1) - math.comb(
        N // 2 - 1, SUPPORT_SIZE // 2 - 1
    )
    anchored_to_orbit_factor = anchored_nonantipodal / nonantipodal_rotation_orbits

    print("h=8 n=64 rotation-orbit compiler")
    print(f"all 16-supports: {all_supports}")
    print(f"anchored 16-supports with 0: {anchored_supports}")
    print(f"rotation group size: {N}")
    print(f"all 16-support rotation orbits: {all_rotation_orbits}")
    print(f"antipodal 16-supports: {antipodal_supports}")
    print(f"antipodal rotation orbits: {antipodal_rotation_orbits}")
    print(f"non-antipodal rotation orbits: {nonantipodal_rotation_orbits}")
    print(
        "anchored non-antipodal supports per rotation orbit, average: "
        f"{anchored_to_orbit_factor:.6f}"
    )
    print("H8_ROTATION_ORBIT_COMPILER_PASS")


if __name__ == "__main__":
    main()
