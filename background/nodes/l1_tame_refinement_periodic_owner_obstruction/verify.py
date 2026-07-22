#!/usr/bin/env python3
"""Verify the tame-refinement periodic-owner obstruction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_tame_refinement_periodic_owner_obstruction"


def main() -> None:
    checks = 0
    prime = 17
    domain = set(range(1, prime))
    k = 8
    sigma = 5
    ell = 6
    petal = {1, 2, 3, 11, 12, 13}
    core = {7, 8, 9, 10, 14, 15, 16}
    remainder = {4, 5, 6}
    agreement = core | petal

    assert core.isdisjoint(petal)
    assert remainder == domain - agreement
    assert len(core) == k - 1
    assert len(petal) == ell
    assert len(agreement) == k + sigma
    assert len(remainder) < ell
    checks += 6

    def quotient(x: int) -> int:
        return (x * x + 3 * x) % prime

    fibers = ((4, {1, 13}), (10, {2, 12}), (1, {3, 11}))
    union: set[int] = set()
    for label, fiber in fibers:
        assert len(fiber) == 2
        assert all(quotient(x) == label for x in fiber)
        assert {x for x in range(prime) if quotient(x) == label} == fiber
        assert union.isdisjoint(fiber)
        union |= fiber
        checks += 4
    assert union == petal
    assert prime % (ell // 2) != 0
    checks += 2

    received = {x: (0 if x in agreement else 1) for x in domain}
    exact_zero_agreement = {x for x in domain if received[x] == 0}
    assert exact_zero_agreement == agreement
    checks += 1

    stabilizer = {
        scalar
        for scalar in domain
        if {(scalar * x) % prime for x in agreement} == agreement
    }
    remainder_stabilizer = {
        scalar
        for scalar in domain
        if {(scalar * x) % prime for x in remainder} == remainder
    }
    assert stabilizer == remainder_stabilizer == {1}
    assert {(-x) % prime for x in petal} != petal
    checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_tame_fixed_petal_refinement_census",
        "pma_exact_periodic_owner",
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
        "P(X)=X^2+3X",
        "P^(-1)(4) ={1,13}",
        "Stab_H(A)={1}",
        "general polynomial-",
        "not an official-row counterexample",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_TAME_REFINEMENT_PERIODIC_OWNER_OBSTRUCTION_PASS checks={checks}")


if __name__ == "__main__":
    main()
