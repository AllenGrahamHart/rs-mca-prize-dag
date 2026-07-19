#!/usr/bin/env python3
"""Replay the C36' identity-deficit energy close."""

from __future__ import annotations

import copy
import json
from collections import Counter
from decimal import Decimal, getcontext
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3] if len(HERE.parents) > 3 else Path.cwd()
ROOT = REPO_ROOT if (REPO_ROOT / "dag.json").exists() else Path.cwd()
DAG = ROOT / "dag.json"
NODE = "f3_h3_identity_deficit_energy_close"
DEPENDENCIES = {"f3_h2_stepanov_inhouse", "f3_h3_quotient_block_identity"}
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


def finite_identity_checks() -> int:
    checked = 0
    for prime, order in ((17, 8), (97, 16), (97, 32), (193, 64)):
        roots = subgroup(prime, order)
        shifted = tuple((1 - value) % prime for value in roots if value != 1)
        product = Counter(left * right % prime for left in shifted for right in shifted)
        quotient = Counter(
            left * pow(right, -1, prime) % prime
            for left in shifted
            for right in shifted
        )
        labels = set(product) | set(quotient)
        product_energy = sum(value * value for value in product.values())
        quotient_energy = sum(value * value for value in quotient.values())
        correlation = sum(product[label] * quotient[label] for label in labels)
        distance = sum((product[label] - quotient[label]) ** 2 for label in labels)
        if product_energy != quotient_energy:
            raise AssertionError((prime, order, product_energy, quotient_energy))
        if 2 * correlation != 2 * product_energy - distance:
            raise AssertionError((prime, order, correlation, product_energy, distance))
        if quotient[1] != order - 1:
            raise AssertionError((prime, order, quotient[1]))
        checked += 1
    return checked


def official_inequalities() -> tuple[int, int]:
    getcontext().prec = 100
    passed = 0
    mutation_failures = 0
    for exponent in range(13, 42):
        n = Decimal(1 << exponent)
        x = n ** (Decimal(1) / Decimal(3))
        identity_gap = n - 1 - 4 * x * x
        target = 36 * n * n - 16 * x**4 - n / 2
        energy_bound = Decimal(145) * (n - 1) ** 2 / 4
        if energy_bound - identity_gap**2 / 2 >= target:
            raise AssertionError(("official close", exponent))
        if Decimal(145) * (n - 1) ** 2 / 4 <= 35 * n * n:
            raise AssertionError(("strict improvement", exponent))
        passed += 1

        mutated = Decimal(146) * (n - 1) ** 2 / 4 - identity_gap**2 / 2
        if mutated >= target:
            mutation_failures += 1
    if mutation_failures == 0:
        raise AssertionError("constant mutation never failed")

    x = 20
    polynomial = x**6 - 16 * x**5 - 32 * x**4 + 284 * x**3 + 16 * x**2 - 143
    inner = 6 * x**3 - 80 * x**2 - 128 * x + 852
    inner_derivative = 18 * x**2 - 160 * x - 128
    if (polynomial, inner, inner_derivative) != (9_958_257, 14_292, 3_872):
        raise AssertionError((polynomial, inner, inner_derivative))
    return passed, mutation_failures


def validate_dag(data: dict[str, object]) -> None:
    nodes = {row["id"]: row for row in data["nodes"]}
    if nodes.get(NODE, {}).get("status") != "PROVED":
        raise AssertionError("node status")
    edges = {(row["from"], row["to"], row["kind"]) for row in data["edges"]}
    for dependency in DEPENDENCIES:
        if (dependency, NODE, "req") not in edges:
            raise AssertionError(("dependency", dependency))
    for consumer in CONSUMERS:
        if (NODE, consumer, "ev") not in edges:
            raise AssertionError(("consumer", consumer))


def dag_mutation_controls(dag: dict[str, object]) -> int:
    mutations = []
    changed = copy.deepcopy(dag)
    next(row for row in changed["nodes"] if row["id"] == NODE)["status"] = "TARGET"
    mutations.append(changed)
    for dependency in DEPENDENCIES:
        changed = copy.deepcopy(dag)
        changed["edges"] = [
            row
            for row in changed["edges"]
            if not (row["from"] == dependency and row["to"] == NODE)
        ]
        mutations.append(changed)
    caught = 0
    for mutation in mutations:
        try:
            validate_dag(mutation)
        except AssertionError:
            caught += 1
    if caught != len(mutations):
        raise AssertionError((caught, len(mutations)))
    return caught


def main() -> None:
    finite = finite_identity_checks()
    official, constant_mutations = official_inequalities()
    dag = json.loads(DAG.read_text())
    validate_dag(dag)
    mutations = dag_mutation_controls(dag)
    print(
        "F3_H3_IDENTITY_DEFICIT_ENERGY_CLOSE_PASS "
        f"finite={finite} official={official} "
        f"constant_mutations={constant_mutations} "
        f"dag_mutations={mutations}/{mutations}"
    )


if __name__ == "__main__":
    main()
