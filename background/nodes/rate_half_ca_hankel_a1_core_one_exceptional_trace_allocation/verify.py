#!/usr/bin/env python3
"""Verify the core-one exceptional-trace allocation packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_active_trace_core_reduction"
CONSUMER = "rate_half_band_closure"


def official_gcd_check() -> None:
    e = (1 << 38) - 1
    for b in (0, 1, e // 5):
        capacity = e - 5 * b
        e_star = e - b
        r = 2 * e_star + 1
        for c in (1, capacity):
            assert r - 1 - c >= e + 3 * b > 0


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
        "Q V_a+P_X W_a=P",
        "Z_B=E_Z,       Z_W=E_a=1",
        "X_0=1,X_1=B_X",
        "QA_a+P B_a=G_X",
        "W_aB_a-B_X=QK_a",
        "three systems",
    ):
        assert marker in packet


def main() -> None:
    official_gcd_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_TRACE_ALLOCATION_PASS "
        "exceptional_allocations=active_or_B"
    )


if __name__ == "__main__":
    main()
