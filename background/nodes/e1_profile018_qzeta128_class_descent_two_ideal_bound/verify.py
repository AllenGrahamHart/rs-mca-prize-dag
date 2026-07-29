#!/usr/bin/env python3
"""Verify the proved class-descent implication and source arithmetic."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile018_qzeta128_class_descent_two_ideal_bound"
CERT = "e1_qzeta128_p257_class_orbit_certificate"
DICTIONARY = "e1_profile018_galois_norm_occupancy_dictionary"
CONSUMER = "e1_profile018_m514_five_ideal_occupancy"
CLASS_NUMBER = 359_057
MULTIPLIER = 29_301


def multiplicative_order(value: int, modulus: int) -> int:
    current = 1
    for order in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return order
    raise AssertionError("order not found")


def main() -> None:
    assert multiplicative_order(3, 128) == 32
    units = {
        sign * pow(3, exponent, 128) % 128
        for sign in (1, -1)
        for exponent in range(32)
    }
    assert len(units) == 64

    assert multiplicative_order(MULTIPLIER, CLASS_NUMBER) == 32
    class_orbit = {
        sign * pow(MULTIPLIER, exponent, CLASS_NUMBER) % CLASS_NUMBER
        for sign in (1, -1)
        for exponent in range(32)
    }
    assert len(class_orbit) == 64

    # A primitive generator modulo the Fermat prime exhibits the exact
    # two-to-one map from primitive 256th roots to primitive 128th roots.
    assert multiplicative_order(3, 257) == 256
    roots_256 = {pow(3, exponent, 257) for exponent in range(1, 256, 2)}
    roots_128 = {value * value % 257 for value in roots_256}
    assert len(roots_256) == 128
    assert len(roots_128) == 64
    fibers: dict[int, set[int]] = {}
    for value in roots_256:
        fibers.setdefault(value * value % 257, set()).add(value)
    assert {len(fiber) for fiber in fibers.values()} == {2}
    for fiber in fibers.values():
        left, right = tuple(fiber)
        assert (left + right) % 257 == 0

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    source = (
        ROOT
        / "background/nodes"
        / CERT
        / "source_evidence.md"
    ).read_text()
    for text in ("at most two", CERT, "P_r (1-zeta_256) Q_s"):
        assert text in statement
    for text in ("Cl(L)->Cl(K)", "s^2=t^2 mod 257", "Q_(-s)"):
        assert text in proof
    for text in (
        "e0d441b6207999a110a921a4792d78dee1bfb1d9fa6cbb675c78fc370905a40e",
        "162c0d392e77b07e61271e41d7362e4b44c5791c0e2145046e7d4c0963fa45ee",
        "29301",
    ):
        assert text in source

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[CERT]["status"] == "PROVED"
    assert nodes[DICTIONARY]["status"] == "PROVED"
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "PROVED"
    assert (CERT, NODE, "req") in edges
    assert (DICTIONARY, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    print(
        "E1_PROFILE018_QZETA128_CLASS_DESCENT_TWO_IDEAL_BOUND_PASS "
        "class_orbit=proved lower_classes=64 upper_fiber=2"
    )


if __name__ == "__main__":
    main()
