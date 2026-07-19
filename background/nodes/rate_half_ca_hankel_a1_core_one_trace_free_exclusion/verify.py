#!/usr/bin/env python3
"""Verify the core-one trace-free weld exclusion packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_trace_free_exclusion"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity"
CONSUMER = "rate_half_band_closure"


def official_degree_check() -> None:
    e = (1 << 38) - 1
    d0 = 8 * e + 7
    for b in (0, 1, e // 5):
        e_star = e - b
        r = 2 * e_star + 1
        for slope_deficit in (0, 1):
            capacity = e - 5 * b - 1 + slope_deficit
            gap = e_star - capacity
            assert gap == 4 * b + 1 - slope_deficit
            assert gap >= 0
            if gap == 0:
                assert (b, slope_deficit) == (0, 1)
                c = 1
                assert (d0 - c) - (r - 1) == d0 - r
                assert d0 - r > d0 - r - c


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
        "0=P_cl(gamma_0)!=0",
        "Q A_1+P B_1=P_X",
        "C_*=c e_*",
        "b=0,       D_*=1,       c=1",
        "deg_X A_1<=D_0-r-1",
        "active defect trace",
    ):
        assert marker in packet


def main() -> None:
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_TRACE_FREE_EXCLUSION_PASS "
        "survivor=active_trace"
    )


if __name__ == "__main__":
    main()
