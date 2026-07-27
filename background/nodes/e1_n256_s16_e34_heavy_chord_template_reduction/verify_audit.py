#!/usr/bin/env python3
"""Independent audit of the E34 heavy-chord templates."""

from __future__ import annotations

from itertools import product


def main() -> None:
    # One heavy-heavy chord and zero/one light-light chord misses the target
    # alphabet. Allowing two light chords is a hostile mutation and admits 2.
    one_light = {abs(4 * sign + unit) for sign in (-1, 1) for unit in (-1, 0, 1)}
    assert one_light.isdisjoint({0, 1, 2})
    two_light = {
        abs(4 * sign + first + second)
        for sign, first, second in product((-1, 1), repeat=3)
    }
    assert 2 in two_light

    with_quarter = {
        abs(4 * middle * (left + right) + 2 * light * (right - left))
        for left, middle, right, light in product((-1, 1), repeat=4)
    }
    assert min(with_quarter) == 4

    no_quarter = {
        (left, right, abs(4 * middle * (left + right) + unit))
        for left, middle, right in product((-1, 1), repeat=3)
        for unit in (-1, 0, 1)
    }
    assert {value for _, _, value in no_quarter if value <= 2} == {0, 1}
    assert all(right == -left for left, right, value in no_quarter if value <= 2)

    # Z/128Z has no nonzero element of order three, so three distinct points
    # cannot have all three unoriented distances equal.
    assert all((3 * value) % 128 != 0 for value in range(1, 128))

    print("E1_N256_S16_E34_HEAVY_CHORD_TEMPLATE_REDUCTION_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
