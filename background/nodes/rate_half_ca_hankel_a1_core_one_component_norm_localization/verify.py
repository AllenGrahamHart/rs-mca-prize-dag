#!/usr/bin/env python3
"""Verify the core-one componentwise norm localization packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_component_norm_localization"
DEPENDENCIES = {
    "rate_half_ca_hankel_a1_core_one_max_component_localization",
    "rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization",
}
CONSUMER = "rate_half_band_closure"


def arithmetic_check(m: int) -> None:
    e = 2 * m - 1
    residual_domain = 16 * m - 1
    supported = 4 * e + 1
    assert residual_domain == 8 * e + 7
    for residual_e in range(e // 5 + 1):
        dominant_e = e - residual_e
        dominant_difference = residual_domain * dominant_e - supported * (
            2 * dominant_e + 1
        )
        assert dominant_difference == e - 5 * residual_e - 1
        for omission in (0, 1):
            dominant_capacity = dominant_difference + omission
            if dominant_capacity >= 0:
                assert residual_domain - dominant_capacity >= 14 * m + 5 * residual_e
    for component_e in range(1, e + 1):
        for omission in (0, 1):
            capacity = residual_domain * component_e - supported * (2 * component_e) + omission
            assert capacity == 5 * component_e + omission


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all((dependency, NODE, "req") in edges for dependency in DEPENDENCIES)
    assert (NODE, CONSUMER, "ev") in edges
    assert f"background/nodes/{NODE}/statement.md" in nodes[CONSUMER]["refs"]

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "sum_i D_i=O-E in {0,1}",
        "C_*=e-5b-1+D_*",
        "C_i=5e_i+D_i",
        "D_0-C_*>=14m+5b",
        "J_i R_i=P^r_i S_i",
        "Q_i V_i+P_sat,i W_i=P",
    ):
        assert marker in packet


def main() -> None:
    for m in range(3, 256):
        arithmetic_check(m)
    m = 1 << 37
    e = 2 * m - 1
    residual_e = e // 5
    assert e % 5 == 3
    assert e - 5 * residual_e - 1 == 2
    assert 14 * m + 5 * residual_e == 2_199_023_255_548
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_COMPONENT_NORM_LOCALIZATION_PASS "
        f"official_e={e} minimum_dominant_residual=2"
    )


if __name__ == "__main__":
    main()
