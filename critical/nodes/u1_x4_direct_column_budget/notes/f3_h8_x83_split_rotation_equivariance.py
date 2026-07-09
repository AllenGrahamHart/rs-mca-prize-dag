#!/usr/bin/env python3
"""Replay x83 split equivariance under h=8 support rotations."""

from __future__ import annotations

from f3_h8_x83_support_certifier_reduction import (
    classify_x83_support,
    paid_lift_supports,
)
from f3_h8_n64_x83_obstruction_interface import root_table


PRIMES = (193, 4289, 262337)
N = 64


def rotate_support(support: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(sorted((exponent + shift) % N for exponent in support))


def rotated_side(side: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(sorted((exponent + shift) % N for exponent in side))


def same_split_up_to_swap(
    got: tuple[tuple[int, ...], tuple[int, ...]],
    expected: tuple[tuple[int, ...], tuple[int, ...]],
) -> bool:
    return got == expected or got == (expected[1], expected[0])


def verify_prime(p: int) -> tuple[int, int]:
    vals = root_table(p, N)
    supports = paid_lift_supports(p)
    checks = 0
    for support in supports:
        plus, minus = classify_x83_support(support, vals, p)
        for shift in range(N):
            rotated = rotate_support(support, shift)
            got = classify_x83_support(rotated, vals, p)
            expected = (rotated_side(plus, shift), rotated_side(minus, shift))
            if not same_split_up_to_swap(got, expected):
                raise AssertionError((p, support, shift, got, expected))
            checks += 1
    return len(supports), checks


def main() -> None:
    total_supports = 0
    total_checks = 0
    for p in PRIMES:
        supports, checks = verify_prime(p)
        total_supports += supports
        total_checks += checks
        print(f"p={p}: paid_supports={supports} rotation_split_checks={checks}")
    if total_supports != 29 or total_checks != 1856:
        raise AssertionError((total_supports, total_checks))
    print("x83 canonical split commutes with rotations up to side swap")
    print("H8_X83_SPLIT_ROTATION_EQUIVARIANCE_PASS")


if __name__ == "__main__":
    main()
