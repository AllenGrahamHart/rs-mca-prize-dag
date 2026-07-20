#!/usr/bin/env python3
"""Verify quotient anharmonic symmetry and the antipodal twin identity."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_anharmonic_antipodal_twin"
DEPENDENCIES = {
    "f3_h3_quotient_block_identity",
    "f3_h3_dsp8_antipodal_cayley_product_router",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def subgroup(prime: int, order: int) -> list[int]:
    for base in range(2, prime):
        generator = pow(base, (prime - 1) // order, prime)
        if pow(generator, order // 2, prime) != 1:
            return [pow(generator, exponent, prime) for exponent in range(order)]
    raise AssertionError("subgroup generator not found")


def orbit(target: int, prime: int) -> set[int]:
    return {
        target,
        pow(target, -1, prime),
        (1 - target) % prime,
        pow((1 - target) % prime, -1, prime),
        target * pow((target - 1) % prime, -1, prime) % prime,
        (target - 1) * pow(target, -1, prime) % prime,
    }


def signed_support(
    logarithm: dict[int, int], half: int, x: int, y: int, prime: int
) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for value, coefficient in ((x * y % prime, 1), (x, -1), (y, -1)):
        exponent = logarithm[value]
        coordinate = exponent % half
        sign = 1 if exponent < half else -1
        coefficients[coordinate] = coefficients.get(coordinate, 0) + coefficient * sign
    return {key: value for key, value in coefficients.items() if value}


def disjoint_edges(
    target: int,
    prime: int,
    group: list[int],
    group_set: set[int],
    logarithm: dict[int, int],
) -> int:
    pairs = set()
    for x in group:
        if x == 1:
            continue
        y = (1 - target * pow((1 - x) % prime, -1, prime)) % prime
        if y in group_set and y != 1:
            pairs.add(tuple(sorted((x, y))))
    supports = []
    for x, y in pairs:
        support = signed_support(logarithm, len(group) // 2, x, y, prime)
        if len(support) == 3 and all(abs(value) == 1 for value in support.values()):
            supports.append(set(support))
    return sum(
        supports[left].isdisjoint(supports[right])
        for left in range(len(supports))
        for right in range(left + 1, len(supports))
    )


def finite_field_check(prime: int = 97, order: int = 32) -> tuple[int, int, int]:
    group = subgroup(prime, order)
    group_set = set(group)
    logarithm = {value: exponent for exponent, value in enumerate(group)}
    shifted = [(1 - value) % prime for value in group if value != 1]
    product = Counter(left * right % prime for left in shifted for right in shifted)
    quotient = Counter(
        right * pow(left, -1, prime) % prime
        for left in shifted
        for right in shifted
    )

    tested = 0
    for target in range(2, prime):
        values = {quotient[value] for value in orbit(target, prime)}
        assert len(values) == 1
        tested += 1

    antipodal = 0
    for a in group:
        if a in {1, prime - 1}:
            continue
        target = (1 - a * a) % prime
        twin = target * pow((target - 1) % prime, -1, prime) % prime
        assert twin == (1 - pow(a, -2, prime)) % prime
        assert product[target] == product[twin]
        assert quotient[target] == quotient[twin]

        for x in group:
            if x == 1:
                continue
            for y in group:
                if y == 1 or (1 - x) * (1 - y) % prime != target:
                    continue
                mapped = (pow(x, -1, prime), y * pow(a, -2, prime) % prime)
                assert 1 not in mapped
                assert (1 - mapped[0]) * (1 - mapped[1]) % prime == twin
        antipodal += 1

    assert product[23] == product[76] == 6
    assert quotient[23] == quotient[76] == 9
    squares = {value * value % prime for value in group}
    assert (1 - 23) % prime in squares
    assert 23 * pow(22, -1, prime) % prime == 76
    first_edges = disjoint_edges(23, prime, group, group_set, logarithm)
    twin_edges = disjoint_edges(76, prime, group, group_set, logarithm)
    assert (first_edges, twin_edges) == (0, 1)
    return tested, antipodal, twin_edges - first_edges


def antipodal_parity_check(prime: int = 193, order: int = 64) -> int:
    group = subgroup(prime, order)
    shifted = [(1 - value) % prime for value in group if value != 1]
    product = Counter(left * right % prime for left in shifted for right in shifted)
    cayley = {
        value: (1 + value) * pow((1 - value) % prime, -1, prime) % prime
        for value in group
        if value not in {1, prime - 1}
    }
    cayley_values = list(cayley.values())
    maximum = 0
    for a, center in cayley.items():
        target = (1 - a * a) % prime
        multiplicity = sum(
            left * right % prime == center
            for left in cayley_values
            for right in cayley_values
        )
        assert product[target] == multiplicity + 2
        assert product[target] % 2 == 0
        assert multiplicity % 2 == 0
        maximum = max(maximum, product[target])
    assert maximum == 26
    return maximum


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "O(t)={t,1/t,1-t,1/(1-t),t/(t-1),(t-1)/t}",
        "P(t)=P(tau(t))",
        "R(t)=R(tau(t))",
        "P(t)>=25iffP(t)>=26iffM_a>=24",
        "doesnotassertequalityof`N_6^disj`",
    ):
        assert marker in statement


def main() -> None:
    tested, antipodal, edge_gap = finite_field_check()
    parity_maximum = antipodal_parity_check()
    packet_check()
    print(
        "F3_H3_QUOTIENT_ANHARMONIC_ANTIPODAL_TWIN_PASS "
        f"targets={tested} antipodal_signs={antipodal} edge_gap={edge_gap} "
        f"parity_max={parity_maximum}"
    )


if __name__ == "__main__":
    main()
