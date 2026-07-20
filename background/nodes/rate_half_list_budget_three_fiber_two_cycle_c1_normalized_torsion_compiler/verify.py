#!/usr/bin/env python3
"""Exact checks for the c=1 normalized torsion compiler."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from random import Random


HERE = Path(__file__).resolve().parent
DEPENDENCY = (
    HERE.parent
    / "rate_half_list_budget_three_fiber_two_cycle_c1_coefficient_resultant_elimination"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("c1_resultant_algebra", DEPENDENCY)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load c1 resultant algebra")
compiler = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(compiler)

algebra = compiler.algebra
PRIME = compiler.PRIME
OFFICIAL_H = (1 << 37) + 1


def outer_invariants(alpha: int, beta: int, gamma: int) -> tuple[int, int]:
    invariant_i = (alpha * alpha + 12 * gamma) % PRIME
    invariant_j = (
        72 * alpha * gamma - 27 * beta * beta - 2 * alpha**3
    ) % PRIME
    return invariant_i, invariant_j


def scale_outer(
    repeated: int,
    alpha: int,
    beta: int,
    gamma: int,
    h_value: int = OFFICIAL_H,
) -> tuple[int, int, int]:
    scale = pow(repeated, -1, PRIME)
    return (
        alpha * pow(scale, 2 * h_value, PRIME) % PRIME,
        beta * pow(scale, 3 * h_value, PRIME) % PRIME,
        gamma * pow(scale, 4 * h_value, PRIME) % PRIME,
    )


def normalized_norm(
    total: int,
    product: int,
    invariant_i: int,
    invariant_j: int,
) -> int:
    return compiler.norm_from_sum_product(
        1, total, product, invariant_i, invariant_j
    )


def torsion_recurrence(
    total: int,
    product: int,
    unused: int,
    *,
    levels: int = 40,
    modulus: int = PRIME,
    product_coefficient: int = 2,
) -> tuple[int, int, int]:
    trace = total % modulus
    product_power = product % modulus
    unused_power = unused % modulus
    for _ in range(levels):
        trace = (
            trace * trace - product_coefficient * product_power
        ) % modulus
        product_power = product_power * product_power % modulus
        unused_power = unused_power * unused_power % modulus
    return trace, product_power, unused_power


def main() -> None:
    rng = Random(20260720)
    scaling_checks = 0

    for _ in range(80):
        repeated, first, second = [
            rng.randrange(1, PRIME) for _ in range(3)
        ]
        alpha, beta, gamma = [rng.randrange(PRIME) for _ in range(3)]
        invariant_i, invariant_j = outer_invariants(alpha, beta, gamma)
        old_norm = algebra.c1_components(
            repeated,
            first,
            second,
            invariant_i,
            invariant_j,
        )[2]

        scale = pow(repeated, -1, PRIME)
        normalized_first = first * scale % PRIME
        normalized_second = second * scale % PRIME
        normalized_alpha, normalized_beta, normalized_gamma = scale_outer(
            repeated, alpha, beta, gamma
        )
        normalized_i, normalized_j = outer_invariants(
            normalized_alpha, normalized_beta, normalized_gamma
        )
        new_norm = normalized_norm(
            (normalized_first + normalized_second) % PRIME,
            normalized_first * normalized_second % PRIME,
            normalized_i,
            normalized_j,
        )
        expected_factor = pow(
            repeated, -(24 * OFFICIAL_H + 12), PRIME
        )
        assert new_norm == old_norm * expected_factor % PRIME
        scaling_checks += 1

    # Exhaust the small analogue N=8 over F_17. This checks both directions
    # of the two-scalar pair recurrence, not only subgroup fixtures.
    pair_checks = 0
    for first in range(1, 17):
        for second in range(1, 17):
            total = (first + second) % 17
            product = first * second % 17
            trace, product_power, _ = torsion_recurrence(
                total, product, 1, levels=3, modulus=17
            )
            recurrence_passes = trace == 2 and product_power == 1
            direct_passes = pow(first, 8, 17) == pow(second, 8, 17) == 1
            assert recurrence_passes == direct_passes
            pair_checks += 1

    unused_checks = 0
    for unused in range(1, 17):
        _, _, unused_power = torsion_recurrence(
            2, 1, unused, levels=3, modulus=17
        )
        assert (unused_power == 1) == (pow(unused, 8, 17) == 1)
        unused_checks += 1

    # Use a direct order-eight subgroup for an official forty-level fixture.
    primitive = next(
        candidate
        for candidate in range(2, PRIME)
        if all(
            pow(candidate, (PRIME - 1) // factor, PRIME) != 1
            for factor in (2, 3, 7)
        )
    )
    subgroup = [
        pow(primitive, (PRIME - 1) // 8 * exponent, PRIME)
        for exponent in range(8)
    ]
    first, second, unused = subgroup[1], subgroup[3], subgroup[5]
    terminal = torsion_recurrence(
        (first + second) % PRIME,
        first * second % PRIME,
        unused,
    )
    assert terminal == (2, 1, 1)

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_NORMALIZED_TORSION_PASS "
        f"scaling={scaling_checks} pair_equivalence={pair_checks} "
        f"unused_equivalence={unused_checks} official_levels=40"
    )


if __name__ == "__main__":
    main()
