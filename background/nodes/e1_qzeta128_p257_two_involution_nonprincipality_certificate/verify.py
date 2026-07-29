#!/usr/bin/env python3
"""Verify the exact interface of the conditional two-involution join."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_qzeta128_p257_two_involution_nonprincipality_certificate"
CONSUMER = "e1_qzeta128_p257_class_orbit_certificate"
J63 = "e1_qzeta128_p257_j63_fixed_field_nonprincipality_certificate"
J65 = "e1_qzeta128_p257_j65_harbater_nonprincipality"


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
    assert (9 - pow(9, -1, 257)) % 257 == 66
    assert (57 - pow(57, -1, 257)) % 257 == 66

    units = {value for value in range(128) if value % 2}
    involutions = {value for value in units if value != 1 and value * value % 128 == 1}
    assert involutions == {63, 65, 127}

    roots = {pow(9, exponent, 257) for exponent in units}
    assert len(roots) == 64
    assert all(pow(root, 64, 257) == 256 for root in roots)

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    contract = (node_dir / "claim_contract.md").read_text()
    for text in ("q_63=(257,zeta-57)", "q_65=(257,zeta-248)", "nonprincipal"):
        assert text in statement
    for text in ("bnfcertify(B,1)", "J_63", "J_65", "p_66"):
        assert text in contract

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "CONDITIONAL"
    assert nodes[J63]["status"] == "TARGET"
    assert nodes[J65]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "CONDITIONAL"
    assert (J63, NODE, "req") in edges
    assert (J65, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    print(
        "E1_QZETA128_P257_TWO_INVOLUTION_JOIN_PASS "
        "roots=64 involutions=3 proved_tests=1 open_tests=1"
    )


if __name__ == "__main__":
    main()
