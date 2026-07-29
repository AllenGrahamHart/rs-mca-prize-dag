#!/usr/bin/env python3
"""Verify the two-involution conditional class-orbit reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_qzeta128_p257_class_orbit_certificate"
PREMISE = "e1_qzeta128_p257_two_involution_nonprincipality_certificate"
REAL_CLASS = "e1_conductor256_full_unit_circular_basis"
CONSUMER = "e1_profile018_qzeta128_class_descent_two_ideal_bound"


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("order not found")


def main() -> None:
    assert multiplicative_order(9, 257) == 128
    assert pow(9, 63, 257) == 57
    assert pow(9, 65, 257) == 248

    group = {value for value in range(128) if value % 2}
    involutions = {value for value in group if value != 1 and value * value % 128 == 1}
    assert len(group) == 64
    assert involutions == {63, 65, 127}
    assert 127 * 65 % 128 == 63
    assert 127 * 63 % 128 == 65

    # Each cyclic subgroup check is enough to audit the 2-group fact here.
    for generator in group:
        subgroup = set()
        value = 1
        while value not in subgroup:
            subgroup.add(value)
            value = value * generator % 128
        assert subgroup == {1} or subgroup & involutions

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    source = (node_dir / "source_evidence.md").read_text()
    for text in (PREMISE, "pairwise distinct", "class number one"):
        assert text in statement
    for text in ("q_1 q_63", "q_1 q_65", "Every nontrivial subgroup"):
        assert text in proof
    for text in ("Appendix C.1", "Weber's theorem", "162c0d392e77b07e61271e41d7362e4b44c5791c0e2145046e7d4c0963fa45ee"):
        assert text in source

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[PREMISE]["status"] == "TARGET"
    assert nodes[REAL_CLASS]["status"] == "PROVED"
    assert nodes[NODE]["status"] == "CONDITIONAL"
    assert nodes[CONSUMER]["status"] == "CONDITIONAL"
    assert (PREMISE, NODE, "req") in edges
    assert (REAL_CLASS, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    print(
        "E1_QZETA128_P257_CLASS_ORBIT_TWO_INVOLUTION_REDUCTION_PASS "
        "group_order=64 involutions=3 open_nonprincipality_tests=2"
    )


if __name__ == "__main__":
    main()
