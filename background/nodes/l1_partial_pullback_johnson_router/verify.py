#!/usr/bin/env python3
"""Verify the partial-pullback Johnson router."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_partial_pullback_johnson_router"


def evaluate(coefficients: tuple[int, ...], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * value + coefficient) % prime
    return out


def verify_f17_boundary() -> int:
    prime = 17
    domain = set(range(1, prime))
    pullback = (0, 3, 1)
    fibers: dict[int, set[int]] = {}
    for x in domain:
        fibers.setdefault(evaluate(pullback, x, prime), set()).add(x)
    complete = {label: fiber for label, fiber in fibers.items() if len(fiber) == 2}
    residual = domain - set().union(*complete.values())
    assert len(complete) == 7
    assert residual == {7, 14}

    agreement = domain - {4, 5, 6}
    fully_agreed = {
        label for label, fiber in complete.items() if fiber <= agreement
    }
    full_points = set().union(*(complete[label] for label in fully_agreed))
    z = len(agreement - full_points)
    assert len(fully_agreed) == 4
    assert len(agreement) == 2 * len(fully_agreed) + z == 13
    assert z == 5

    s = 2
    k = 8
    ell = 6
    b = len(complete)
    caps = [max(0, (k - j + s - 1) // s) for j in range(s)]
    kappa = sum(max(0, cap - b) for cap in caps)
    h_z = (k + ell - 1 - z + s - 1) // s
    degree = (k + s - 1) // s - 1
    assert caps == [4, 4]
    assert kappa == 0
    assert h_z == 4
    assert h_z * h_z < b * degree == 21
    return 13


def verify_tiny_johnson() -> int:
    prime = 3
    labels = (0, 1, 2)
    codewords = tuple(
        tuple((constant + linear * x) % prime for x in labels)
        for constant, linear in itertools.product(range(prime), repeat=2)
    )
    tuples = tuple(itertools.product(codewords, repeat=2))
    received_symbols = tuple(itertools.product(range(prime), repeat=2))
    maximum = 0
    for received in itertools.product(received_symbols, repeat=3):
        size = sum(
            sum(
                (first[index], second[index]) == received[index]
                for index in range(3)
            )
            >= 2
            for first, second in tuples
        )
        maximum = max(maximum, size)
    b = 3
    h = 2
    degree = 1
    bound = b * (h - degree) // (h * h - b * degree)
    assert maximum <= bound == 3
    return len(received_symbols) ** 3 + len(tuples)


def verify_router_arithmetic() -> int:
    checks = 0
    for n in (16, 32, 64, 128):
        for k in (n // 2, n // 4):
            for s in (2, 4, 8):
                for b in range(1, n // s + 1):
                    caps = [max(0, (k - j + s - 1) // s) for j in range(s)]
                    kappa = sum(max(0, cap - b) for cap in caps)
                    assert kappa >= 0
                    for z in range(0, min(n, 2 * s) + 1):
                        threshold = k + min(n - k + 1, n // 4) - 1
                        h = max(0, (threshold - z + s - 1) // s)
                        degree = (k + s - 1) // s - 1
                        if h <= b and h * h > b * degree:
                            denominator = h * h - b * degree
                            bound = b * (h - degree) // denominator
                            assert 0 <= bound <= b * b
                        checks += 1
    return checks


def main() -> None:
    checks = verify_f17_boundary() + verify_tiny_johnson() + verify_router_arithmetic()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_general_pullback_interleaving_descent",
        "l1_tame_fixed_petal_refinement_census",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "z(f)=|Agr(f,U)\\disjoint_union_(a in E_f) T_a|",
        "h_Z=max(0,ceil((a_*-Z)/s))",
        "h_Z^2>b d",
        "q^kappa b^2",
        "affine-quadratic obstruction has `z=5`",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_PARTIAL_PULLBACK_JOHNSON_ROUTER_PASS checks={checks}")


if __name__ == "__main__":
    main()
