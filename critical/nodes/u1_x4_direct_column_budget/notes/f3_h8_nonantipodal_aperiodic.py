#!/usr/bin/env python3
"""Exact combinatorial check for h=8 non-antipodal support aperiodicity."""

from __future__ import annotations

import math


N = 64
SUPPORT_SIZE = 16

EXPECTED = {
    "anchored_nonantipodal_supports": 122131731640320,
    "nonantipodal_rotation_orbits": 7633233227520,
    "anchored_per_nonantipodal_orbit": 16,
}


def subgroup_order(shift: int) -> int:
    return N // math.gcd(N, shift)


def verify_stabilizer_lemma() -> None:
    for shift in range(1, N):
        order = subgroup_order(shift)
        if SUPPORT_SIZE % order:
            continue
        if (N // 2) % math.gcd(N, shift):
            raise AssertionError(("half-turn not generated", shift, order))
        if order not in {2, 4, 8, 16}:
            raise AssertionError(("unexpected stabilizer order", shift, order))


def verify_counts() -> None:
    anchored = math.comb(N - 1, SUPPORT_SIZE - 1)
    anchored_antipodal = math.comb(N // 2 - 1, SUPPORT_SIZE // 2 - 1)
    anchored_nonantipodal = anchored - anchored_antipodal

    all_rotation_orbits = 7633233556276
    antipodal_rotation_orbits = 328756
    nonantipodal_rotation_orbits = all_rotation_orbits - antipodal_rotation_orbits

    actual = {
        "anchored_nonantipodal_supports": anchored_nonantipodal,
        "nonantipodal_rotation_orbits": nonantipodal_rotation_orbits,
        "anchored_per_nonantipodal_orbit": anchored_nonantipodal
        // nonantipodal_rotation_orbits,
    }
    if actual != EXPECTED:
        raise AssertionError((actual, EXPECTED))
    if anchored_nonantipodal % nonantipodal_rotation_orbits:
        raise AssertionError("nonintegral anchored/orbit ratio")


def main() -> None:
    verify_stabilizer_lemma()
    verify_counts()
    print("non-antipodal 16-supports in Z/64Z have trivial rotation stabilizer")
    print(
        "anchored_nonantipodal = "
        f"{EXPECTED['anchored_nonantipodal_supports']}"
    )
    print(
        "nonantipodal_rotation_orbits = "
        f"{EXPECTED['nonantipodal_rotation_orbits']}"
    )
    print("anchored supports per non-antipodal orbit = 16 exactly")
    print("H8_NONANTIPODAL_APERIODIC_PASS")


if __name__ == "__main__":
    main()
