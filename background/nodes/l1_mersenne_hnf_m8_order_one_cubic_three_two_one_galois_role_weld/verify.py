#!/usr/bin/env python3
"""Check the twelve Galois packets in the ordered role polynomial."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_galois_role_weld"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_role_weld",
}
CONSUMER = "l1_mixed_petal_amplification"
UNITS = (1, 3, 5, 7)


def add(left: tuple[F, ...], right: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(a + b for a, b in zip(left, right))


def scale(value: tuple[F, ...], scalar: F) -> tuple[F, ...]:
    return tuple(scalar * item for item in value)


def mul(left: tuple[F, ...], right: tuple[F, ...]) -> tuple[F, ...]:
    raw = [F(0)] * 7
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            raw[i + j] += a * b
    for degree in range(6, 3, -1):
        raw[degree - 4] -= raw[degree]
    return tuple(raw[:4])


ONE = (F(1), F(0), F(0), F(0))
ZERO = (F(0), F(0), F(0), F(0))
ZETA = (F(0), F(1), F(0), F(0))


def power(value: tuple[F, ...], exponent: int) -> tuple[F, ...]:
    out = ONE
    for _ in range(exponent):
        out = mul(out, value)
    return out


def homogeneous_eval(
    coefficients: tuple[int, ...], numerator: tuple[F, ...], denominator: tuple[F, ...]
) -> tuple[F, ...]:
    degree = len(coefficients) - 1
    out = ZERO
    for exponent, coefficient in enumerate(coefficients):
        term = mul(power(numerator, exponent), power(denominator, degree - exponent))
        out = add(out, scale(term, F(coefficient)))
    return out


PACKETS = (
    ((2, 6), (1, 0, 1)),
    ((2, 4), (2, -2, 1)),
    ((4, 2), (1, -2, 2)),
    ((1, 2), (2, -4, 6, -4, 1)),
    ((1, 3), (1, -4, 8, -4, 1)),
    ((1, 4), (8, -16, 12, -4, 1)),
    ((1, 5), (1, 0, 6, 0, 1)),
    ((1, 6), (2, -4, 2, 0, 1)),
    ((1, 7), (1, 0, 0, 0, 1)),
    ((2, 1), (1, -4, 6, -4, 2)),
    ((2, 3), (1, 0, 2, -4, 2)),
    ((4, 1), (1, -4, 12, -16, 8)),
)


def pair_orbit(pair: tuple[int, int]) -> frozenset[tuple[int, int]]:
    return frozenset(((unit * pair[0]) % 8, (unit * pair[1]) % 8) for unit in UNITS)


def main() -> None:
    all_pairs = {(a, b) for a in range(1, 8) for b in range(1, 8) if a != b}
    orbits = {pair_orbit(pair) for pair in all_pairs}
    assert len(orbits) == 12
    assert sorted(len(orbit) for orbit in orbits) == [2, 2, 2] + [4] * 9
    assert {pair_orbit(pair) for pair, _ in PACKETS} == orbits

    total_degree = 0
    for (a, b), coefficients in PACKETS:
        numerator = add(power(ZETA, b), scale(ONE, F(-1)))
        denominator = add(power(ZETA, a), scale(ONE, F(-1)))
        assert homogeneous_eval(coefficients, numerator, denominator) == ZERO
        total_degree += len(coefficients) - 1
    assert total_degree == 42

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(GRW1)", "(GRW2)", "(GRW3)", "(GRW5)"):
        assert anchor in statement
    for anchor in ("three orbits of size two", "nine representatives", "3*2+9*4"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GALOIS_ROLE_WELD_PASS")


if __name__ == "__main__":
    main()
