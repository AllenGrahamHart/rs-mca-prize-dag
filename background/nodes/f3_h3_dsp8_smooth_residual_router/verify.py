#!/usr/bin/env python3
"""Verify the exact post-Mattarei DSP8 smooth residual ledger."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_smooth_residual_router"
DEPENDENCIES = {
    "f3_h3_dsp8_unit_trace_elliptic_curve_router",
    "f3_h3_dsp8_nodal_cube_preimage_envelope",
    "f3_h3_dsp8_global_overlap_cover_payment",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def arithmetic_check() -> None:
    raw_allowance = 4 * Fraction(12134, 25)
    assert raw_allowance == Fraction(48536, 25)
    assert raw_allowance - 116 == Fraction(45636, 25)
    assert raw_allowance - 498 == Fraction(36086, 25)
    assert Fraction(36086, 25) / 4 == Fraction(18043, 50)
    assert Fraction(36086, 25) < Fraction(45636, 25)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    statement = "".join((base / "statement.md").read_text().split())
    proof = "".join((base / "proof.md").read_text().split())
    for marker in (
        "G_25^c=G_sm^c+G_sing^c",
        "W_sm<=(45636/25)n^2",
        "W_sm<=(36086/25)n^2",
        "10K_sm^0+17K_sm^A<=(18043/50)n^2",
        "4*(12134/25)=48536/25",
        "suppliesnoestimateforthesmooth",
    ):
        assert marker in statement + proof, marker


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_H3_DSP8_SMOOTH_RESIDUAL_ROUTER_PASS "
        "raw_allowance=48536/25 smooth_uniform=36086/25 "
        "smooth_k=18043/50"
    )


if __name__ == "__main__":
    main()

