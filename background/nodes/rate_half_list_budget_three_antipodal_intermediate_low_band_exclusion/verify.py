#!/usr/bin/env python3
"""Verify the official intermediate low-band exclusion arithmetic."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_low_band_exclusion"
DEPENDENCY = "rate_half_list_budget_three_antipodal_intermediate_residual_square_gcd_gate"
CONSUMER = "rate_half_list_adjacent_crossing"


def degree_check() -> None:
    r_value = (1 << 37) - 1
    d_value = 4 * r_value + 4
    floor_value = ((1 << 38) - 4) // 3
    threshold = (7 * r_value - 14 + 9) // 10
    assert d_value == 1 << 39
    assert floor_value == 91_625_968_980
    assert threshold == 96_207_267_429
    assert threshold - floor_value == 4_581_298_449

    floor_t = 3 * floor_value - 2 * r_value + 4
    assert floor_t == 2 and 18 < floor_value

    for ell in (1, 2, 10, threshold - floor_value - 1):
        v_value = floor_value + ell
        t_value = 3 * v_value - 2 * r_value + 4
        assert t_value == 2 + 3 * ell and t_value >= 5
        assert 7 * t_value < v_value
        assert t_value + 3 * r_value <= 4 * r_value + 1 < d_value

    v_value = threshold
    t_value = 3 * v_value - 2 * r_value + 4
    assert 7 * t_value >= v_value
    assert 10 * (threshold - 1) < 7 * r_value - 14
    assert 10 * threshold >= 7 * r_value - 14


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "t=deg T=r+4-3h=3v-2r+4", "deg J=7t",
        "v>=ceil((7r-14)/10)=96,207,267,429",
        "91,625,968,980 <= v <= 96,207,267,428",
        "4,581,298,449", "does not exclude",
    ):
        assert marker in statement


def main() -> None:
    degree_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_LOW_BAND_PASS "
        "floor=91625968980 first_open=96207267429 excluded=4581298449"
    )


if __name__ == "__main__":
    main()
