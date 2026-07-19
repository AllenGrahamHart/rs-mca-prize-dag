#!/usr/bin/env python3
"""Verify the core-one active-trace core-reduction packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_active_trace_core_reduction"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_trace_free_exclusion"
CONSUMER = "rate_half_band_closure"


def official_capacity_check() -> None:
    e = (1 << 38) - 1
    for b in (0, 1, e // 5):
        e_star = e - b
        for slope_deficit in (0, 1):
            capacity = e - 5 * b - 1 + slope_deficit
            if not slope_deficit:
                assert capacity < e_star
            else:
                assert 2 * (e_star - 1) > capacity
                if capacity >= e_star - 1:
                    assert b == 0
                    assert capacity == e_star
                    assert capacity - (e_star - 1) == 1


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
        "B_X=X_0X_1",
        "K=X_0Z_WZ_BK_a",
        "W_aB_a-X_1E_a=QK_a",
        "z(e_*-D_*)<=C_*",
        "epsilon_0=0:       c=1, X_1=1, E_a=E_Z",
        "epsilon_0=1:       c=2, X_1 has one root of deficit 1",
    ):
        assert marker in packet


def main() -> None:
    official_capacity_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_TRACE_CORE_REDUCTION_PASS "
        "zero_domain_rows=0_or_boundary_one"
    )


if __name__ == "__main__":
    main()
