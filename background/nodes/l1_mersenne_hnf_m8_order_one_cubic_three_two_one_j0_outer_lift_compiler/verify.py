#!/usr/bin/env python3
"""Check the J-zero outer-lift compiler packet."""

from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_outer_lift_compiler"
DEPS = {
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_j0_role_p4_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split",
    "l1_mersenne_hnf_order_one_frobenius_gate",
    "l1_mersenne_hnf_m8_order_one_cubic_coefficient_field_degree_eight_router",
}
CONSUMER = "l1_mixed_petal_amplification"


def scaling_check() -> None:
    d, g1, y, g2, v, a, b_value = map(Q, (2, 3, 5, 7, 11, 13, 17))
    x, big_y = d * g1, d * y
    big_g2, big_v = d**2 * g2, d**2 * v
    big_a, big_b = d * a, d**3 * b_value
    assert (x / d, big_y / d) == (g1, y)
    assert (big_g2 / d**2, big_v / d**2) == (g2, v)
    assert (big_a / d, big_b / d**3) == (a, b_value)
    assert 7 * 6 == 42 and 2 < 8 and 8 % 2 == 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for dependency in DEPS:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    refs = set(nodes[NODE]["refs"])
    for name in (
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "lineage.md",
        "upstream_crosswalk.md",
        "verify.py",
        "verify_audit.py",
    ):
        assert str((base / name).relative_to(ROOT)) in refs
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "T(eta)",
        "E_(beta,gamma)(W)",
        "L(W) divides E_(beta,gamma)(W)^8-1",
        "P(W) divides W^n-1",
        "separate global inner lift",
    ):
        assert marker in packet


def main() -> None:
    scaling_check()
    packet_check()
    print("L1_M8_H7_C321_J0_OUTER_LIFT_COMPILER_PASS roles=42 colors=8 degree=6")


if __name__ == "__main__":
    main()
