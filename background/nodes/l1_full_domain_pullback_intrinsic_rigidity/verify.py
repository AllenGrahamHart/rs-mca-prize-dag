#!/usr/bin/env python3
"""Verify full-domain pullback intrinsic rigidity on exhaustive finite rows."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_full_domain_pullback_intrinsic_rigidity"


def evaluate(coefficients: tuple[int, ...], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * value + coefficient) % prime
    return out


def subgroup(prime: int, generator: int, order: int, scalar: int = 1) -> tuple[int, ...]:
    return tuple(sorted({scalar * pow(generator, exponent, prime) % prime for exponent in range(order)}))


def verify_case(prime: int, domain: tuple[int, ...], degree: int) -> int:
    assert len(domain) % degree == 0
    full_partitions = 0
    checks = 0
    for lower in itertools.product(range(prime), repeat=degree):
        polynomial = lower + (1,)
        fibers: dict[int, list[int]] = {}
        for x in domain:
            fibers.setdefault(evaluate(polynomial, x, prime), []).append(x)
        if any(len(fiber) != degree for fiber in fibers.values()):
            continue
        assert len(fibers) == len(domain) // degree
        assert all(coefficient == 0 for coefficient in polynomial[1:degree])
        full_partitions += 1
        checks += len(domain) + 2
    assert full_partitions == prime
    return checks + 1


def main() -> None:
    checks = 0
    cases = (
        (7, tuple(range(1, 7)), 2),
        (7, tuple(range(1, 7)), 3),
        (13, tuple(range(1, 13)), 2),
        (13, tuple(range(1, 13)), 3),
        (13, subgroup(13, 4, 6), 2),
        (13, subgroup(13, 4, 6), 3),
        (17, subgroup(17, 2, 8), 2),
        (17, subgroup(17, 2, 8), 4),
        (17, subgroup(17, 2, 8, scalar=3), 2),
    )
    for prime, domain, degree in cases:
        checks += verify_case(prime, domain, degree)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_general_pullback_interleaving_descent",
        "pma_exact_periodic_owner",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_full_pullback_divisibility_johnson_closure",
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "H=alpha mu_n subset K^*",
        "P(X)=X^s+c",
        "pma_exact_periodic_owner",
        "no non-intrinsic full-domain pullback branch",
        "incomplete fibers or residual domain points",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_FULL_DOMAIN_PULLBACK_INTRINSIC_RIGIDITY_PASS checks={checks}")


if __name__ == "__main__":
    main()
