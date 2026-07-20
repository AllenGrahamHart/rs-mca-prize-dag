#!/usr/bin/env python3
"""Verify the DSP8 accident-depth compiler constants and packet."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_accident_depth_compiler"
DEPENDENCIES = {
    "f3_h3_cutoff18_double_accident_reduction",
    "f3_h3_antipodal_tail_distance_six_split",
    "f3_h3_dsp8_global_overlap_cover_payment",
    "f3_h3_dsp8_primitive_shift_pair_adapter",
    "f3_h3_dsp8_disjoint_six_multiplicity_gate",
    "f3_h3_double_accident_nonzero_coupling_ideal_router",
    "f3_h3_double_accident_coupling_batch_odd_saturation",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}


def budget(n: int, depth: int, cutoff: int) -> int:
    return (
        300 * n * n
        - 17 * depth * (n - 1) ** 2
        - 17 * cutoff * (n - 2) ** 2
    )


def arithmetic_check() -> None:
    for n in (2**s for s in range(13, 42)):
        assert budget(n, 1, 6) == 181 * n * n + 442 * n - 425
        assert budget(n, 1, 14) == 45 * n * n + 986 * n - 969
        assert budget(n, 3, 14) == 11 * n * n + 1054 * n - 1003
        assert budget(n, 3, 14) > 11 * n * n
        assert Fraction(1113 * 45, 136 * 42) == Fraction(2385, 272)
        assert Fraction(1113 * 11, 136 * 42) == Fraction(583, 272)

        for cutoff in (0, 2, 6, 10, 14):
            depth = 17 - cutoff
            expected = (
                11 * n * n
                + (578 + 34 * cutoff) * n
                - (289 + 51 * cutoff)
            )
            assert budget(n, depth, cutoff) == expected > 11 * n * n

        # The n^(5/3) terms cost strictly less than 2601/160 n^2.
        assert n ** Fraction(1, 3) > 20
        for depth in range(1, 12):
            uniform = (
                Fraction(750)
                - Fraction(85 * depth, 2)
                - 255
                - Fraction(2601, 160)
            )
            assert uniform == Fraction(76599 - 6800 * depth, 160)
        assert 76599 - 6800 * 11 == 1799

    # Exact coefficient transport from complete N6 moments to primitive K.
    assert Fraction(4, 5) * 10 == 8
    assert Fraction(4, 5) * 17 == Fraction(68, 5)
    assert Fraction(5, 2) * 300 == 750


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
        "T_L<=T_1<=(n-2)^2",
        "P>=33, R>=4",
        "B_(3,14)(n)=11n^2+1054n-1003",
        "(583/272)n^2",
        "76599-6800L",
        "at least three",
        "I_E^batch O[1/2]=I_E^anchor O[1/2]",
        "four distinct quotient lifts",
        "A product-only",
        "no estimate",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print("F3_H3_DSP8_ACCIDENT_DEPTH_COMPILER_PASS diagonal=5 selected=583/272")


if __name__ == "__main__":
    main()
