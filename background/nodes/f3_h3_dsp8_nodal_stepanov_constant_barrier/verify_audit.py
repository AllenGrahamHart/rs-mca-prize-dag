#!/usr/bin/env python3
"""Independent rational audit of the nodal Stepanov barrier."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def inverse(value: int, prime: int) -> int:
    return pow(value, prime - 2, prime)


def nodal_weight_shortcut_falsifier() -> None:
    prime, order, generator = 7937, 64, 151
    theta, phi, target = 3603, 7083, 2596
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    assert len(group) == order
    assert pow(generator, order // 2, prime) != 1

    def triple(value: int) -> tuple[int, int, int]:
        return (
            -inverse(value * (value + 1) % prime, prime) % prime,
            -value * value * inverse(value + 1, prime) % prime,
            (value + 1) ** 2 * inverse(value, prime) % prime,
        )

    def q(value: int) -> int:
        return value * (value + 1) % prime

    left, right = triple(theta), triple(phi)
    assert left == (4337, 2593, 1010)
    assert right == (3604, 2595, 1741)
    assert set(left) <= group and set(right) <= group
    assert not (set(left) & set(right))
    assert not (set(left) & {-value % prime for value in right})

    actual_target = (
        1
        - (q(theta) + q(phi) + 3 * q(theta) * q(phi))
        * inverse(q(theta) ** 2 * q(phi) ** 2 % prime, prime)
    ) % prime
    assert actual_target == target
    assert (1 - 853**2) % prime == target
    product_richness = sum(
        (1 - x) * (1 - y) % prime == target for x in group for y in group
    )
    quotient_weight = sum(
        z != 1 and (1 - target * (1 - z)) % prime in group for z in group
    )
    assert (product_richness, quotient_weight) == (10, 7)


def main() -> None:
    checked = 0
    for m in (8, 27, 64, 125, 216, 343):
        for b in range(1, m + 1):
            for a in range(1, m // b + 1):
                target = a * b * b
                d = max(0, (isqrt(a * a + 4 * target) - a) // 2)
                while d * (a + d) >= target:
                    d -= 1
                if d:
                    left = Fraction((a + 2 * m * b) ** 3, d**3 * m**2)
                    assert left > 32
                    checked += 1
    # Mutation: the current printed constant is above, not below, the floor.
    assert Fraction(51**3, 16**3) > 32
    assert not Fraction(51**3, 16**3) <= 32
    nodal_weight_shortcut_falsifier()
    print(
        "AUDIT_F3_H3_DSP8_NODAL_STEPANOV_CONSTANT_BARRIER_PASS "
        f"rational_tuples={checked} antipodal_control=P10R7"
    )


if __name__ == "__main__":
    main()
