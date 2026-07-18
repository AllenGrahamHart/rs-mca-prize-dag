#!/usr/bin/env python3
"""Replay the shifted-energy zero normalization and C36' compiler."""

from __future__ import annotations

import copy
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "f3_h3_shifted_energy_zero_normalization"
DEPENDENCY = "f3_h3_identity_deficit_energy_close"
CONSUMERS = {"f3_h3_mobius_excess_half", "f3_h3_three_to_one_c36"}


def prime_factors(value: int) -> set[int]:
    factors: set[int] = set()
    candidate = 2
    while candidate * candidate <= value:
        if value % candidate == 0:
            factors.add(candidate)
            while value % candidate == 0:
                value //= candidate
        candidate += 1
    if value > 1:
        factors.add(value)
    return factors


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError(("primitive root", prime))


def subgroup(prime: int, order: int) -> tuple[int, ...]:
    generator = pow(primitive_root(prime), (prime - 1) // order, prime)
    values = tuple(pow(generator, exponent, prime) for exponent in range(order))
    if len(set(values)) != order:
        raise AssertionError((prime, order))
    return values


def multiplicative_energy(values: tuple[int, ...], prime: int) -> int:
    products = Counter(left * right % prime for left in values for right in values)
    return sum(count * count for count in products.values())


def finite_checks() -> tuple[int, int]:
    checked = 0
    mutations = 0
    for prime, order in ((17, 8), (97, 16), (97, 32), (193, 64)):
        roots = subgroup(prime, order)
        full = tuple((root - 1) % prime for root in roots)
        deleted = tuple(value for value in full if value != 0)
        full_energy = multiplicative_energy(full, prime)
        deleted_energy = multiplicative_energy(deleted, prime)
        if full_energy != deleted_energy + (2 * order - 1) ** 2:
            raise AssertionError((prime, order, full_energy, deleted_energy))
        if full_energy != deleted_energy + (2 * order - 2) ** 2:
            mutations += 1
        checked += 1
    if mutations != checked:
        raise AssertionError((mutations, checked))
    return checked, mutations


def official_checks() -> int:
    checked = 0
    floor = Fraction(981, 25)
    for exponent in range(13, 42):
        n = 1 << exponent
        target = Fraction(145, 4) * (n - 1) ** 2 + (2 * n - 1) ** 2
        expanded = Fraction(161, 4) * n * n - Fraction(153, 2) * n + Fraction(149, 4)
        if target != expanded:
            raise AssertionError(("expansion", exponent, target, expanded))
        error_floor = Fraction(157, 4) * n * n - Fraction(153, 2) * n + Fraction(149, 4)
        if error_floor <= floor * n * n:
            raise AssertionError(("39.24 floor", exponent, error_floor))
        checked += 1
    return checked


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    if (DEPENDENCY, NODE, "req") not in edges:
        raise AssertionError("dependency")
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer", consumer))


def dag_mutations(dag: dict[str, object]) -> tuple[int, int]:
    cases = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    cases.append(changed)
    changed = copy.deepcopy(dag)
    changed["edges"] = [
        row
        for row in changed["edges"]
        if not (row["from"] == DEPENDENCY and row["to"] == NODE)
    ]
    cases.append(changed)
    caught = 0
    for case in cases:
        try:
            validate_dag(case)
        except AssertionError:
            caught += 1
    if caught != len(cases):
        raise AssertionError((caught, len(cases)))
    return caught, len(cases)


def main() -> None:
    finite, zero_mutations = finite_checks()
    official = official_checks()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    caught, total = dag_mutations(dag)
    print(
        "F3_H3_SHIFTED_ENERGY_ZERO_NORMALIZATION_PASS "
        f"finite={finite} official={official} "
        f"zero_mutations={zero_mutations}/{finite} dag_mutations={caught}/{total}"
    )


if __name__ == "__main__":
    main()
