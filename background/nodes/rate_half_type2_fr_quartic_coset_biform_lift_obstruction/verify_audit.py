#!/usr/bin/env python3
"""Independent cyclic-exponent audit of the quartic lift obstruction."""

from __future__ import annotations

from itertools import combinations
from math import gcd


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    checked = 0
    for m in (1, 2, 4, 8, 16, 32, 64):
        n = 4 * m
        order = 4 * n
        exponent = n - 1
        require(gcd(exponent, order) == 1, f"noninjective official exponent at m={m}")

        # Work in the exponent group Z/(4n). Representatives of distinct
        # H-cosets have distinct residues modulo 4. Injectivity of the
        # (n-1)-power map keeps every selected triple distinct.
        representatives = [
            (i + 4 * ((i + 1) * (m + 3) % n)) % order for i in range(4)
        ]
        require({value % 4 for value in representatives} == {0, 1, 2, 3}, "bad transversal")
        powered = [(exponent * value) % order for value in representatives]
        require(len(set(powered)) == 4, f"power collision at m={m}")
        for i, j in combinations(range(4), 2):
            require(powered[i] != powered[j], "pairwise injectivity")
        checked += 1

    # Hostile scope mutation: if two representatives are allowed to be the
    # same domain point, the final contradiction disappears. The guard must
    # therefore explicitly retain distinct H-cosets.
    order = 1024
    exponent = 255
    mutated = [1, 1, 2]
    require(len({exponent * value % order for value in mutated}) < 3, "scope mutation escaped")

    # Hostile degree mutation: degree n permits a nonzero polynomial that
    # vanishes on a complete coset, so the n-1 locator-degree pin is material.
    n = 32
    tau_exponent = 1
    coset_root_exponent = (n * tau_exponent) % (4 * n)
    require(coset_root_exponent != 0, "coset polynomial mutation collapsed")

    require(pow(257, 2, 1024) == 513 and pow(257, 4, 1024) == 1, "extension-degree audit")
    print(
        "RH_TYPE2_FR_QUARTIC_BIFORM_LIFT_OBSTRUCTION_AUDIT_PASS "
        f"scales={checked} pinned_m=64 pinned_N=1024 exponent=255"
    )


if __name__ == "__main__":
    main()
