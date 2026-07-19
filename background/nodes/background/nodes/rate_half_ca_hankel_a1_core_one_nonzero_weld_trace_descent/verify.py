#!/usr/bin/env python3
"""Verify the core-one nonzero-weld trace-descent packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_zero_weld_exclusion"
CONSUMER = "rate_half_band_closure"


def official_degree_check() -> None:
    e = (1 << 38) - 1
    d0 = 8 * e + 7
    t = 4 * e + 1
    for b in (0, 1, e // 5):
        e_star = e - b
        r = 2 * e_star + 1
        for slope_deficit in (0, 1):
            capacity = e - 5 * b - 1 + slope_deficit
            assert capacity >= 2
            for c in (1, capacity):
                assert d0 - 1 - c >= 0
                assert t - 1 - slope_deficit >= 0
                if slope_deficit:
                    assert r - 1 - c >= e + 3 * b
                    assert c + 1 <= e - 5 * b + 1


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    refs = set(nodes[NODE]["refs"])
    for name in required:
        assert f"background/nodes/{NODE}/{name}" in refs
    assert f"background/nodes/{NODE}/statement.md" in nodes[CONSUMER]["refs"]

    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "K_x=-H_x J_x",
        "deg Qhat_x=delta_x+epsilon_x",
        "a_0>=r-1-c>=e+3b",
        "B_X E_Z divides K",
        "W_1B_1-1=QK_1",
        "K_1!=0",
    ):
        assert marker in packet


def main() -> None:
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_NONZERO_WELD_TRACE_DESCENT_PASS "
        "branches=active_trace,factor_descent"
    )


if __name__ == "__main__":
    main()
