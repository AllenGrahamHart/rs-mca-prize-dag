#!/usr/bin/env python3
"""Verify the exact J_63 Stickelberger/Jacobi ideal relation."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_qzeta128_p257_j63_stickelberger_relation"
CONSUMER = "e1_qzeta128_p257_j63_residue_obstruction"
Q = 128
P = 257
ELL = 21121
COEFFICIENTS = [
    21121, -24549, -26280, -22490, -16564, -12336, -20492, -20254,
    -28314, -25086, -29901, -20529, -12414, -5602, -8856, -7172,
    2231, 7193, 0, 3708, 10233, 17881, 9371, 20529, 14851, 21121,
    15861, 21263, 29977, 42499, 39176, 46066,
]
PAIRS = [(32, 32)] + [(1, index - 1) for index in range(2, 33)]


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for order in range(1, modulus):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("order not found")


def carry(a: int, b: int, s: int) -> int:
    return ((a * s) % Q + (b * s) % Q - ((a + b) * s) % Q) // Q


def epsilon(a: int, b: int, s: int) -> int:
    return 1 - carry(a, b, s)


def main() -> None:
    assert multiplicative_order(3, P) == 256
    assert multiplicative_order(9, P) == 128
    assert len(COEFFICIENTS) == len(PAIRS) == 32

    expected = {1: 2 * ELL, 63: 2 * ELL, 65: -2 * ELL, 127: -2 * ELL}
    valuations = {}
    for s in range(1, Q, 2):
        value = sum(
            coefficient * (epsilon(a, b, s) - epsilon(a, b, -s))
            for coefficient, (a, b) in zip(COEFFICIENTS, PAIRS)
        )
        valuations[s] = value
        assert value == expected.get(s, 0)

    for a, b in PAIRS:
        bits = [epsilon(a, b, s) for s in range(1, Q, 2)]
        assert set(bits) <= {0, 1}
        assert sum(bits) == 32
        assert epsilon(a, b, 1) == 1

    node_dir = ROOT / "background/nodes" / NODE
    proof = (node_dir / "proof.md").read_text()
    for text in ("1-carry_i(s)", "2 ell", "j_i/bar(j_i)"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "PROVED"
    assert (NODE, CONSUMER, "req") in edges

    support = [(s, value) for s, value in valuations.items() if value]
    print(
        "E1_QZETA128_P257_J63_STICKELBERGER_RELATION_PASS "
        f"pairs=32 ell={ELL} support={support}"
    )


if __name__ == "__main__":
    main()
