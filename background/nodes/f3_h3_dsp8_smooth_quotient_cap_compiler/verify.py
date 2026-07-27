#!/usr/bin/env python3
"""Verify the DSP8 smooth quotient-cap compiler."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_smooth_quotient_cap_compiler"
DEPENDENCIES = {
    "f3_affine_coset_pair_mattarei_bound",
    "f3_h3_dsp8_smooth_residual_router",
    "f3_h3_dsp8_unit_product_trace_normal_form",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def arithmetic_check() -> None:
    assert 189 * 17 == 3213
    assert 4 * 36086 == 144344
    assert Fraction(144344, 100) == Fraction(36086, 25)
    threshold = Fraction(144344, 3213)
    assert Fraction(44924, 1000) < threshold < Fraction(44926, 1000)
    assert Fraction(189, 100) * 17 * threshold == Fraction(36086, 25)


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
    text = "".join(
        "".join((base / name).read_text().replace("`", "").split())
        for name in ("statement.md", "proof.md", "audit.md")
    )
    for marker in (
        "G_sm^c=sum_(basetuplesinclassc)R(t)",
        "189(10U_sm^0+17U_sm^A)<=144344n^(4/3)",
        "3213(U_sm^0+U_sm^A)<=144344n^(4/3)",
        "L_1(Z)=Z",
        "L_2(Z)=tZ+(1-t)",
        "forgetsonlythequotientpair",
    ):
        assert marker in text, marker


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_H3_DSP8_SMOOTH_QUOTIENT_CAP_COMPILER_PASS "
        "weighted=144344/189 class_blind=144344/3213"
    )


if __name__ == "__main__":
    main()
