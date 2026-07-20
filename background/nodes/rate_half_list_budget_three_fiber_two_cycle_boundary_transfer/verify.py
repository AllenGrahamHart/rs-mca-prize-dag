#!/usr/bin/env python3
"""Verify the doubled-order fiber-two cycle boundary transfer."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_boundary_transfer"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_quotient_embedding",
    "rate_half_list_budget_three_antipodal_reverse_residual_stratification",
    "rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity",
    "rate_half_list_budget_three_antipodal_fourth_root_gap_reduction",
    "rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction",
    "rate_half_list_budget_three_antipodal_generic_two_window_square_reduction",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction",
    "rate_half_list_budget_three_antipodal_generic_canonical_span_criterion",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def ceiling(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def parameter_check(exponent: int) -> tuple[int, int]:
    s = 1 << exponent
    r = s - 1
    generic_v = ceiling(r - 4, 2)
    generic_h = r - generic_v
    generic_t = r + 4 - 2 * generic_h
    assert generic_v == s // 2 - 2
    assert generic_h == s // 2 + 1
    assert generic_t == 1

    intermediate_v = ceiling(2 * r - 4, 3)
    intermediate_h = r - intermediate_v
    intermediate_t = r + 4 - 3 * intermediate_h
    if exponent % 2 == 0:
        assert intermediate_v == (2 * s - 5) // 3
        assert intermediate_h == (s + 2) // 3
        assert intermediate_t == 1
        assert 3 * intermediate_h == s + 2
    else:
        assert intermediate_t == 2

    assert 2 * generic_h == s + 2
    return generic_t, intermediate_t


def official_check() -> None:
    generic_t, intermediate_t = parameter_check(38)
    assert (generic_t, intermediate_t) == (1, 1)
    s = 1 << 38
    h = (1 << 37) + 1
    assert 4 * s == 1 << 40
    assert 8 * h - 8 == 1 << 40
    assert 2 * h - 3 == s - 1
    assert h - 3 == (1 << 37) - 2
    m = 1 << 36
    assert 16 * m == 1 << 40
    assert 8 * m == 1 << 39

    mutation_t = (s - 1) + 4 - 3 * ((s - 1) - ((2 * s - 5) // 3 + 1))
    assert mutation_t != 1


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "v=(2^39-5)/3",
        "a_(2^38)=a_(2^38+1)=0",
        "[z^(2^37-1)]P=[z^(2^37)]P=0",
        "M=2^36",
        "fractional-linear image of the four completion roots",
        "wrong condition",
    ):
        assert marker in statement
    for marker in (
        "rounding\nchanges at the doubled dyadic order",
        "qh=s+2",
        "arbitrary monic quartic denominator",
        "columns",
        "not justified",
    ):
        assert marker in proof


def main() -> None:
    controls = [parameter_check(exponent) for exponent in (8, 9, 10, 11, 12)]
    official_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_CYCLE_BOUNDARY_TRANSFER_PASS "
        f"dyadic_controls={len(controls)} official_generic_T=1 "
        "official_intermediate_T=1 mutation=1"
    )


if __name__ == "__main__":
    main()
