#!/usr/bin/env python3
"""Independent finite-field cross-ratio audit for the mismatch router."""

from __future__ import annotations

from itertools import permutations


PRIME = 101


def cross_ratio(points: tuple[int, int, int, int]) -> int:
    a, b, c, d = points
    numerator = (a - c) * (b - d)
    denominator = (a - d) * (b - c)
    return numerator * pow(denominator % PRIME, -1, PRIME) % PRIME


def invariants_from_roots(roots: tuple[int, int, int, int]) -> tuple[int, int]:
    r0, r1, r2, r3 = roots
    e1 = sum(roots) % PRIME
    e2 = sum(roots[i] * roots[j] for i in range(4) for j in range(i + 1, 4)) % PRIME
    e3 = sum(
        roots[i] * roots[j] * roots[k]
        for i in range(4)
        for j in range(i + 1, 4)
        for k in range(j + 1, 4)
    ) % PRIME
    e4 = r0 * r1 * r2 * r3 % PRIME
    a, b, c, d, e = 1, -e1, e2, -e3, e4
    invariant_i = (12 * a * e - 3 * b * d + c * c) % PRIME
    invariant_j = (
        72 * a * c * e
        + 9 * b * c * d
        - 27 * a * d * d
        - 27 * b * b * e
        - 2 * c * c * c
    ) % PRIME
    return invariant_i, invariant_j


def same_modulus(left: tuple[int, int], right: tuple[int, int]) -> bool:
    left_i, left_j = left
    right_i, right_j = right
    return (left_i**3 * right_j**2 - right_i**3 * left_j**2) % PRIME == 0


def mobius(value: int) -> int:
    return (7 * value + 3) * pow((11 * value + 13) % PRIME, -1, PRIME) % PRIME


def main() -> None:
    source = (1, -1 % PRIME, 2, 3)
    target = tuple(mobius(value) for value in source)
    assert same_modulus(invariants_from_roots(source), invariants_from_roots(target))

    source_ratios = {cross_ratio(ordering) for ordering in permutations(source)}
    target_ratios = {cross_ratio(ordering) for ordering in permutations(target)}
    assert len(source_ratios) == len(target_ratios) == 6
    assert source_ratios == target_ratios

    mutation = (target[0], target[1], target[2], (target[3] + 1) % PRIME)
    assert not same_modulus(invariants_from_roots(source), invariants_from_roots(mutation))
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MISMATCH_INVARIANT_COUPLING_AUDIT_PASS "
        "field=101 anharmonic_orbit=6 mutations=1"
    )


if __name__ == "__main__":
    main()
