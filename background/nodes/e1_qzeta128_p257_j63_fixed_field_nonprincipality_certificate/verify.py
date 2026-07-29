#!/usr/bin/env python3
"""Verify the exact interface of the remaining J_63 fixed-field target."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_qzeta128_p257_j63_fixed_field_nonprincipality_certificate"
JOIN = "e1_qzeta128_p257_two_involution_nonprincipality_certificate"

F63 = {
    32: 1,
    30: 32,
    28: 464,
    26: 4032,
    24: 23400,
    22: 95680,
    20: 283360,
    18: 615296,
    16: 980628,
    14: 1136960,
    12: 940576,
    10: 537472,
    8: 201552,
    6: 45696,
    4: 5440,
    2: 256,
    0: 2,
}


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("order not found")


def evaluate_f63(value: int) -> int:
    return sum(coefficient * pow(value, degree, 257) for degree, coefficient in F63.items()) % 257


def main() -> None:
    assert multiplicative_order(9, 257) == 128
    assert pow(9, 63, 257) == 57
    assert pow(9, -1, 257) == 200
    assert pow(57, -1, 257) == 248
    assert (9 - pow(9, -1, 257)) % 257 == 66
    assert (57 - pow(57, -1, 257)) % 257 == 66
    assert 63 * 63 % 128 == 1

    roots = {value for value in range(257) if evaluate_f63(value) == 0}
    assert len(roots) == 32
    assert 66 in roots

    units = {value for value in range(128) if value % 2}
    fixed_subgroup = {1, 63}
    quotient_cosets = {
        frozenset({value, value * 63 % 128})
        for value in units
    }
    generated_cosets = set()
    value = 1
    for _ in range(32):
        generated_cosets.add(frozenset({value, value * 63 % 128}))
        value = value * 3 % 128
    assert value in fixed_subgroup
    assert generated_cosets == quotient_cosets

    # Ambiguous class-number formula: h(Q)*(32*2)/32 divided by unit index 2.
    assert (1 * 32 * 2) // (32 * 2) == 1

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    contract = (node_dir / "claim_contract.md").read_text()
    for text in ("E_63=Q(beta)", "p_66=(257,beta-66)", "TARGET"):
        assert text in statement
    for text in ("degree-32", "21121", "bnfcertify(B,1)"):
        assert text in contract

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "TARGET"
    assert nodes[JOIN]["status"] == "CONDITIONAL"
    assert (NODE, JOIN, "req") in edges

    print(
        "E1_QZETA128_P257_J63_FIXED_FIELD_INTERFACE_PASS "
        "degree=32 residue=66 split_roots=32 cyclic_quotient=32 open_tests=1"
    )


if __name__ == "__main__":
    main()
