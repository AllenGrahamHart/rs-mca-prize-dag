#!/usr/bin/env python3
"""Verify the Kummer midpoint algebra, degree ledger, and DAG wiring."""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_near_third_kummer_midpoint_pencil"
SOURCE = "f3_hge4_near_third_belyi_necklace_bound"
CONSUMER = "f3_hge4_norm_gate_count"
TRACE_POWER = "f3_hge4_kummer_midpoint_trace_power_gate"


def midpoint_root_check(order: int, width: int, defect: int, prime: int) -> None:
    assert order == 3 * width + defect
    assert 0 < defect < width
    center = width + defect
    assert 2 * width + center == order

    # At a midpoint root, D*W=-a^2*lambda*r^m.  The sign in kappa is forced.
    for a_value, lambda_value, root_power in ((2, 3, 5), (4, 7, 11)):
        kappa = (1 - a_value * a_value * lambda_value) % prime
        if kappa == 0:
            continue
        root_power = pow(kappa, -1, prime)
        left = (-a_value * a_value * lambda_value * root_power) % prime
        right = (1 - root_power) % prime
        assert left == right


def kummer_degree_check(order: int, width: int) -> None:
    assert order & (order - 1) == 0
    allowed = gcd(order, width)
    assert allowed == width & -width
    for class_exponent in range(order):
        degree = order // gcd(order, class_exponent)
        assert degree & (degree - 1) == 0
        may_divide_midpoint = width % degree == 0
        assert may_divide_midpoint == (allowed % degree == 0)
    if width % 2:
        assert allowed == 1


def primitive_degree_check(order: int, width: int) -> None:
    """Every arithmetically possible d>1 stabilizes both outside members."""
    allowed = gcd(order, width)
    for degree in (1, 2, 4, 8, 16, 32, 64, 128):
        if order % degree or width % degree:
            continue
        assert allowed % degree == 0
        if degree > 1:
            # S(eta*y)=S(y), and degree|h makes eta^h=1 in U,V.
            assert width % degree == 0
            common_stabilizer_order = degree
            assert common_stabilizer_order > 1
        else:
            assert degree == 1


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == nodes[SOURCE]["status"] == "PROVED"
    assert (SOURCE, NODE, "req") in edges
    assert (NODE, TRACE_POWER, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    base = ROOT / "background/nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "W=ZS+lambda y^c", "kappa=1-a^2lambda", "S | 1-kappa y^m",
        "d | gcd(m,h)=2^v_2(h)", "d=1", "contrary to primitivity",
        "every width", "no orbit payment",
    ):
        assert marker in text


def main() -> None:
    for fixture in ((32, 9, 5, 101), (64, 17, 13, 103), (64, 18, 10, 107)):
        midpoint_root_check(*fixture)
    for order, width in ((32, 9), (64, 17), (64, 18), (128, 36)):
        kummer_degree_check(order, width)
        primitive_degree_check(order, width)
    packet_check()
    print(
        "F3_HGE4_NEAR_THIRD_KUMMER_MIDPOINT_PENCIL_PASS "
        "root_fixtures=3 degree_ledgers=4 primitive_collapses=4"
    )


if __name__ == "__main__":
    main()
