#!/usr/bin/env python3
"""Independent finite cyclic-action and arithmetic audit."""

from __future__ import annotations

from itertools import combinations
from fractions import Fraction
from math import comb, gcd


def translate(support: tuple[int, ...], shift: int, n: int) -> tuple[int, ...]:
    return tuple(sorted((value + shift) % n for value in support))


def stabilizer(support: tuple[int, ...], n: int) -> tuple[int, ...]:
    return tuple(shift for shift in range(n) if translate(support, shift, n) == support)


def main() -> None:
    # Exhaustively audit the group-theoretic implication on small cyclic sets:
    # a nontrivial stabilizer partitions a support into subgroup orbits.
    checked = 0
    for n in (8, 12, 16):
        for h in range(2, n // 2 + 1):
            for support in combinations(range(n), h):
                stab = stabilizer(support, n)
                if len(stab) > 1:
                    generator = min(value for value in stab if value)
                    order = n // gcd(n, generator)
                    orbit = {0}
                    value = generator
                    while value:
                        orbit.add(value)
                        value = (value + generator) % n
                    assert len(orbit) == order
                    assert all(
                        {(x + delta) % n for delta in orbit} <= set(support)
                        for x in support
                    )
                checked += 1

    n = 11
    left = (0, 1, 3)
    right = (2, 5, 7)
    ordered_orbit = {
        (translate(left, shift, n), translate(right, shift, n))
        for shift in range(n)
    }
    assert len(ordered_orbit) == n
    assert sum(0 in moved_left for moved_left, _ in ordered_orbit) == len(left)

    n = 2**13
    target_upper = 7000 * n * (1 + Fraction(n * n, 576))
    assert target_upper < comb(n, 4)
    print(
        "AUDIT_F3_HGE4_PRIMITIVE_SHIFT_PAIR_ORBIT_AGGREGATE_ROUTER_PASS "
        f"cyclic_supports={checked}"
    )


if __name__ == "__main__":
    main()
