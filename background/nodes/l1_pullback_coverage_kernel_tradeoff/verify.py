#!/usr/bin/env python3
"""Verify the pullback coverage/kernel tradeoff."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_pullback_coverage_kernel_tradeoff"


def component_dimensions(k: int, s: int) -> tuple[int, ...]:
    return tuple(max(0, (k - j + s - 1) // s) for j in range(s))


def main() -> None:
    checks = 0
    for k in range(1, 101):
        for s in range(1, 21):
            dimensions = component_dimensions(k, s)
            assert sum(dimensions) == k
            for b in range(0, 31):
                kappa = sum(max(0, dimension - b) for dimension in dimensions)
                assert kappa == max(0, k - s * b)
                for ell in range(1, 16):
                    threshold = k + ell - 1
                    minimum_z = max(0, threshold - s * b)
                    for z in (minimum_z, minimum_z + 1, minimum_z + 7):
                        assert threshold <= s * b + z
                        assert kappa <= max(0, z - ell + 1)
                        checks += 1

    # The affine-quadratic boundary has fourteen complete-domain points,
    # already exceeding k=8, so its evaluation kernel is zero despite z=5.
    k = 8
    s = 2
    b = 7
    ell = 6
    z = 5
    dimensions = component_dimensions(k, s)
    kappa = sum(max(0, dimension - b) for dimension in dimensions)
    assert dimensions == (4, 4)
    assert kappa == max(0, k - s * b) == 0
    assert kappa <= max(0, z - ell + 1)
    checks += 3

    # Sparse coverage forces the exact loss claimed by CK3/CK4.
    k = 10
    s = 3
    b = 2
    ell = 5
    kappa = max(0, k - s * b)
    minimum_z = k + ell - 1 - s * b
    assert kappa == 4
    assert minimum_z == ell - 1 + kappa == 8
    checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_general_pullback_interleaving_descent",
        "l1_partial_pullback_johnson_router",
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
        "kappa=max(0,k-sb)",
        "kappa<=max(0,z(f)-ell+1)",
        "z(f)<=ell-1       ==> kappa=0",
        "n^(3+gamma K)",
        "not an independent mechanism",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_PULLBACK_COVERAGE_KERNEL_TRADEOFF_PASS checks={checks}")


if __name__ == "__main__":
    main()
