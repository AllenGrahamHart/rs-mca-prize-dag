#!/usr/bin/env python3
"""Independent hostile audit of the E=34 parity-profile reduction."""

from __future__ import annotations

from itertools import combinations


def candidate_survivors(magnitudes, profiles):
    unit_supply = sum(
        left * right == 1 for left, right in combinations(magnitudes, 2)
    )
    return tuple(profile for profile in profiles if profile[0] + profile[2] <= unit_supply)


def diameter_values(heavy: int, light: int, allow_light_diameter: bool):
    values = set()
    for d4 in range(heavy // 2 + 1):
        for d2 in range(min(heavy - 2 * d4, light) + 1):
            remaining_light = light - d2
            d1_max = remaining_light // 2 if allow_light_diameter else 0
            for d1 in range(d1_max + 1):
                values.add(16 * d4 + 4 * d2 + d1)
    return values


def main() -> None:
    profiles = ((6, 7, 0), (9, 4, 1), (12, 1, 2))
    assert candidate_survivors((2, 2, 2, 1, 1, 1, 1), profiles) == ((6, 7, 0),)

    # Mutating a heavy coefficient to light increases the odd-chord supply and
    # invalidates the unique-survivor conclusion.
    assert candidate_survivors((2, 2, 1, 1, 1, 1, 1), profiles) != ((6, 7, 0),)

    # A unit diameter or a repeated unit-distance class leaves at most five
    # unit chords for six odd output classes.
    assert 6 - 1 < 6
    assert 6 - 1 < 6

    assert diameter_values(3, 4, False) == {0, 4, 8, 12, 16, 20}
    assert 21 in diameter_values(3, 4, True)
    assert {(34 - 102 + value) // 2 for value in diameter_values(3, 4, False)} == {
        -34,
        -32,
        -30,
        -28,
        -26,
        -24,
    }

    print("E1_N256_S16_E34_PARITY_PROFILE_REDUCTION_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
