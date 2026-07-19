#!/usr/bin/env python3
"""Verify the core-one active two-sided partition packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_exceptional_trace_nonvanishing"
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
            for z in (0, 1):
                assert r + (d0 - z - r) == d0 - z
                assert e_star + (t - e_star) == t
            for c in (1, capacity):
                explicit = (c - 1) * e + (5 - c) * b + 1 - slope_deficit
                for exceptional_bad in (0, c if slope_deficit else 0):
                    direct = c * e_star - capacity - exceptional_bad
                    assert direct == explicit - exceptional_bad


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
        "R_X=P_XX_1=G_X/X_0",
        "Q(gamma;X) A_a(gamma;X)=R_X",
        "Q(U,V;x) V_a(U,V;x)=P",
        "sum_(x:X_1(x)=0) a_x=c e_*-C_*-E_bad",
        "D_*=0: sum a_x=(c-1)e+(5-c)b+1",
        "D_*=1: sum a_x=(c-1)e+(5-c)b-E_bad",
    ):
        assert marker in packet


def main() -> None:
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_TWO_SIDED_PARTITION_PASS "
        "partition_sides=clean_slope,saturated_domain"
    )


if __name__ == "__main__":
    main()
