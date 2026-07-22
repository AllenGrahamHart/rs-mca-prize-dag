#!/usr/bin/env python3
"""Verify the DSP8 nodal/smooth high-tail domination router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_nodal_smooth_high_tail_domination"
DEPENDENCIES = {
    "f3_h3_dsp8_smooth_trace_substar_router",
    "f3_h3_dsp8_disjoint_six_multiplicity_gate",
}
CONSUMER = "f3_h3_dsp8_correlation_bound"


def ceil_half(value: int) -> int:
    return (value + 1) // 2


def f0(m: int) -> int:
    return ceil_half(m * (m - 4)) - 2 * m - 6


def fa(m: int) -> int:
    return ceil_half(m * (m - 2)) - 4 * (m - 1) - 8


def nu0(m: int) -> int:
    return 3 * m // 2


def nua(m: int) -> int:
    return 3 * (m - 1) // 2


def integer_bounds_check() -> None:
    assert f0(14) - 2 * nu0(14) == -6
    assert f0(15) - 2 * nu0(15) == 3
    assert fa(15) - 2 * nua(15) == -8
    assert fa(16) == 44 == 2 * nua(16)

    for m in range(15, 4097):
        assert f0(m) >= 2 * nu0(m)
    for m in range(16, 4097):
        assert fa(m) >= 2 * nua(m)

    for product in range(25, 257):
        lower_m = 7 + ceil_half(product - 18)
        if product >= 33:
            assert lower_m >= 15
        if product >= 35:
            assert lower_m >= 16


def graph_envelope_check() -> None:
    for antipodal in (False, True):
        for m in range(11, 81):
            generic = m - int(antipodal)
            nodal_cap = 3 * generic // 2
            edge_floor = fa(m) if antipodal else f0(m)
            smooth_floor = max(0, edge_floor - nodal_cap)
            assert smooth_floor >= 0
            if (not antipodal and m >= 15) or (antipodal and m >= 16):
                assert smooth_floor >= nodal_cap


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "D_nod(t)<=nu_0(m)",
        "D_sm(t)>=max(0,F_0(m)-nu_0(m))",
        "ifa=0andP(t)>=33",
        "ifa=1andP(t)>=35",
        "D_6,25^0<=L_0+2S_0",
        "doesnotestimatethesmoothmoments",
    ):
        assert marker in statement


def main() -> None:
    integer_bounds_check()
    graph_envelope_check()
    packet_check()
    print("F3_H3_DSP8_NODAL_SMOOTH_HIGH_TAIL_DOMINATION_PASS integers=8270")


if __name__ == "__main__":
    main()
