#!/usr/bin/env python3
"""Verify the pure harmonic-Fermat router and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_pure_harmonic_fermat_router"
DEPENDENCY = "rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def primitive_root(prime: int) -> int:
    factors: list[int] = []
    remainder = prime - 1
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            factors.append(divisor)
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors.append(remainder)
    return next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [
        ((left[index] if index < len(left) else 0)
         + (right[index] if index < len(right) else 0))
        % PRIME
        for index in range(size)
    ]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value % PRIME for value in poly]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def power(poly: list[int], exponent: int) -> list[int]:
    answer = [1]
    for _ in range(exponent):
        answer = multiply(answer, poly)
    return answer


def cross_ratio(a: int, b: int, c: int, d: int) -> int:
    numerator = (a - c) * (b - d) % PRIME
    denominator = (a - d) * (b - c) % PRIME
    return numerator * pow(denominator, -1, PRIME) % PRIME


def harmonic_check() -> None:
    generator = primitive_root(PRIME)
    fourth = pow(generator, (PRIME - 1) // 4, PRIME)
    outer = (1, PRIME - 1, fourth, (-fourth) % PRIME)
    assert cross_ratio(*outer) == PRIME - 1

    order = 16
    zeta = pow(generator, (PRIME - 1) // order, PRIME)
    subgroup = {pow(zeta, exponent, PRIME) for exponent in range(order)}
    witness = None
    for x in subgroup:
        for y in subgroup:
            denominator = (1 + x - 2 * y) % PRIME
            if denominator == 0:
                continue
            z = (2 * x - y * (1 + x)) * pow(denominator, -1, PRIME) % PRIME
            values = (1, x, y, z)
            if z not in subgroup or len(set(values)) != 4:
                continue
            if len({value * value % PRIME for value in values}) != 4:
                continue
            witness = values
            break
        if witness is not None:
            break
    assert witness is not None
    assert cross_ratio(*witness) == PRIME - 1
    assert all(pow(value, order, PRIME) == 1 for value in witness)


def fermat_check() -> None:
    generator = primitive_root(PRIME)
    eighth = pow(generator, (PRIME - 1) // 8, PRIME)
    roots_minus_one = tuple(pow(eighth, exponent, PRIME) for exponent in (1, 3, 5, 7))
    assert all(pow(value, 4, PRIME) == PRIME - 1 for value in roots_minus_one)

    b_poly = [1, 2, 3, 5]
    z_poly = [0, 1, 4, 2]
    product_factors = [1]
    for root in roots_minus_one:
        product_factors = multiply(product_factors, add(b_poly, scale(z_poly, root)))
    assert product_factors == add(power(b_poly, 4), power(z_poly, 4))
    assert b_poly[0] == 1
    assert z_poly[0] == 0 and z_poly[1] != 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "cr(a_0,a_1;a_2,a_3)",
        "w=(2x-y(1+x))/(1+x-2y)",
        "Q=B^4+Z^4",
        "reconstruct the pure-quartic",
        "not an emptiness theorem",
    ):
        assert marker in statement


def main() -> None:
    harmonic_check()
    fermat_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_PURE_HARMONIC_FERMAT_PASS "
        "harmonic_order16_witness=1 fermat_factorization=1"
    )


if __name__ == "__main__":
    main()
