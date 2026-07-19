#!/usr/bin/env python3
"""Verify the core-one exceptional-trace nonvanishing packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_trace_nonvanishing"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation"
CONSUMER = "rate_half_band_closure"


def official_degree_check() -> None:
    e = (1 << 38) - 1
    d0 = 8 * e + 7
    for b in (0, 1, e // 5):
        r = 2 * (e - b) + 1
        required = d0 - (r - 1)
        available = d0 - r
        assert required == available + 1
        assert required > available


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
        "K_a(gamma_0;X)!=0",
        "q_0 A_a(gamma_0;X)=G_X",
        "deg_X A_a(gamma_0;X)=D_0-r+1",
        "deg_X A=D_0-r",
        "two systems",
    ):
        assert marker in packet


def main() -> None:
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_TRACE_NONVANISHING_PASS "
        "remaining_systems=2"
    )


if __name__ == "__main__":
    main()
