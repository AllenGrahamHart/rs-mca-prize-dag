#!/usr/bin/env python3
"""Independent generating-function audit of the unsigned orbit count."""

from __future__ import annotations

from collections import defaultdict


ORDER = 256
WEIGHT = 6
EXPECTED_FIXED = (197_438_898_176, 184_310_267_904)
EXPECTED_ORBITS = (6_025_357, 5_624_703)


def cycle_inventory(multiplier: int, shift: int) -> list[tuple[int, int]]:
    permutation = [(multiplier * point + shift) % ORDER for point in range(ORDER)]
    unvisited = set(range(ORDER))
    inventory = []
    while unvisited:
        start = min(unvisited)
        point = start
        length = 0
        parity = 0
        while True:
            if point not in unvisited:
                if point != start:
                    raise AssertionError("permutation cycle")
                break
            unvisited.remove(point)
            length += 1
            parity ^= point & 1
            point = permutation[point]
        inventory.append((length, parity))
    return inventory


def fixed_six(inventory: list[tuple[int, int]]) -> tuple[int, int]:
    polynomial = {(0, 0): 1}
    for length, parity in inventory:
        if length > WEIGHT:
            continue
        updated = defaultdict(int, polynomial)
        for (degree, old_parity), coefficient in polynomial.items():
            if degree + length <= WEIGHT:
                updated[(degree + length, old_parity ^ parity)] += coefficient
        polynomial = dict(updated)
    return polynomial.get((WEIGHT, 0), 0), polynomial.get((WEIGHT, 1), 0)


def main() -> None:
    totals = [0, 0]
    maps = 0
    for multiplier in range(1, ORDER, 2):
        for shift in range(ORDER):
            even, odd = fixed_six(cycle_inventory(multiplier, shift))
            totals[0] += even
            totals[1] += odd
            maps += 1
    if tuple(totals) != EXPECTED_FIXED or maps != 32_768:
        raise AssertionError((totals, maps))
    orbits = tuple(total // maps for total in totals)
    if orbits != EXPECTED_ORBITS or any(total % maps for total in totals):
        raise AssertionError(orbits)
    print(
        "DLI_WCL_ELL1_WEIGHT6_UNSIGNED_ROUTER_AUDIT_PASS "
        f"maps={maps} fixed={tuple(totals)} orbits={orbits}"
    )


if __name__ == "__main__":
    main()
