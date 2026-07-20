#!/usr/bin/env python3
"""Verify the finite constants and normalized fixtures for PF33."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_uniform_product_fiber_stepanov"
CONSUMER = "f3_h3_mobius_excess_half"
EXPONENT_CONSUMER = "f3_h3_double_accident_derivative_ideal"
LAYER_CONSUMER = "f3_h3_cutoff_layered_gcd_compiler"


def integer_cube_root(value: int) -> int:
    low, high = 0, 1
    while high**3 <= value:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**3 <= value:
            low = middle
        else:
            high = middle
    return low


def scaled_two_thirds_floor(order: int, numerator: int, denominator: int) -> int:
    low, high = 0, integer_cube_root(order * order) + 1
    while low + 1 < high:
        middle = (low + high) // 2
        if (denominator * middle) ** 3 <= numerator**3 * order**2:
            low = middle
        else:
            high = middle
    return low


def scaled_one_third_floor(order: int, numerator: int, denominator: int) -> int:
    low, high = 0, 1
    while (denominator * high) ** 3 <= numerator**3 * order:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if (denominator * middle) ** 3 <= numerator**3 * order:
            low = middle
        else:
            high = middle
    return low


def prime_factors(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def subgroup(prime: int, order: int) -> set[int]:
    factors = prime_factors(prime - 1)
    generator = next(
        value
        for value in range(2, prime)
        if all(pow(value, (prime - 1) // factor, prime) != 1 for factor in factors)
    )
    root = pow(generator, (prime - 1) // order, prime)
    group = {pow(root, exponent, prime) for exponent in range(order)}
    if len(group) != order:
        raise AssertionError("subgroup fixture has the wrong order")
    return group


def check_fixture(prime: int, order: int) -> tuple[int, int]:
    group = subgroup(prime, order)
    shifted = {(1 - value) % prime for value in group if value != 1}
    products = Counter(left * right % prime for left in shifted for right in shifted)
    checked = 0
    max_fiber = 0
    for tau in range(1, prime):
        if tau == 1:
            continue
        normalized = sum(
            1
            for u in group
            for v in group
            if (u * u - u * v - u + (1 - tau) * v) % prime == 0
        )
        if products[tau] != normalized:
            raise AssertionError((prime, order, tau, products[tau], normalized))
        checked += normalized
        max_fiber = max(max_fiber, normalized)
    return checked, max_fiber


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("PF33 node is not PROVED in dag.json")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    if (NODE, CONSUMER, "ev") not in edges:
        raise AssertionError("PF33 evidence edge is missing")
    required_consumers = {
        right for left, right, kind in edges if left == NODE and kind == "req"
    }
    if required_consumers != {EXPONENT_CONSUMER, LAYER_CONSUMER}:
        raise AssertionError(("unexpected PF33 required consumers", required_consumers))
    for consumer in (EXPONENT_CONSUMER, LAYER_CONSUMER):
        if nodes.get(consumer, {}).get("status") != "PROVED":
            raise AssertionError(f"PF33 required consumer {consumer} is not PROVED")


def main() -> None:
    constant_32_failures: list[int] = []
    unadjusted_dimension_failures: list[int] = []
    adjustments = {14: 2, 16: 1, 17: 2}
    dimension_rows: list[tuple[int, int, int, int, int, int, int]] = []

    for exponent in range(13, 42):
        n = 1 << exponent
        a0 = scaled_two_thirds_floor(n, 10, 11)
        b = scaled_one_third_floor(n, 11, 10)
        base_c = scaled_one_third_floor(n, 11, 5)
        c = base_c + adjustments.get(exponent, 0)
        d = scaled_two_thirds_floor(n, 3, 10)

        raw_left = 4 * (a0 * d + 3 * d * d)
        if not raw_left < a0 * b * base_c:
            unadjusted_dimension_failures.append(exponent)
        if not raw_left < a0 * b * c:
            raise AssertionError((exponent, "auxiliary dimension"))
        if not a0 * b < n:
            raise AssertionError((exponent, "strict coprimality"))
        if not (b + c - 1) * n < n * n:
            raise AssertionError((exponent, "degree below every p>=n^2"))

        numerator = 9 * d + 3 * (b + c - 1) * n
        if not numerator**3 < 33**3 * n**2 * d**3:
            raise AssertionError((exponent, "constant 33"))
        if numerator**3 >= 32**3 * n**2 * d**3:
            constant_32_failures.append(exponent)
        if exponent <= 20:
            dimension_rows.append((exponent, a0, b, c, d, raw_left, a0 * b * c))

    expected_rows = [
        (13, 369, 22, 44, 121, 354288, 357192),
        (14, 586, 27, 57, 193, 899380, 901854),
        (15, 930, 35, 70, 307, 2273028, 2278500),
        (16, 1477, 44, 89, 487, 5723224, 5783932),
        (17, 2345, 55, 113, 774, 14449032, 14574175),
        (18, 3723, 70, 140, 1228, 36383184, 36485400),
        (19, 5910, 88, 177, 1950, 91728000, 92054160),
        (20, 9382, 111, 223, 3096, 231209280, 232232646),
    ]
    if dimension_rows != expected_rows:
        raise AssertionError("printed finite parameter table drifted")
    if unadjusted_dimension_failures != [14, 16, 17]:
        raise AssertionError((unadjusted_dimension_failures, "floor-repair mutation"))
    if constant_32_failures != list(range(13, 42)):
        raise AssertionError((constant_32_failures, "constant-32 mutation"))

    fixtures = [check_fixture(97, 32), check_fixture(193, 64)]
    if any(total <= 0 or maximum <= 0 for total, maximum in fixtures):
        raise AssertionError("finite normalization fixture is vacuous")
    check_dag()

    print(
        "F3_H3_UNIFORM_PRODUCT_FIBER_STEPANOV_PASS "
        "official_orders=29 adjusted_rows=3 constant32_mutations=29 "
        f"fixtures={fixtures} dag=2/2"
    )


if __name__ == "__main__":
    main()
