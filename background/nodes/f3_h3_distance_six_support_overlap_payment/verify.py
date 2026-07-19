#!/usr/bin/env python3
"""Verify the distance-six support-overlap payment and DAG wiring."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_distance_six_support_overlap_payment"
DEPENDENCIES = {
    "f3_h3_distance_four_fiber_degree_cap",
    "f3_h3_antipodal_tail_distance_six_split",
    "f3_h3_quotient_block_identity",
}
CONSUMER = "f3_h3_mobius_excess_half"
PRIME = 1_000_003


def inverse(value: int) -> int:
    return pow(value % PRIME, -1, PRIME)


def identity_check() -> None:
    u = 3
    x = 2 * u * u * inverse(1 + u * u) % PRIME
    y = -u % PRIME
    v = -2 * u * inverse(1 + u * u) % PRIME
    assert u * v % PRIME == -x % PRIME
    assert (1 - x) * (1 - y) % PRIME == (1 - u) * (1 - v) % PRIME

    y = 5
    x = (1 + y * y) * inverse(2 * y * y) % PRIME
    u = x * y % PRIME
    v = -inverse(y) % PRIME
    assert u * v % PRIME == -x % PRIME
    assert (1 - x) * (1 - y) % PRIME == (1 - u) * (1 - v) % PRIME

    s = 7
    u = -s % PRIME
    v = 2 * s * inverse(1 + s) % PRIME
    assert (u + v - u * v) % PRIME == s


def arithmetic_check() -> None:
    for exponent in range(13, 42):
        order = 1 << exponent
        quotient_mass = (order - 1) * (order - 2)
        budget = 300 * order * order - 102 * quotient_mass
        residual = Fraction(budget, 8) - Fraction(68, 5) * quotient_mass
        exact = Fraction(750 * order * order - 527 * quotient_mass, 20)
        assert residual == exact
        assert residual > Fraction(223, 20) * order * order


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert all((dependency, NODE, "req") in edges for dependency in DEPENDENCIES)
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "x=2u^2/(1+u^2)",
        "x=(1+y^2)/(2y^2)",
        "O_6(t)<=6",
        "D_6,25^0+(17/10)D_6,25^A <=(223/20)n^2",
    ):
        assert marker in packet


def main() -> None:
    identity_check()
    arithmetic_check()
    packet_check()
    print(
        "F3_H3_DISTANCE_SIX_SUPPORT_OVERLAP_PAYMENT_PASS "
        "generic_cap=6 antipodal_extra=2 residual=223/20"
    )


if __name__ == "__main__":
    main()
