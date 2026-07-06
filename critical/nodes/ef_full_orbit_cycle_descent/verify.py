#!/usr/bin/env python3
"""Toy check for Galois-orbit cycle descent as stable finite-set descent."""

from __future__ import annotations


def orbit(n: int, start: int) -> set[int]:
    # Cyclic Galois action on component labels.
    return {(start + g) % n for g in range(n)}


def translate(n: int, subset: set[int], g: int) -> set[int]:
    return {(x + g) % n for x in subset}


def main() -> None:
    n = 6
    component = {1}
    pole_divisor_labels = {20, 21}  # disjoint label universe for this toy.
    full_orbit = orbit(n, next(iter(component)))

    for g in range(n):
        assert translate(n, full_orbit, g) == full_orbit
        assert translate(n, component, g).isdisjoint(pole_divisor_labels)

    assert full_orbit.isdisjoint(pole_divisor_labels)
    assert len(full_orbit) == n

    print(
        "ef full-orbit cycle descent check passed:",
        {"orbit_size": len(full_orbit), "stable": True},
    )


if __name__ == "__main__":
    main()
