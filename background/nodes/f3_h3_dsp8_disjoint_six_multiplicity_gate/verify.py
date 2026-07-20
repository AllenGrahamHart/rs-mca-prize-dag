#!/usr/bin/env python3
"""Verify the DSP8 disjoint-distance-six multiplicity gate."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_disjoint_six_multiplicity_gate"
DEPENDENCIES = {
    "f3_h3_excess_multistar_degree_ladder",
    "f3_h3_distance_four_fiber_degree_cap",
    "f3_h3_distance_six_support_overlap_payment",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}


def d0(m: int) -> int:
    return math.ceil(m * (m - 4) / 2) - 2 * m - 6


def da(m: int) -> int:
    return math.ceil(m * (m - 2) / 2) - 4 * (m - 1) - 8


def arithmetic_check() -> None:
    assert d0(11) == 11
    assert da(11) == 2
    for m in range(11, 1000):
        assert d0(m) >= 11
        assert da(m) >= 2
        if m > 11:
            assert d0(m) > d0(m - 1)
            assert da(m) > da(m - 1)
    for m in range(15, 1000):
        assert math.ceil(2 * d0(m) / m) >= 7
        assert math.ceil(2 * da(m) / (m - 1)) >= 5


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md",
        "dependency_subdag.md", "audit.md", "result.md", "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text()
        for name in ("statement.md", "proof.md", "audit.md", "result.md")
    )
    for marker in (
        "D_0(11)=39-22-6=11",
        "D_A(11)=50-40-8=2",
        "K_0=",
        "K_A=",
        "cross generator",
        "at least seven",
        "at least five",
        "does not bound",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_DSP8_DISJOINT_SIX_MULTIPLICITY_GATE_PASS d0=11 da=2 tail=7/5")


if __name__ == "__main__":
    main()
