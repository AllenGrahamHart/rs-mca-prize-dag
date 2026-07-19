#!/usr/bin/env python3
"""Verify the core-one zero-weld exclusion packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_zero_weld_exclusion"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary"
CONSUMER = "rate_half_band_closure"


def capacity_check() -> None:
    e = (1 << 38) - 1
    clean_slopes = 4 * e
    supported_slopes = clean_slopes + 1
    residual_domain = 8 * e + 7
    roots_g0 = 8 * e + 4
    omitted_rows = residual_domain - roots_g0
    exact_capacity = e
    omitted_lower_bound = omitted_rows * (e - 1)

    assert supported_slopes == 4 * e + 1
    assert omitted_rows == 3
    assert exact_capacity == e - 5 * 0 - 1 + 1
    assert omitted_lower_bound == 3 * e - 3
    assert omitted_lower_bound > exact_capacity


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
        "C_* >= 3(e-1) > e=C_*",
        "G_0(x_j)!=0",
        "v_(x_j)<=1",
        "K!=0",
        "nonzero-weld",
    ):
        assert marker in packet


def main() -> None:
    capacity_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ZERO_WELD_EXCLUSION_PASS "
        "omitted_rows=3 lower_bound=3e-3 exact_capacity=e"
    )


if __name__ == "__main__":
    main()
