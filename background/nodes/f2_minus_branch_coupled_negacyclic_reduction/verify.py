#!/usr/bin/env python3
"""Verify minus-branch order/orbit arithmetic and the DAG contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_minus_branch_coupled_negacyclic_reduction"
PARENTS = {
    "dli_wcl_newton_short_window_exclusion",
    "f2_weighted_kernel_collision_floor",
}
CONSUMER = "f2_conditional_close"


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def dyadic_order(value: int, exponent: int) -> int:
    modulus = 1 << exponent
    x = value % modulus
    order = 1
    while x != 1:
        x = x * x % modulus
        order *= 2
        assert order <= 1 << (exponent - 2)
    return order


def orbit_union(modulus: int, p: int, r: int) -> set[int]:
    h = dyadic_order(p, modulus.bit_length() - 1)
    roots = set()
    for j in range(1, r + 1):
        exponent = 2 * j - 1
        value = exponent
        for _ in range(h):
            roots.add(value % modulus)
            value = value * p % modulus
    assert len(roots) == h * r
    return roots


def main() -> None:
    order_checks = 0
    for exponent in range(3, 14):
        modulus = 1 << exponent
        for p in range(3, modulus, 4):
            expected = 1 << max(1, exponent - v2(p + 1))
            assert dyadic_order(p, exponent) == expected
            order_checks += 1

    n = 1 << 41
    t_max = (n + 40) // 41
    r_max = (t_max + 1) // 2
    assert 2 * r_max < 1 << 36

    orbit_checks = 0
    for exponent in range(8, 15):
        modulus = 1 << exponent
        for p in range(3, modulus, 4):
            h = dyadic_order(p, exponent)
            if h <= 4:
                r = min(7, (modulus // 8 - 1) // 2)
                if r:
                    orbit_union(modulus, p, r)
                    orbit_checks += 1

    official_residues = (
        (1 << 39) - 1,
        3 * (1 << 39) - 1,
        (1 << 40) - 1,
        (1 << 41) - 1,
        (1 << 61) - 1,
    )
    top_checks = 0
    for p in official_residues:
        for exponent in (39, 40, 41):
            h = dyadic_order(p, exponent)
            if h <= 4:
                orbit_union(1 << exponent, p, 64)
                top_checks += 1

    result = json.loads(
        (ROOT / "notes/pilots_20260806/f2_minus_branch/counterexample_result.json").read_text()
    )
    assert result["status"] == "PASS"
    p = (1 << 61) - 1
    assert v2(p + 1) == 61
    assert dyadic_order(p, 41) == 2
    assert p > 1 << 40

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "F2_MINUS_COUPLED_NEGACYCLIC_REDUCTION_PASS "
        f"orders={order_checks} surrogate_orbits={orbit_checks} "
        f"top_orbits={top_checks} official=1 dag=3/3"
    )


if __name__ == "__main__":
    main()
