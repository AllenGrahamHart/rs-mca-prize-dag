#!/usr/bin/env python3
"""Check the official degree-eight coefficient-field router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_coefficient_field_degree_eight_router"
DEPS = {
    "l1_mersenne_next_to_maximal_belyi_shifted_value_gate",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler",
}
CONSUMER = "l1_mixed_petal_amplification"
ROWS = ((13, 8191), (17, 131071), (19, 524287), (31, 2147483647))


def arithmetic_check() -> None:
    for t, prime in ROWS:
        assert prime == 2**t - 1
        order = 2 ** (t + 3)
        assert prime**2 % order == 1 - order // 4
        assert prime**4 % order == 1 - order // 2
        assert prime**8 % order == 1
        assert all(prime**exponent % order != 1 for exponent in (1, 2, 4))
    assert {degree for degree in range(1, 17) if 8 % degree == 0} == {1, 2, 4, 8}


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
    for marker in ("ord_n(p)=8", "d,g_1,x,b,z in K", "deg f divides 8", "{1,2,4,8}"):
        assert marker in packet


def main() -> None:
    arithmetic_check()
    packet_check()
    print("L1_M8_H7_CUBIC_COEFFICIENT_FIELD_DEGREE_EIGHT_ROUTER_PASS rows=4 degrees=1,2,4,8")


if __name__ == "__main__":
    main()
